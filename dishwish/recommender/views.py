from django.shortcuts import render
from recommender.models import Restaurant, Dishes

def index(request):
    if request.method == "GET":
        return render(request, "recommender/templates/index.html", data=None)
    if request.method == "POST":
        search_kw = request.POST["search_kw"]
        # making a 'LIKE' like query 
        result = Dishes.get(name_contains=search_kw)
        return render(request, "recommender/templates/index.html", data=result)


