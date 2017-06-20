from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from django.shortcuts import render
import re
from .models import urls
  
# Create your views here.

def get_image_url (kwargs):
	return kwargs


def main(request):
    html = urlopen("http://pchelomarket.com/15-inventar?id_category=15&n=57")
    bsobj = bs(html, "html.parser")

    dict = {}
    lists = []

    for link in bsobj.find("div",{"id":"center_column"}).findAll("a", {'product-name'}):
        if 'href' in link.attrs:
            dict[link.attrs['href']] = link.contents[0]

            a = get_image_url(urlopen(link.attrs['href']))
           
    return HttpResponse(a)