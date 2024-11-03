from django.shortcuts import render,redirect
from .models import Employee1, Depot1, Bus, Route11
from django.contrib.auth import login 
from .forms import UserRegisterForm,EmployeeForm

def home(request):
    print("Rendering Home")
    return render(request, 'bus_app/home.html')

def employee_list(request):
    print("Rendering Employee List")
    employees = Employee1.objects.all()
    return render(request, 'bus_app/employee_list.html', {'employees': employees})

def depot_list(request):
    print("Rendering Depot List")
    depots = Depot1.objects.all()
    return render(request, 'bus_app/depot_list.html', {'depots': depots})

def bus_list(request):
    print("Rendering Bus List")
    buses = Bus.objects.all()
    return render(request, 'bus_app/bus_list.html', {'buses': buses})

def route_list(request):
    print("Rendering Route List")
    routes = Route11.objects.all()
    return render(request, 'bus_app/route_list.html', {'routes': routes})

def contact(request):
    print("Rendering Contact")
    return render(request, 'bus_app/contact.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'bus_app/register.html', {'form': form})


def add_employee(request): 
            if request.method == 'POST': 
                form = EmployeeForm(request.POST) 
                if form.is_valid(): 
                    form.save() 
                    return redirect('employee_list') 
                else: form = EmployeeForm() 
                return render(request, 'bus_app/add_employee.html', {'form':form})