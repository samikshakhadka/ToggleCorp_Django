from django.shortcuts import render
from django.http import HttpResponse
from .models import GeeksModel  # Make sure to import the model correctly

def index(request):
    
    data_1 = GeeksModel(title="CDC", description="COMPILER DESIGNING", img="images/fifi1.jpg")
    data_2 = GeeksModel(title="SE", description="book about software engineering", img="images/fifi1.jpg")
    data_1.save()
    data_2.save()
    
    return HttpResponse("Dummy data added to the model")
