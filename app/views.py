from django.shortcuts import render
def home(request):
# Create your views here.
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')