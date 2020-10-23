from django.shortcuts import render

def HomeView(request, *args, **kwargs):
    return render(request, "Home.html", context={}, status=200)



""" 
deprecated views below this line
-----------
-----------
-----------
----------
"""
