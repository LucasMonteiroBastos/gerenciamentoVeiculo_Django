from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Veiculo, Marca, Contact
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'gestoes/gestoes.html', {'veiculos': veiculos})

# request > urls > view > models  > response

class HomeView(ListView):
    template_name = 'gestoes/gestoes.html'
    model = Veiculo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # adicionar variáveis para a template (onde é acessivel por {{ VARIAVEL }}
        context['veiculos'] = self.model.objects.all()
        return context


class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact

class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'

class ContactUpdate(UpdateView):
    model = Contact
    fields = '__all__'

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')