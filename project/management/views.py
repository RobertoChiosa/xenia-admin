#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 5/12/2024
import os

from django.contrib.sites import requests
# Third party imports
from django.http import HttpResponse
from django.shortcuts import render

from models import Property


# Create your views here.


def index(request):
    return HttpResponse("Management resources")


def host_upload(request):
    return HttpResponse("Hello, world. Here you can update your data.")


def apartments(request):
    url = "https://login.smoobu.com/api/apartments"
    response = requests.get(
        url,
        headers={
            "Content-type": "application/json",
            "Api-Key": os.getenv("APIKEY"),
        },
    )
    print(response)
    data = response.json()
    for apt in data:
        print(apt)
        apartment_data = Property(
            name=apt["name"],
            smoobu_id=apt["id"],
        )
        apartment_data.save()

    return render(request, "smoobu/apartments.html")
