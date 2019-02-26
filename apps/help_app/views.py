from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def index(request):
    if 'user_first' not in request.session:
        return redirect("/")
    # request.session['user_id']
    # jobs= this_user.my_job.all()
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        "all_jobs": Job.objects.all(),
        "my_jobs": this_user.my_job.all()
       
    }
    return render(request, 'help_app/dashboard.html', context)

def log_out(request):
    request.session.flush()
    return redirect("/")

def add_job(request):
    return render(request, 'help_app/add.html')

def add(request):
    errors = Job.objects.add_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect ("/add_job")
    else:
        this_user = User.objects.get(id=request.session['user_id'])
        Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], user = this_user)
       

        return redirect('/add_job')

def view_job(request, num):
    context = {
        "job": Job.objects.get(id=num)
    }
    return render(request, 'help_app/view_job.html', context)

def delete(request, num):
    job_to_delete = Job.objects.get(id=num)	
    job_to_delete.delete()
    
    return redirect("/handy_help")

def update(request, num):
    errors = Job.objects.add_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect ("/edit_job/"+num)
    else:
        job_to_update = Job.objects.get(id=num)
        job_to_update.title = request.POST['title']
        job_to_update.description = request.POST['description']
        job_to_update.location = request.POST['location']
        job_to_update.save()

    return redirect("/edit_job/"+num)   

def edit_job(request, num):
    context = {
        "job": Job.objects.get(id=num)
    }
    return render(request, "help_app/edit.html", context)

def add_to_my_job(request, num):
    this_user = User.objects.get(id=request.session['user_id'])
    job=Job.objects.get(id=num)

    job.my_job.add(this_user)
    my_assign=this_user.my_job.all()
    print(my_assign)
 

    # context = {
    #     "my_j": my_assign
    # }
    return redirect("/handy_help")