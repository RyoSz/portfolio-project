from django.shortcuts import render
from .models import Job
import requests
import json

def home(request):
    jobs = Job.objects
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content.decode('utf-8'))
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,BCH,DASH,ETC,XRP&tsyms=USD")
    price = json.loads(price_request.content.decode('utf-8'))
    return render(request, 'jobs/home.html', {'jobs':jobs, 'api':api, 'price':price})


