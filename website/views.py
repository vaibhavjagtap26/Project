from django.shortcuts import render,redirect
from website.models import enquiry_table
from django.contrib import messages
from website.models import booking_form

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 

def best_tours(request):
    return render(request,'best tours.html')       

def booking(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('destination')
        d = request.POST.get('date')
        book = booking_form(name = a,email = b,destination = c,date = d)
        book.save()
        messages.success(request, 'Booking Form Submitted Successfully...')
    return render(request,'Booking.html')

# def contact(request):
#     return render(request,'contact.html')


def flights(request):
    return render(request,'flights.html')  

def hotels(request):
    return render(request,'hotels.html')

def popular_destinations(request):
    return render(request,'popular destinations.html')



def contact(request):
    if request.method == "POST":
        a = request.POST.get('Name')
        b = request.POST.get('Email')
        c = request.POST.get('Telephone')
        d = request.POST.get('Subject')
        e = request.POST.get('Message')
        print(a,b,c,d,e)
        enquiry = enquiry_table(Name = a, Email = b, Telephone = c, Subject = d,Message = e)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
    # return redirect('contact')   
    return render(request, 'contact.html')



