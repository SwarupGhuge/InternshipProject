# from django.shortcuts import render,redirect
# from .models import HRMmodel
# from .forms import HRMForm

# Create your views here.
# def Sample(request):
#     if request.method == 'POST':
#         emp = HRMForm(request.POST)
#         if emp.is_valid():
#             emp.save()
#             return redirect('showform')
#     else:
#         emp = HRMForm()    
#         return render(request,'Department_Management_System.html',{'form':emp})



# HRMapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HRMForm  # replace with your form
from .models import HRMmodel

def Sample(request):
    # Always start with a form
    # form = HRMForm()

    if request.method == 'POST':
        form = HRMForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('showform')  # MUST RETURN!
        # If invalid, fall through → render form with errors
    else:
        form = HRMForm()  # GET request

    # This runs for GET and invalid POST
    return render(request, 'Department_Management_system.html', {'form': form})

def ShowForm(request):
    data = HRMmodel.objects.all()
    return render(request,'Dashboard_Creation.html',{'range':data})

def FormEdit(request,id):
    data = HRMmodel.objects.get(id = id)
    return render(request,'Dashboard_Edit.html',{'range' :data})

def FormsUpdate(request,id):
    obj = HRMmodel.objects.get(id = id)
    data = HRMForm(request.POST,instance=obj)

    if data.is_valid():
        data.save()
        return redirect('showform')
    else:
        return render(request,'Dashboard_Edit.html')
    
def FormsDelete(request,id):
    data = HRMmodel.objects.get(id=id)
    data.delete()
    return redirect('showform')    