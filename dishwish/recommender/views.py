from django.shortcuts import render
from recommender.models import Restaurant, Dish

def index(request):
    if request.method == "GET":
        return render(request, "index.html", {"data": None, "show_form": True})
    if request.method == "POST":
        search_kw = request.POST["search_kw"]
        # making a 'LIKE' like query 
        result = Dish.objects.filter(name__contains=search_kw)
        # print(result) 
        return render(request, "index.html", {"data": result, "show_form": False})


