from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse

from hospi_mgmt.forms import OccupantForm
from hospi_mgmt.models import Availability, Occupant


# Create your views here.

def index(request):
    return render(request, "index.html")


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def gato_view(request):
    q = (
        Availability.objects
        .filter(dedicated="GAT")
        .select_related("occupant")
    )
    return render(request, "cat.html", {"availability": q})


@login_required
def perro_view(request):
    q = (
        Availability.objects
        .filter(dedicated="PER")
        .select_related("occupant")
    )
    return render(request, "dog.html", {"availability": q})


class OccupantCreate(CreateView):
    model = Occupant
    form_class = OccupantForm
    template_name = "create.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["space"] = self.kwargs["pk"]
        return initial


    def get_success_url(self):
        if self.object.space.dedicated == "GAT":
            return reverse("gato")
        return reverse("perro")


class OccupantUpdate(UpdateView):
    model = Occupant
    form_class = OccupantForm
    template_name = 'update.html'

    def get_success_url(self):
        if self.object.space.dedicated == "GAT":
            return reverse("gato")
        return reverse("perro")


class OccupantDetail(DetailView):
    pass


class OccupantDelete(DeleteView):
    model = Occupant
    template_name = 'delete.html'

    def get_success_url(self):
        if self.object.space.dedicated == "GAT":
            return reverse("gato")
        return reverse("perro")
