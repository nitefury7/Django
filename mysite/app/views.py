from django.shortcuts import render
from django.http import HttpResponse 
from .models import ToDoList, Item
# Create your views here.
def index(response, id):
    tdl = ToDoList.objects.get(id=id)
    item = tdl.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><h2>%s</h2>" %(tdl.name, str(item.text)))   

def home(response):
    return HttpResponse("home page")