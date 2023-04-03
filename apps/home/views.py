from django.shortcuts import render
from apps.appointment.models import Doctor
from apps.news.models import News


def home(request):
    news = News.objects.order_by('-published_date')[:3]
    doctor = Doctor.objects.all()[:3]
    context = {'news': news, 'doctor': doctor}
    return render(request, 'home/home.html', context)
