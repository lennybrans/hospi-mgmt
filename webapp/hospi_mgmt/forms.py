from django import forms

from hospi_mgmt.models import Occupant


class OccupantForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = "__all__"
