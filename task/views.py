from django.shortcuts import render,redirect
from django.http import HttpResponse
from task.forms import TaskForm,TaskModelForm,TaskDetailModelForm
from task.models import Employee,Task
from django.db.models import Q,Count,Max,Min,Avg
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):
    # task = Task.objects.select_related('details').prefetch_related('assigned_to').all()

    counts = Task.objects.aggregate(
        total=Count('id'),
        completed = Count('id', filter= Q(status='COMPLETED')),
        in_progress = Count('id',filter=Q(status='IN_PROGRESS')),
        pending = Count('id',filter=Q(status='PENDING')),
    )
    # total_task = task.count()
    # pending_task = Task.objects.filter(status="PENDING").count()
    # completed_task = Task.objects.filter(status="COMPLETED").count()
    # in_progress = Task.objects.filter(status="IN_PROGRESS").count()

    type = request.GET.get('type','all')
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type =='Completed':
        task = base_query.filter(status='COMPLETED')
    elif type =='in_progress':
        task = base_query.filter(status='IN_PROGRESS')
    elif type =='Pending':
        task = base_query.filter(status='PENDING')
    elif type =='all':
        task = base_query.all()


    context = {
        "task":task,
        "counts":counts,
        
    }
    return render(request,"dashboard/manager_dashboard.html",context)


def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()


    if request.method=="POST":
        # For Django Model Form Data
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid() :

            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            
            messages.success(request,"Task created Successfully !!")
            return redirect("create_task")
        
        #For Django form Data

        #     data = form.cleaned_data
        #     title = data.get("title")
        #     description = data.get("description")
        #     due_date = data.get("due_date")
        #     assigned_to = data.get("assigned_to")
        #     task = Task.objects.create(title=title,description=description,due_date=due_date)

        #     for emp_id in assigned_to:
        #         employee = Employee.objects.get(id=emp_id)
        #         task.assigned_to.add(employee)
            
            

    context = {
        "task_form":task_form,
        "task_detail_form":task_detail_form
    }
    return render(request,"task_form.html",context)




def update_task(request,id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    
    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)


    if request.method=="POST":
        # For Django Model Form Data
        task_form = TaskModelForm(request.POST,instance=task)
        task_detail_form = TaskDetailModelForm(request.POST,instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid() :

            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            
            messages.success(request,"Task Updated Successfully !!")
            return redirect("update_task",id)
        
        #For Django form Data

        #     data = form.cleaned_data
        #     title = data.get("title")
        #     description = data.get("description")
        #     due_date = data.get("due_date")
        #     assigned_to = data.get("assigned_to")
        #     task = Task.objects.create(title=title,description=description,due_date=due_date)

        #     for emp_id in assigned_to:
        #         employee = Employee.objects.get(id=emp_id)
        #         task.assigned_to.add(employee)
            
            

    context = {
        "task_form":task_form,
        "task_detail_form":task_detail_form
    }
    return render(request,"task_form.html",context)

def delete_task(request,id):
    if request.method=="POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request,"Task Deleted Successfully !!")
        return redirect("manager_dashboard")
    else:
        messages.error(request,"Something went Wrong !!")
        return redirect("manager_dashboard")


def view_task(request):
    # Retrive data using Get 
    # task = Task.objects.all()
    # spec_task =Task.objects.get(id=1)

    # Select Related  using 2 way (Foreign Key and One To One Field )
    task = Task.objects.filter(status = "PENDING")

    return render(request,"show_task.html",{"task":task})


