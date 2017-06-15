from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from django.shortcuts import render
import re
# Create your views here.
def main(request):
    html = urlopen("http://pchelomarket.com/15-inventar")
    bsobj = bs(html)

    dict = {}
    for link in bsobj.find("div",{"id":"center_column"}).findAll("a", {'product-name'}):
        if 'href' in link.attrs:
            dict[link.attrs['href']] = link.contents[0]

    return render(request, 'crowler/index.html', {'dict':dict})