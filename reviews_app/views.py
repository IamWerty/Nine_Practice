from django.shortcuts import render
from .models import Review

def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_app/index.html', {'reviews': reviews})
