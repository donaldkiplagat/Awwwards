from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Categories,Technologies,Colors,Countries,Project,Profile
# from .forms import
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q

# Create your views here.
def index(request):

    return render(request,'index.html')
