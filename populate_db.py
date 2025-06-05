import os
import django 
from faker import Faker
import random
from task.models import Employee,Project,Task, Task_Details


# SetUp Dejango Environment 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','new_task.settings')
django.setup()


# Function to Populate to The Database

def populate_db():
    #initialize Faker

    fake = Faker()

    #Create Project

    projects= [Project.objects.create(
        name = fake.bs().capitalize(),
        description = fake.paragraph(),
        start_date = fake.date_this_year()
    )for _ in range(5)]

    print(f"Created {len(projects)} Projects.")

    #Create some Employee
    employees = [Employee.objects.create(
        name = fake.name(),
        email = fake.email()
    )for _ in range(10)]

    print(f"Created {len(employees)} Employee.")

    # Create Some Task 

    tasks = []

    for _ in range(20):
        task = Task.objects.create(
           project = random.choice(projects),
           title = fake.sentence(),
           description = fake.paragraph(),
           due_date = fake.date_this_year(),
           status = random.choice(['PENDING','IN_PROGRESS','COMPLETED']),
           is_completed = random.choice([True,False])
        )
        task.assigned_to.set(random.sample(employees,random.randint(1,3)))
        tasks.append(task)

    print(f"Created {len(tasks)} Task.")


    #Created Task Details 

    for task in tasks:
        Task_Details.objects.create(
            task = task,
            assigned_to = ", ".join(
                [emp.name for emp in task.assigned_to.all()]),
            priority = random.choice(['H','M','L']),
            notes = fake.paragraph()   

        )

    print("Populated taskdetails for all Task")
    print("DataBase Populated SuccessFully  ")








