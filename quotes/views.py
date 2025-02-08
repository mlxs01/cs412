from django.shortcuts import render
from django.conf import settings
import random

# Sample quotes and images
quotes_list = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "And if they hate what I make and they spit in my face okay I'll show 'em what tough is",
    "ehh heh heh ehh heh heh SNRK ehh heh heh ehh heh heh SNRK"
]

""" Not HTML so used same syntax as urls.py """
images_list = [
    f"{settings.MEDIA_URL}FDR.jpeg",
    f"{settings.MEDIA_URL}connerPrice.jpg",
    f"{settings.MEDIA_URL}numi.png",
]

# View for the main page (random quote and image)
def quote(request):
    context = {
        'quote': random.choice(quotes_list),
        'image': random.choice(images_list),
    }

    template = 'quotes/quote.html'

    return render(request, template, context)

# View for showing all quotes
def show_all(request):

    template = 'quotes/show_all.html'

    return render(request, template, {'quotes': quotes_list, 'images': images_list})

# View for the about page
def about(request):

    template = 'quotes/about.html'

    return render(request, template)
