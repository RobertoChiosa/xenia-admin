#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 5/12/2024

from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()

# Create your views here.


def index(request):
    return render(request, "smoobu/index.html")
