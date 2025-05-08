from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Project, Rating

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        score = int(request.POST['score'])
        Rating.objects.create(project=project, score=score)
        return redirect('project_detail', pk=project.pk)

    ratings = project.rating_set.all()
    avg_score = ratings.aggregate(models.Avg('score'))['score__avg']
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'ratings': ratings,
        'avg_score': avg_score,
    })
