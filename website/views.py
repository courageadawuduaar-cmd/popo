from django.shortcuts import render, redirect
from .models import Service, Testimonial, Booking, Gallery
from django.contrib import messages
from .models import BeforeAfter

from .models import Service, Testimonial, BeforeAfter, Gallery, Barber

def home(request):

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    transformations = BeforeAfter.objects.all()
    gallery = Gallery.objects.all().order_by("-created")[:10]
    barbers = Barber.objects.all()

    return render(request, "home.html", {
        "services": services,
        "testimonials": testimonials,
        "transformations": transformations,
        "gallery": gallery,
        "barbers": barbers
    })

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def contact(request):
    return render(request, "contact.html")


def booking(request):

    services = Service.objects.all()

    if request.method == "POST":

        Booking.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            service_id=request.POST["service"],
            date=request.POST["date"],
            time=request.POST["time"]
        )

        messages.success(request, "Your appointment was booked successfully!")

        return redirect("booking")

    return render(request, "booking.html", {"services": services})


def gallery(request):
    images = Gallery.objects.all().order_by("-created")
    return render(request, "gallery.html", {"images": images})