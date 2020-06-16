from django.shortcuts import render
from pprint import pprint


def index(request):

    return render(request, 'pages/index.html')
