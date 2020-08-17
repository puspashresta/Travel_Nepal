from django.conf import settings
from django.db import models
from django.urls import reverse

Labels=(('offer','offer'),('limited','limited'))
STATUS= (('active','active'),('','default'))


# Create your models here.
class Place(models.Model):
        title = models.CharField(max_length=250)
        price = models.IntegerField()
        discounted_price = models.IntegerField(default=0)
        image = models.ImageField(upload_to='media',blank=True)
        description = models.TextField(blank=True)
        slug = models.CharField(max_length=300, unique=True)
        labels = models.CharField(choices=Labels, max_length=100, blank=True)
        special_offer = models.BooleanField(default=False)

        def __str__(self):
            return self.title

        # def get_place_url(self):
        #     return reverse("home:place",kwargs={'slug' : self.slug})

        def add_to_book(self):
            return reverse('home:place',kwargs={'slug':self.slug})

        def add_to_checkout(self):
            return reverse('home:place', kwargs={'slug': self.slug})


class Slider(models.Model):
        title = models.CharField(max_length=200)
        rank = models.IntegerField()
        status = models.CharField(choices=STATUS, max_length=100, blank=True)
        upper_part = models.CharField(max_length=300)
        lower_part = models.CharField(max_length=200, blank=True)

        def __str__(self):
            return self.title

class Service(models.Model):
        image=models.TextField()
        title = models.CharField(max_length=200)
        upper_part = models.CharField(max_length=300)
        lower_part = models.CharField(max_length=200, blank=True)

        def __str__(self):
            return self.title

class Feedback(models.Model):
        description=models.TextField()
        image = models.CharField(max_length=200, blank=True)
        name = models.CharField(max_length=200)
        address = models.CharField(max_length=300)

        def __str__(self):
            return self.name

class Team(models.Model):
        image=models.ImageField(upload_to='media')
        name=models.CharField(max_length=100)
        contact=models.CharField(max_length=100)

        def __str__(self):
                return self.name

class Choose(models.Model):
        image=models.ImageField(upload_to='media')
        title=models.CharField(max_length=200)
        description=models.TextField()

        def __str__(self):
                return self.title

class History(models.Model):
        slug=models.CharField(max_length=50)
        title=models.CharField(max_length=200)
        description=models.TextField()

        def __str__(self):
                return self.title

class GetInTouch(models.Model):
        description = models.TextField()
        Telephone = models.CharField(max_length=100)
        mail = models.CharField(max_length=100)
        address = models.CharField(max_length=200)

        def __str__(self):
                return self.mail

class Message(models.Model):
        name = models.CharField(max_length=200)
        email = models.CharField(max_length=100)
        subject = models.CharField(max_length=200,blank=True)
        telephone = models.IntegerField()
        message = models.TextField()

        def __str__(self):
                return self.name


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.TextField()
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='media',blank=True)
    description = models.TextField(blank=True)
    quantity=models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    number_of_ticket = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete_book(self):
        return reverse("home:delete_book",kwargs={'slug' : self.slug})

class Checkout(models.Model):
    place=models.ImageField(upload_to='media',blank=True)
    slug=models.CharField(max_length=50,blank=True)
    quantity=models.IntegerField()
    placeName=models.CharField(max_length=100,blank=True)
    price=models.FloatField()
    # action=models.BooleanField(default=True)
    fullname=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=100)
    address_type = models.CharField(max_length=100, blank=True)
    checkout = models.BooleanField(default=True,blank=True)

    def __str__(self):
        return self.fullname
