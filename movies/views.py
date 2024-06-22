from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    "movies": ["gladiator", "the notebook", "save the last dance", "six days, seven nights"],
    "title": "Favourite movies of all time"
  }

  return render(request, "movies/index.html", context)

def about(request):
  return render(request, "movies/about.html", {})
