#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024
# Standard library imports
import datetime
import os

# Third party imports
import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from fpdf import FPDF
from reportlab.pdfgen import canvas

from .forms import HostForm
from .models import CadastralData, Property, Reservation, Host


# Create your views here.


def home(request, host_id):
    """
    Homepage of the management app
    :param request:
    :param host_id:
    :return:
    """
    host = get_object_or_404(Host, id=host_id)

    return render(request, "management/home.html", {"host": host})


def profile(request, host_id):
    """
    Homepage of the management app
    :param request:
    :param host_id:
    :return:
    """
    host = get_object_or_404(Host, pk=host_id)
    if request.method == "POST":
        form = HostForm(request.POST, request.FILES, instance=host)
        if form.is_valid():
            form.save()
    else:
        form = HostForm(instance=host)

    return render(
        request,
        "management/profile.html",
        {
            "host": host,
            "form": form,
        },
    )


def login(request):
    return render(request, "management/login.html")


def apartments(request):
    response = requests.get(
        "https://login.smoobu.com/api/apartments",
        headers={
            "Content-type": "application/json",
            "Api-Key": os.getenv("APIKEY"),
        },
    )
    print(response)
    data = response.json()
    for apt in data["apartments"]:
        response_single = requests.get(
            f"https://login.smoobu.com/api/apartments/{apt['id']}",
            headers={
                "Content-type": "application/json",
                "Api-Key": os.getenv("APIKEY"),
            },
        )
        location = response_single.json()["location"]
        timeZone = response_single.json()["timeZone"]
        # insert if not existing and update if existes
        if not Property.objects.filter(smoobu_id=apt["id"]).exists():
            Property(
                name=apt["name"],
                smoobu_id=apt["id"],
                street=location["street"],
                zip=location["zip"],
                city=location["city"],
                country=location["country"],
                latitude=location["latitude"],
                longitude=location["longitude"],
                time_zone=timeZone,
            ).save()
        else:
            Property.objects.filter(smoobu_id=apt["id"]).update(
                name=apt["name"],
                smoobu_id=apt["id"],
                street=location["street"],
                zip=location["zip"],
                city=location["city"],
                country=location["country"],
                latitude=location["latitude"],
                longitude=location["longitude"],
                time_zone=timeZone,
            )

    return render(request, "management/apartments.html")


