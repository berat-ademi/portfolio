from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Projects

from .forms import UserRegistrationForm, ProjectForm

from django.contrib.auth.decorators import login_required
from .decorators import admin_only

@login_required(login_url='login')
@admin_only
def createProject(request):
    all_projects = Projects.objects.all()
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        'projects': all_projects,
        'projectform' : form,
    }
    return render(request, 'portfolioapp/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def updateProject(request, id):

    project = Projects.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context ={
        'projectform': form,
    }
    return render(request, 'portfolioapp/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def deleteProject(request, id):
    project = Projects.objects.get(id=id)
    if request.method == "POST":
        project.delete()
        return redirect('home')
        
    context={
        'project': project
    }
    return render (request, 'portfolioapp/delete.html', context)


def home(request):
    projects = Projects.objects.all()
    context = {

        'projects': projects,

    }
    return render(request, 'portfolioapp/home.html', context)


def register(request):
    if request.method =='POST':
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created successfully')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    

    context = {
        'form': form
    }
    return render(request, 'portfolioapp/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.add_message(request, messages.ERROR, "Invalid Credentials!")

		context = {}
		return render(request, 'portfolioapp/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')