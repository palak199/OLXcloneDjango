from django.shortcuts import render

def home(request):
    template='olxclone/home.html'
    return render(request,template)