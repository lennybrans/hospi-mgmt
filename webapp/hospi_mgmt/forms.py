from django import forms

from hospi_mgmt.models import Occupant

INPUT_CLASSES = (
    "bg-slate-50 border border-slate-300 text-slate-900 sm:text-sm "
    "rounded-lg focus:ring-teal-500 focus:border-teal-500 block w-full p-3 "
    "disabled:cursor-not-allowed disabled:bg-slate-100 disabled:text-slate-500"
)


class OccupantForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = "__all__"
        widgets = {
            "space": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "weight": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "motive": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "correa": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "transportin": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "attention": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["space"].disabled = True
