from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BeforeAfter(models.Model):

    title = models.CharField(max_length=100)

    before_image = models.ImageField(upload_to="before_after/")
    after_image = models.ImageField(upload_to="before_after/")

    def __str__(self):
        return self.title

class Barber(models.Model):

    name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    photo = models.ImageField(upload_to="barbers/")

    def __str__(self):
        return self.name