from django.shortcuts import render, redirect
from .models import Person

people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
        return redirect('show_people')
    return render(request, 'add_person.html')

def show_people(request):
    return render(request, 'show_people.html', {'people': people})
