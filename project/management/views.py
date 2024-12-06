#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024
import os

import requests
from django.contrib.admin.views.decorators import staff_member_required

# Third party imports
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from fpdf import FPDF
from reportlab.pdfgen import canvas

from .models import Property, CadastralData


# Create your views here.


def index(request):
    return HttpResponse("Management resources")


def host_upload(request):
    return HttpResponse("Hello, world. Here you can update your data.")


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
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

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
