from django.shortcuts import render,HttpResponse
import requests

# Create your views here.

def index(request):
    context={}
    obj = requests.get("https://api.spacexdata.com/v3/launches?limit=100")
    data = obj.json()
    context["data"]=data
    if "launch_success" in request.GET:
        launch_success = request.GET["launch_success"]
        obj = ("https://api.spacexdata.com/v3/launches?limit=100&launch_success={}").format(launch_success)
        new_obj = requests.get(obj)
        data = new_obj.json()
        context["data"]=data

    if "launch_success" in request.GET:
        launch_success = request.GET["launch_success"]
        obj = ("https://api.spacexdata.com/v3/launches?limit=100&launch_success={}").format(launch_success)
        new_obj = requests.get(obj)
        data = new_obj.json()
        context["data"]=data

    if "land_success" in request.GET:
        land_success = request.GET["land_success"]
        obj = ("https://api.spaceXdata.com/v3/launches?limit=100&launch_success={}&land_success={}").format(land_success,land_success)
        new_obj = requests.get(obj)
        data = new_obj.json()
        context["data"]=data

    if "land_success" in request.GET:
        land_success = request.GET["land_success"]
        obj = ("https://api.spaceXdata.com/v3/launches?limit=100&launch_success=true&land_success={}").format(land_success)
        new_obj = requests.get(obj)
        data = new_obj.json()
        context["data"]=data
        
    if "year" in request.GET:
        year = request.GET["year"]
        obj = ("https://api.spaceXdata.com/v3/launches?limit=100&launch_success=true&land_success=true&launch_year={}").format(year)
        new_obj = requests.get(obj)
        data = new_obj.json()
        context["data"]=data
    return render(request,"index.html",context)
    

    

