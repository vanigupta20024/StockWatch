from django.shortcuts import render, HttpResponse, redirect

def about(request):
    return render(request, "landing_page/about.html")
