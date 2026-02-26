from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Certificate, Skill, Training
from .forms import ProjectForm, CertificateForm, SkillForm, TrainingForm

def home(request):
    projects = Project.objects.order_by('-created_date')[:3]  # Show recent 3 projects
    return render(request, 'home.html', {'projects': projects})

def about(request):
    skills = Skill.objects.filter(category='skill')
    tools = Skill.objects.filter(category='tool')
    trainings = Training.objects.all()
    return render(request, 'about.html', {
        'skills': skills,
        'tools': tools,
        'trainings': trainings
    })

def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'projects/project_list.html', {'projects': projects})

def certificate_list(request):
    certificates = Certificate.objects.order_by('-date_issued')
    return render(request, 'certificates/certificate_list.html', {'certificates': certificates})

def certificate_detail(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    return render(request, 'certificates/certificate_detail.html', {'certificate': certificate})

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

@user_passes_test(lambda u: u.is_staff)
def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'certificates/certificate_create.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = SkillForm()
    return render(request, 'projects/skill_create.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def training_create(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = TrainingForm()
    return render(request, 'projects/training_create.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def skill_delete(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == 'POST':
        skill.delete()
    return redirect('about')

@user_passes_test(lambda u: u.is_staff)
def training_delete(request, id):
    training = get_object_or_404(Training, id=id)
    if request.method == 'POST':
        training.delete()
    return redirect('about')
