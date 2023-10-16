from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime

from blog.forms import CollaboratorFilterForm, JobFilterForm
from blog.models import Collaborator


# Create your views here.
def index(request):
    date = datetime.today()
    return render(request, "blog/index.html", context={"date": date})
def article(request):
    form = CollaboratorFilterForm(request.GET)
    magasin_filter = request.GET.get('magasin')
    collaborators = Collaborator.objects.all()

    if magasin_filter:
        if magasin_filter != '':
            collaborators = collaborators.filter(Q(magasin=magasin_filter) | Q(magasin__contains=magasin_filter))

    job_filter_form = JobFilterForm(request.GET)
    job_filter = request.GET.get("job")
    if job_filter and job_filter != "Tous":
        collaborators = collaborators.filter(job=job_filter)

    return render(request, f'blog/page.html', context={"collaborator": collaborators, 'form': form,
                                                       'job_filter_form': job_filter_form,})


def collab_detail(request, slug):
    collaborateur = get_object_or_404(Collaborator, slug=slug)
    return render(request, f'blog/detail.html', context={"collaborator": collaborateur,})
