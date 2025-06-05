from django.shortcuts import render
from django.http import HttpResponse
from task.forms import TaskForm,TaskModelForm
from task.models import Employee,Task
from django.db.models import Q,Count,Max,Min,Avg

# Create your views here.

def manager_dashboard(request):
    task = Task.objects.select_related('details').prefetch_related('assigned_to').all()

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

    context = {
        "task":task,
        "counts":counts,
        
    }
    return render(request,"dashboard/manager_dashboard.html",context)


def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm()

    if request.method=="POST":
        # For Django Model Form Data
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"task_form.html",{"form":form,"message":"Task Added Successfully "})
        
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
        "form":form
    }
    return render(request,"task_form.html",context)


def view_task(request):
    # Retrive data using Get 
    # task = Task.objects.all()
    # spec_task =Task.objects.get(id=1)

    # Select Related  using 2 way (Foreign Key and One To One Field )
    task = Task.objects.filter(status = "PENDING")

    return render(request,"show_task.html",{"task":task})


