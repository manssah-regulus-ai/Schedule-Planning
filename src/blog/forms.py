from django import forms


class CollaboratorFilterForm(forms.Form):
    CHOICES = (
        ('', 'Tous'),
        ('La Rochelle', 'La Rochelle'),
        ('Angoulins', 'Angoulins'),
    )

    magasin = forms.ChoiceField(choices=CHOICES, required=False)