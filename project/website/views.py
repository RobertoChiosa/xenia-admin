#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import AvailabilityForm

# Create your views here.


def home_view(request):
    """
    This function renders the home page
    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AvailabilityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect("explore", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AvailabilityForm(request.GET)

    return render(request, "website/home.html", {"form": form})


def property_view(request):
    """
    This function renders the property page
    :param request:
    :return:
    """
    context = {
        "location": {
            "street": "Wönnichstr. 68/70",
            "zip": "10317",
            "city": "Berlin",
            "country": "Germany",
            "latitude": "52.5200080000000",
            "longitude": "13.4049540000000",
        },
        "timeZone": "Europe/Berlin",
        "rooms": {
            "maxOccupancy": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "doubleBeds": 1,
            "singleBeds": 3,
            "sofaBeds": None,
            "couches": None,
            "childBeds": None,
            "queenSizeBeds": None,
            "kingSizeBeds": 1,
        },
        "equipments": ["Internet", "Whirlpool", "Pool", "Heating"],
        "currency": "EUR",
        "price": {"minimal": "10.00", "maximal": "100.00"},
        "type": {"id": 2, "name": "Holiday rental"},
    }
    return render(request, "website/property.html", context)


def explore_view(request):
    """
    This function renders the explore page
    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AvailabilityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect("website/explore.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AvailabilityForm()

    return render(request, "website/explore.html", {"form": form})


def checkin_view(request):
    """
    This function renders the checkin form
    :param request:
    :return:
    """
    return render(request, "website/checkin.html")


def about_view(request):
    """
    This function renders the about page
    :param request:
    :return:
    """
    return render(request, "website/about.html")


def privacy_view(request):
    """
    This function renders the privacy policy page
    :param request:
    :return:
    """
    return render(request, "website/privacy.html")
