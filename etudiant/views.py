from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Etudiant
from .form import EtudiantForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class StudentCreateView(CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = "Création de l'étudiant"
        context['panel_name'] = 'Etudiant'
        context['panel_title'] = 'Créer etudiant'
        return context


class StudentUpdateView(UpdateView):
    model = Etudiant
    template_name_suffix = '_form'
    form_class = EtudiantForm
    success_url = reverse_lazy('etudiant:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Update Student Info'
        context['panel_name'] = 'Etudiant'
        context['panel_title'] = " Modifier l'etudiant "
        return context

class StudentListView(ListView):
    model = Etudiant
    template_name = '_list'
    #queryset = Etudiant.objects.all()
    field_list = [
        'nom', 'prenom', 'sexe', 'date_naissance'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Gérer les étudiants'
        context['panel_name'] = 'Etudiants'
        context['panel_title'] = 'Etudiant Info'
        context['field_list'] = self.field_list
        return context


class StudentDeleteView(DeleteView):
    model = Etudiant
    template_name = 'etudiant/student_delete.html'
    success_url = reverse_lazy('etudiant:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = "Confirmation de la suppression de l'etudiant  "
        context['panel_name'] = 'Etudiant'
        context['panel_title'] = 'Supprimer Etudiant'
        return context
