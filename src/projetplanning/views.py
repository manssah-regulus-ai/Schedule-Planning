# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from blog.models import Collaborator


def index(request):
    date = datetime.today()
    collaborator = Collaborator.objects.all()
    return render(request, "blog/index.html", context={"date": date,
                                                                    "collaborator": collaborator})
