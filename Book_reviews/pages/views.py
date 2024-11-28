from django.shortcuts import render
import requests

# Create your views here.
def home_view(request):
    context = {}
    context['quotes'] = []
    context['authors'] = []

    # Get the response and handle it as a list of dictionaries
    res = requests.get("https://zenquotes.io/api/random")
    data = res.json()[0]  # Access the first item in the list

    # Extract quote and author from the dictionary
    q = data['q']
    a = data['a']
    context['quotes'].append(q)
    context['authors'].append(a)

    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html', {})

def contact_view(request):
    return render(request, 'contact.html', {})
