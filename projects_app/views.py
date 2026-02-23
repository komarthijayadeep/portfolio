from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project
from .forms import ProjectForm

def home(request):
    projects = Project.objects.order_by('-created_date')[:3]  # Show recent 3 projects
    return render(request, 'home.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

@user_passes_test(lambda u: u.is_staff)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_create.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})
