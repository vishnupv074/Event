from django.shortcuts import render
from .models import profiles
from django.core.mail import EmailMessage



# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})


def register_view(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        college = request.POST.get('college')
        course = request.POST.get('course')
        messege = request.POST.get('messege')

        profile = profiles()

        profile.name = name
        profile.email = email
        profile.mobile = mobile
        profile.college = college
        profile.course = course
        profile.messege = messege
        profile.save()

        email = EmailMessage('Invitation for one day workshop',
                             'We are happy to invite you to the one day workshop on python and django programing to be held in our office on 10th August 2019. Timing schedule will be 10am to 2.30pm. '
                             '\nLooking forward to meet you', to=[profile.email])
        email.send()
        msg = "Registration form sent Successfully."
    return render(request, 'register.html', {'msg': msg})
