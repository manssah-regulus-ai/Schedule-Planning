from django import forms
from blog.models import Collaborator


class CollaboratorFilterForm(forms.Form):
    CHOICES = (
        ('', 'Tous'),
        ('La Rochelle', 'La Rochelle'),
        ('Angoulins', 'Angoulins'),
    )

    magasin = forms.ChoiceField(choices=CHOICES, required=False)


class JobFilterForm(forms.Form):
    job_choices = [("", "Tous")] + list(Collaborator.objects.values_list("job", "job").distinct())
    job = forms.ChoiceField(choices=job_choices, required=False, label="Filtrer par job")