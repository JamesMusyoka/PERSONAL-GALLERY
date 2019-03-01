from django.shortcuts import render
from django.http  import HttpResponse,Http404


def welcome(request):
       # images=Image.objects.all()
       return render(request, 'welcome.html')


def gallery(request):
    return render(request, 'templates/gallery.html')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):
    raise Http404()  
    return render(request, 'templates/search_results.html')
