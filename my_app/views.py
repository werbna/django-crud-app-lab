from django.shortcuts import render # type: ignore

class Recipe:
    def __init__(self, day, name, description):
        self.day = day
        self.name = name
        self.description = description
        
recipes = [
    Recipe('Monday', 'Chicken Alfredo', 'A delicious pasta dish with chicken and alfredo sauce.'),
    Recipe('Tuesday', 'Spaghetti and Meatballs', 'A classic Italian dish with spaghetti noodles and meatballs.'),
    Recipe('Wednesday', 'Tacos', 'A Mexican dish with seasoned beef and tortillas.'),
    Recipe('Thursday', 'Chicken Parmesan', 'An Italian dish with breaded chicken and marinara sauce.'),
    Recipe('Friday', 'Fish and Chips', 'A British dish with fried fish and french fries.')
]   

# Create your views here.
def home(req):
    return render(req, 'home.html')
def about(req):
    return render(req, 'about.html')
def recipe(req):
    return render(req, 'recipes/recipe.html', {'recipe': recipes})