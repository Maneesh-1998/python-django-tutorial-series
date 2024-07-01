from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def print_hello(request):
    movie_data={'movie':[
        {
        'title':'Godfather',
        'year':'1990',
        'summary':'story of an underworld kin',
        'sucess':True
    },
    {
        'title':'Titanic',
        'year':'1997',
        'summary':'romance and adventure',
        'sucess':True
    },
    {
        'title':'v for vendetta',
        'year':'2005',
        'summary':'action and sci-fi',
        'sucess':True
    },
    {
        'title':'The Mask',
        'year':'1994',
        'summary':'comedy and crime',
        'sucess':True
    },
    {
        'title':'The mommy returns ',
        'year':'2001',
        'summary':'Adventure and Horror',
        'sucess':True
    },
    {
        'title':'superman ',
        'year':'2015',
        'sucess':True
    }    
    ]}
    return render(request,'hello.html',movie_data)