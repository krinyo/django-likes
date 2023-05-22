from django.shortcuts import render, get_object_or_404
from .models import Location, Rating
from django.http import HttpResponseRedirect
from django.urls import reverse

def location_rating(request, location_name):
    location = get_object_or_404(Location, location_name=location_name)
    ratings = Rating.objects.filter(location=location)

    context = {
        'location': location,
        'ratings': ratings,
    }
    return render(request, 'ratings/location_rating.html', context)

def add_rating(request, location_name):
    location = get_object_or_404(Location, location_name=location_name)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'like':
            Rating.objects.create(location=location, like=True, dislike=False)
        elif action == 'dislike':
            Rating.objects.create(location=location, like=False, dislike=True)

        return HttpResponseRedirect(reverse('ratings:location_rating', args=[location_name]))

    context = {
        'location': location
    }
    return render(request, 'ratings/location_rating.html', context)