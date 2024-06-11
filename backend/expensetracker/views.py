from django.http import HttpResponse

def dashboard(request):

    return HttpResponse("Dashboard")

def add_expense(request):

    return HttpResponse("Add Expense")
