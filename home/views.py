from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import View

from .models import *
# Create your views here.

class BaseView(View):
    template_views={}

class HomeView(BaseView):
    def get(self,request):
        self.template_views['places']=Place.objects.all()
        self.template_views['sliders'] = Slider.objects.all()
        self.template_views['special_offers']=Place.objects.filter(special_offer=True)
        self.template_views['services'] = Service.objects.all()
        self.template_views['feedbacks'] = Feedback.objects.all()

        return render(request,'index.html',self.template_views)

class AboutView(BaseView):
    def get(self,request):
        self.template_views['teams']=Team.objects.all()
        self.template_views['chooses']=Choose.objects.all()
        self.template_views['historys']=History.objects.all()

        return render(request,'about.html',self.template_views)

class GalleryView(BaseView):
    def get(self,request):
        self.template_views['gallery']=Place.objects.all()

        return render(request,'gallery.html',self.template_views)

# def placeView(request,slug):
#         view={}
#         view['view_place']=Place.objects.filter(slug = slug)
#         return render(request,"quickview.html",view)
#
# class ContactView(BaseView):
#     def get(self,request):
#         self.template_views['getAccess'] = GetInTouch.objects.all()
#         self.template_views['messages'] = Message.objects.all()
#
#         return render(request, 'contact.html')

def contact(request):
    views = {}
    views['accesses'] = GetInTouch.objects.all()

    if request.method == "POST":
        name = request.POST['name'],

        email = request.POST['email'],
        subject = request.POST['subject'],
        telephone = request.POST['telephone']
        message = request.POST['message']

        message= Message.objects.create(
            name = name,
            email = email,
            subject = subject,
            telephone = telephone,
            message = message
            )
        message.save()
        email = EmailMessage(
            'New Message',
            # f"<html><body><b> {name} </b> is sending you message that <b> {message} </b></body></html>",
            '{name} is sendind you hello {message}',
            email,
            ['puspa0sh@gmail.com']
        )
        email.content_subtype = 'html'
        email.send()

        messages.success(request, "Successfully sent messages!")
        return redirect('home:contact')

    return render(request,'contact.html',views)



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, "This username already exist!")
                return redirect('home:signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request,"Try another email..")
                return redirect('home:signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
                messages.success(request, "you are signed in with us!!")
                return redirect('/accounts/login')
        else:
            messages.error(request,"password not matched")
            return redirect('/signup')
    return render(request,"signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Password not matches!!")
            return redirect('home:login')
    return render(request,"login.html")

def logout(request):
        auth.logout(request)
        return redirect('/')

def book(request):
    views={}
    views['tickets']=Book.objects.filter(checkout = False, user = request.user)

    return render(request, "bookticket.html",views)

def add_to_book(request):
    if request.method == "POST":
        slug = request.POST['slug']
        title = request.POST['title']
        image = request.POST['image']
        description = request.POST['description']
        price = request.POST['price']

        if Book.objects.filter(slug=slug).exists():
            quantity = Book.objects.get(slug=slug).quantity
            Book.objects.filter(slug=slug).update(quantity=quantity + 1)

            return redirect('home:book')
        else:
            my_book = Book.objects.create(
                user=request.user,
                slug=slug,
                title=title,
                image=image,
                description=description,
                price=price
            )
        my_book.save()
        return redirect('home:book')
    else:
        return redirect('/')

def delete_book(request,slug):
    if Book.objects.filter(slug=slug).exists():
        quantity = Book.objects.get(slug=slug).quantity
        Book.objects.filter(slug=slug).delete()
        messages.success(request,"The ticket is deleted")

        return redirect('home:book')
    else:

        return redirect('home:book')
        messages.error(request, "Ticket is not exist in your Book")



def checkout(request):
    check={}
    check['checkouts'] = Checkout.objects.all()

    return render(request, "checkout.html", check)

def add_to_checkout(request):
    if request.method == "POST":
        slug = request.POST['slug']
        fullname = request.POST['fullname']
        name = request.POST['placeName']
        image=request.POST['place']
        quantity = request.POST['quantity']
        price = request.PoST['price']
        if Checkout.objects.filter(slug=slug).exists():
            quantity = Checkout.objects.get(slug=slug).quantity
            Checkout.objects.filter(slug=slug).update(quantity=quantity + 1)

            return redirect('home:checkout')
        else:
            my_checkout = Checkout.objects.create(
                slug=slug,
                fullname=fullname,
                name=name,
                image=image,
                quantity=quantity,
                price=price

            )
            my_checkout.save()
            return redirect('home:checkout')

    return render(request,"checkout.html")

def calculate_price(request,slug):
    if Book.objects.filter(slug=slug).exists():
        quantity = Book.objects.get(slug=slug).quantity
        price = Book.objects.get(slug = slug).price
        total_cost=quantity*price

        return redirect('home:book')
    else:

        return redirect('home:book')
        messages.error(request, "Ticket is not exist in your Book")



def payment(request):

    return render(request,"payment.html")

def success(request):
    return render(request, "success.html")