from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import requests
import json

#Spoonacular API Data ---------------------------------------------------
APIKey     = "b0bbda75fd6c415982ca2cd885d0deb8"
Params     = {'apiKey':'b0bbda75fd6c415982ca2cd885d0deb8', 'number':'1'}
RecipesURL = "https://api.spoonacular.com/recipes/random"

def Home(request):
    return render(request, 'index.html')

def RandomRecipe(request):
    RandomRecipe    = requests.get(RecipesURL, params=Params)
    if RandomRecipe.status_code == 200:
        RecipeDataBytes = RandomRecipe.content
        RecipeDataJson  = json.loads(RecipeDataBytes)
        RecipeUrl       = RecipeDataJson['recipes'][0]['sourceUrl']

        return redirect(RecipeUrl, status=200)
    else:
        return render(request, 'index.html')
