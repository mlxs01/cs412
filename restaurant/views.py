"""
View functions for the restaurant application.
Handles rendering templates and processing form submissions for the restaurant ordering system.
Includes functionality for displaying menus, processing orders, and generating order confirmations.
"""

from django.shortcuts import redirect, render
from django.conf import settings
import random
import time

# All daily specials
daily_specials = [
    "Spicy Chicken Sandwich with Caesar Dressing",
    "Tuna Salad with Cucumber Dressing",
    "Grilled Vegetable Sandwich with Balsamic Glaze",
    "Chef's Special Pizza with Fresh Mozzarella"
]

# Images for main page
img_list = [
    f'{settings.MEDIA_URL}chicken_sandwich.jpeg',
    f'{settings.MEDIA_URL}tuna_salad.jpg',
    f'{settings.MEDIA_URL}vegetable_sandwich.jpg'
]

confirm = f"{settings.MEDIA_URL}check.jpg"

# Menu items with prices
MENU_PRICES = {
    'Classic Burger': 12.99,
    'Garden Salad': 9.99,
    'Margherita Pizza': 14.99,
    'Daily Special': 16.99, # All daily specials have the same price
    'Extra Cheese': 1.00,
    'Bacon': 2.00
}

def debug_context(request):
    return {
        'STATIC_URL': settings.STATIC_URL,
        'STATIC_ROOT': settings.STATIC_ROOT,
        'STATICFILES_DIRS': settings.STATICFILES_DIRS,
        'HOST': request.get_host()
    }

# Logic for main page
def main(request):
    """
    Render the main page of the restaurant website.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered main page template with a randomly selected featured image.
    """

    context = {
        'img': random.choice(img_list),
        'debug': debug_context(request),
    }
    return render(request, 'restaurant/main.html', context)

# Logic for order page
def order(request):
    """
    Render the order page with menu items and a form for placing orders.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered order page template with daily special and featured image.
    """

    context = {
        'daily_special': random.choice(daily_specials),
        'img': random.choice(img_list)
    }
    return render(request, 'restaurant/order.html', context)

# Logic for confirmation page
def confirmation(request):
    """
    Process order submissions and display order confirmation.
    
    Handles POST requests from the order form, calculates total price,
    generates pickup time, and displays order details.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered confirmation page with order details if POST request,
                     otherwise redirects to order page.
    """

    if request.method == 'POST':
        # Get ordered items
        items = request.POST.getlist('items')
        extras = request.POST.getlist('extras')
        
        # Calculate total
        total = 0
        for item in items:
            # For some reason, 'Daily Special' isn't part of a name
            if "Tuna Salad" in item or "Spicy Chicken" in item or "Grilled Vegetable" in item or "Chef's Special" in item:
                total += MENU_PRICES['Daily Special']  # Use the Daily Special price for these items
            else:
                total += MENU_PRICES.get(item, 0)
        
        for extra in extras:
            total += MENU_PRICES.get(extra, 0)
        
        # Calculate pickup time (random between 30-60 minutes from now)
        current_time = time.time()
        pickup_minutes = random.randint(30, 60)
        pickup_time = current_time + (pickup_minutes * 60)
        formatted_pickup_time = time.strftime("%I:%M %p", time.localtime(pickup_time))

        context = {
            'img': confirm,
            'items': items,
            'extras': extras,
            'total': f"{total:.2f}",
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'email': request.POST.get('email'),
            'instructions': request.POST.get('instructions'),
            'readytime': formatted_pickup_time
        }
        
        return render(request, 'restaurant/confirmation.html', context)
    
    # Redirect to order page if not POST (hopefully this doesn't happen)
    return redirect('order')