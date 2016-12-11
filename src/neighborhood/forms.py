from django import forms


from neighborhood.models import Neighborhood

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = []
