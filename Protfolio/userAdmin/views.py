from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Projects, UsersContact


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'projects/index.html')

def view_projects(request : HttpRequest):

    view_projects = Projects.objects.all()

    context = {"view_projects" : view_projects}
    return render(request, "projects/view_projects.html", context)

def add_project(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_project = Projects(title= request.POST["title"],
                                content = request.POST["content"],
                                start_date = request.POST["start_date"],
                                end_date = request.POST["end_date"],
                                image = request.FILES["image"])
        new_project.save()
        return redirect("projects:view_projects_page")


    return render(request, "projects/add_project.html")

def update_project(request : HttpRequest, project_id):

    project = Projects.objects.get(id=project_id)
    project.start_date = Projects.start_date.isoformat #to make it compatible with input value in html
    project.end_date = Projects.end_date.isoformat
    if request.method == "POST":
        project.title = request.POST["title"]
        project.content = request.POST["content"]
        project.start_date = request.POST["start_date"]
        project.end_date = request.POST["end_date"]
        project.image = request.FILES["image"]

        project.save()
        return redirect("projects:view_projects_page")

    return render(request, "projects/update_projects.html", {"project" : project})



def delete_project(request : HttpRequest, project_id):
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect("projects:view_projects_page")


def view_contact(request : HttpRequest):

    view_contact = UsersContact.objects.all()

    context = {"view_contact" : view_contact}
    return render(request, "Projects/view_contact.html", context)

def project_detail(request : HttpRequest, project_id):

    project = Projects.objects.get(id=project_id)

    return render(request, "mian/project_detail.html", {"project" : project})