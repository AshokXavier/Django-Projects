from django.shortcuts import render,redirect,get_object_or_404
from .forms import Pet_shop_form
from .models import Pet
# Create your views here.

def register(request):
  if request.method=='POST':
    form=Pet_shop_form(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      # return redirect('list')
      return redirect('pet_details')
  else:
    form=Pet_shop_form()
  return render(request,'register.html',{'form':form})

def pet_details(request):
  pets=Pet.objects.all()
  return render(request,'details.html',{'details':pets})

def delete(request,id):
  if request.method=='POST':
    pet=get_object_or_404(Pet,id=id)
    pet.delete()
  return redirect('pet_details')

def update(request,id):
  pet=get_object_or_404(Pet,id=id)
  if request.method=='POST':
    form=Pet_shop_form(request.POST,request.FILES,instance=pet)
    if form.is_valid():
      form.save()
      return redirect('pet_details')

  else:
    form=Pet_shop_form(instance=pet)
  return render(request,'update.html',{'form':form,'pet':pet})

