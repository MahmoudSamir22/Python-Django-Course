from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": 'Practice mindfulness meditation for 10 minutes daily!',
    "february": 'Drink at least 2 liters of water every day!',
    "march": 'Write a short journal entry every day!',
    "april": 'Do a random act of kindness each day!',
    "may": 'Go tech-free for 1 hour every evening!',
    "june": 'Stretch for 15 minutes every morning!',
    "july": 'Try a new healthy recipe each week!',
    "august": 'Read at least 10 pages of a book daily!',
    "september": 'Wake up 30 minutes earlier and use it productively!',
    "october": 'Take a photo of something beautiful every day!',
    "november": 'No added sugar for the entire month!',
    "december": 'Reflect and write down 3 things you’re grateful for daily!',
}

# My Method
# def index(request):
#     links = "<ul>"
#     for key in monthly_challenges:
#         location = reverse("month-challenge", args=[key])
#         links = links + f'<li><a href="localhost:8000{location}" target="_blank">{key}</a><br></li>' # Problem i did here was to add localhost:8000
#     links = links + "</ul>"
#     return HttpResponse(links)

#Other Method
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    forward_month = months[month - 1]
    redirect_url = reverse('month-challenge', args=[forward_month])
    return  HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        return render(request ,"challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except: 
        return HttpResponseNotFound("This month is not supported!")
    
