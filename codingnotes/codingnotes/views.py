from django.shortcuts import render
#from django.http import HttpResponseRedirect, HttpResponse
#from django.contrib.auth.models import User
#from django.shortcuts import get_object_or_404, render, redirect
## from .models import related models
# from .restapis import related methods
#from django.contrib.auth import login, logout, authenticate
#from django.contrib import messages
#from datetime import datetime
import logging
#import json


# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "codingnotes/index.html",)
