from django.shortcuts import render


# Create your views here.


def home(request):
    context = {
        "current_year": 2024,  # Example context variable for the footer
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "title": "About Us",
    }
    return render(request, "about.html", context)


def property(request):
    return render(request, "property.html")


def checkin(request):
    return render(request, "checkin.html")


def explore(request):
    return render(request, "explore.html")
