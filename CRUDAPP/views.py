from django.shortcuts import render, redirect
from models import Crud

def index(request):
	names = Crud.objects.all()
	context = {'names':names}
	return render(request,'CRUDAPP/index.html', context)

def create(request):
	print request.POST
	name = Crud(fname=request.POST['fname'],lname=request.POST['lname'])
	name.save()
	return redirect('/')

def edit(request, id):
	name = Crud.objects.get(id=id)
	context = {"name":name}
	return render(request,'CRUDAPP/edit.html', context)

def update(request, id):
	name = Crud.objects.get(id=id)
	name.fname = request.POST['fname']
	name.lname = request.POST['lname']
	name.save()
	return redirect('/')

def destroy(request, id):
	name = Crud.objects.get(id=id)
	name.delete()
	return redirect('/')


