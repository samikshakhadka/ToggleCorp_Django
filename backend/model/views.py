from django.shortcuts import render
from django.http import HttpResponse
from .models import GeeksModel  # Make sure to import the model correctly

def index(request):
    # inserting manualy
    data_1 = GeeksModel(title="CDC", description="COMPILER DESIGNING", img="images/fifi1.jpg")
    data_2 = GeeksModel(title="SE", description="book about software engineering", img="images/fifi1.jpg")
    data_1.save()
    data_2.save()

    # using bulk_create() method to insert data in bulk
    GeeksModel.objects.bulk_create(
    [GeeksModel(title="TOC", description="a book on TOC", img="images/fifi1.jpg"),
     GeeksModel(title="DAA", description="a booK ON DAA", img="images/fifi1.jpg"),
     GeeksModel(title="DL", description="a booK ON DL", img="images/fifi1.jpg"),
     ]
    )
    
    return HttpResponse("Dummy data added to the model")

def create_geeksmodel(request):
    GeeksModel.objects.create(title= "API", description = "A book on API", img = "images/fifi1.png")
    return HttpResponse(f"GeeksModel API created successfully!")

def read_geeksmodel(request):
    all_data = GeeksModel.objects.all()

    read_data = "All the data in database are:"
    for data in all_data:
        read_data += f"Title = { data.title},Description = {data.description},img = {data.img}"
        
    return HttpResponse(read_data)

def edit_geekmodel(request):
    edit_data = GeeksModel.objects.first()
    edit_data.title = "updated "
    edit_data.description = "updated description"
    edit_data.img = "images/fifi1.png"

    edit_data.save()

    return HttpResponse(edit_data)

def delete_geekmodel(request):
    del_data = GeeksModel.objects.first()
    data_del = del_data.delete()
    return HttpResponse(data_del)