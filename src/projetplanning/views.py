# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from blog.models import Collaborator

import plotly.express as px
import plotly.offline as opy

from projetplanning.figure import index_fig_ca_evol


def index(request):
    date = datetime.today()
    collaborator = Collaborator.objects.all()

    # Créez un graphique Plotly
    fig_LR = index_fig_ca_evol()
    fig_ANG = index_fig_ca_evol()
    # Générez l'HTML du graphique Plotly
    plot_div_LR = opy.plot(fig_LR, auto_open=False, output_type='div')
    plot_div_ANG = opy.plot(fig_ANG, auto_open=False, output_type='div')

    return render(request, "blog/index.html", context={"date": date,
                                                       "collaborator": collaborator,
                                                       'plot_div_LR': plot_div_LR,
                                                       'plot_div_ANG': plot_div_ANG})
