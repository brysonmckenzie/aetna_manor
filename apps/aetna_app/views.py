from django.shortcuts import render, redirect, HttpResponse

def index(request):
    
    return render(request, 'aetna_apps/index.html')

def accomplishments(request):
    
    return render(request, 'aetna_apps/accomplishments.html')

def documents(request):
    
    return render(request, 'aetna_apps/documents.html')

def events(request):
    
    return render(request, 'aetna_apps/events.html')

def gallery(request):
    
    return render(request, 'aetna_apps/gallery.html')

def members(request):
    
    return render(request, 'aetna_apps/members.html')

def remix(request):
    
    return render(request, 'aetna_apps/remix.html')

def volunteers(request):
    
    return render(request, 'aetna_apps/volunteers.html')

def registration(request):
    
    return render(request, 'aetna_apps/member_signup.html')
def remix(request):
    
    return render(request, 'aetna_apps/remix.html')

def documents(request):
    
    return render(request, 'aetna_apps/documents.html')

def about(request):

    return render(request, 'aetna_apps/about.html')