def reservations(request):
    params = {
        "page": 1,
        "page_size": 25,
        "from": "2023-09-01",
    }

    # Initial parameters
    params = {"page": 1, "page_size": 25}

    # List to store all bookings
    all_bookings = []

    loop = True
    # Make the API call
    while loop:
        response = requests.get(
            "https://login.smoobu.com/api/reservations",
            params=params,
            headers={
                "Content-type": "application/json",
                "Api-Key": os.getenv("APIKEY"),
            },
        )
        print("getting page", params["page"])

        # Check if the response is valid
        if response.status_code == 200:
            data = response.json()
            print(len(data["bookings"]))

            # Add the current page's bookings to the list
            all_bookings.extend(data["bookings"])

            # Check if there are more pages to fetch
            if data["page"] < data["page_count"]:
                params["page"] += 1  # Move to the next page
            else:
                loop = False
        else:
            print(f"Error fetching data: {response.status_code}")
            break

    print(all_bookings)
    for reservation in all_bookings:
        print(reservation)
        try:

            if not Reservation.objects.filter(id=reservation["id"]).exists():
                Reservation(
                    id=reservation["id"],
                    reference_id=reservation["reference-id"],
                    type=reservation["type"],
                    arrival=reservation["arrival"][:10],
                    departure=reservation["departure"][:10],
                    created_at=reservation["created-at"][:10],
                    modified_at=reservation["modifiedAt"][:10],
                    property=reservation["apartment"]["id"],
                    channel=reservation["channel"]["id"],
                    guest_name=reservation["guest-name"],
                    email=reservation["email"],
                    phone=reservation["phone"],
                    adults=reservation["adults"],
                    children=reservation["children"],
                    check_in=reservation["check-in"],
                    check_out=reservation["check-out"],
                    notice=reservation["notice"],
                    price=reservation["price"],
                    price_paid=reservation["price-paid"],
                    prepayment=reservation["prepayment"],
                    prepayment_paid=reservation["prepayment-paid"],
                    deposit=reservation["deposit"],
                    deposit_paid=reservation["deposit-paid"],
                    language=reservation["language"],
                    guest_app_url=reservation["guest-app-url"],
                    is_blocked_booking=reservation["is-blocked-booking"],
                    guest_id=reservation["guestId"],
                ).save()
            else:
                Reservation.objects.filter(id=reservation["id"]).update(
                    reference_id=reservation["reference-id"],
                    type=reservation["type"],
                    arrival=reservation["arrival"][:10],
                    departure=reservation["departure"][:10],
                    created_at=reservation["created-at"][:10],
                    modified_at=reservation["modifiedAt"][:10],
                    property=reservation["apartment"]["id"],
                    channel=reservation["channel"]["id"],
                    guest_name=reservation["guest-name"],
                    email=reservation["email"],
                    phone=reservation["phone"],
                    adults=reservation["adults"],
                    children=reservation["children"],
                    check_in=reservation["check-in"],
                    check_out=reservation["check-out"],
                    notice=reservation["notice"],
                    price=reservation["price"],
                    price_paid=reservation["price-paid"],
                    prepayment=reservation["prepayment"],
                    prepayment_paid=reservation["prepayment-paid"],
                    deposit=reservation["deposit"],
                    deposit_paid=reservation["deposit-paid"],
                    language=reservation["language"],
                    guest_app_url=reservation["guest-app-url"],
                    is_blocked_booking=reservation["is-blocked-booking"],
                    guest_id=reservation["guestId"],
                )
        except Exception as e:
            print(e)

    return render(request, "management/apartments.html")


def contratto_locazione(request):
    prop = Property.objects.filter(id=1).first()
    context = {
        "name": prop.name,
        "street": prop.street,
        "zip": prop.zip,
        "city": prop.city,
        "country": prop.country,
    }
    return render(request, "management/contratto_locazione.html", context)


def generate_pdf_report_scheda(request, property_id):
    # Third party imports
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

    # Fetch the object by ID
    obj_property = get_object_or_404(Property, id=property_id)
    obj_cadastrial_data = get_object_or_404(CadastralData, property_id=property_id)

    # Create the HTTP response with PDF headers
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="report_{obj_property.id}.pdf"'

    # Create the PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph(f"Property Report: {obj_property.name}", styles["Title"])
    title_property = Paragraph(f"Dati Anagrafici", styles["Heading3"])
    title_cadastrial_data = Paragraph(f"Dati catastali", styles["Heading3"])

    # Table Data
    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.white),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )
    data_property = [
        ["Nome", "Valore"],  # Header Row
    ]
    for i in obj_property._meta.fields:
        data_property.append(
            [i.verbose_name.title(), getattr(obj_property, i.name) or "-"]
        )
    # Table Data
    data_cadastrial_data = [
        ["Nome", "Valore"],  # Header Row
    ]
    for i in obj_cadastrial_data._meta.fields:
        data_cadastrial_data.append(
            [i.verbose_name.title(), getattr(obj_cadastrial_data, i.name) or "-"]
        )

    # Create the Table
    table_property = Table(data_property, colWidths=[150, 350])
    table_cadastrial_data = Table(data_cadastrial_data, colWidths=[150, 350])

    table_property.setStyle(table_style)
    table_cadastrial_data.setStyle(table_style)

    # Build the PDF
    elements = [
        title,
        title_property,
        table_property,
        title_cadastrial_data,
        table_cadastrial_data,
    ]
    doc.build(elements)

    return response
