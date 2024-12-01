#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Management resources")


def host_upload(request):
    return HttpResponse("Hello, world. Here you can update your data.")
