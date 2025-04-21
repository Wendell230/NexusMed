# agenda/views.py

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Paciente, Atendimento
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


class PacienteListView(ListView):
    model = Paciente
    template_name = 'agenda/paciente_list.html'
    context_object_name = 'pacientes'


class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'email', 'telefone', 'estado_civil']
    template_name = 'agenda/paciente_form.html'
    success_url = reverse_lazy('paciente_list')


class AtendimentoListView(ListView):
    model = Atendimento
    template_name = 'agenda/atendimento_list.html'
    context_object_name = 'atendimentos'


class AtendimentoCreateView(CreateView):
    model = Atendimento
    fields = ['paciente', 'titulo', 'data_inicio', 'data_fim', 'observacoes']
    template_name = 'agenda/atendimento_form.html'
    success_url = reverse_lazy('atendimento_list')

    def get_initial(self):
        data = self.request.GET.get('data')
        return {'data_inicio': data} if data else super().get_initial()

            

class AgendaCalendarView(TemplateView):
    template_name = 'agenda/agenda_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context



def atendimentos_json(request):
    atendimentos = Atendimento.objects.all()
    eventos = []

    for a in atendimentos:
        eventos.append({
            "id": a.id,
            "title": a.titulo,
            "start": a.data_inicio.isoformat(),
            "end": a.data_fim.isoformat(),
        })

    return JsonResponse(eventos, safe=False)


@csrf_exempt
@require_POST
def atendimento_create_ajax(request):
    try:
        paciente_id = request.POST.get('paciente')
        titulo = request.POST.get('titulo')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        observacoes = request.POST.get('observacoes', '')

        Atendimento.objects.create(
            paciente_id=paciente_id,
            titulo=titulo,
            data_inicio=data_inicio,
            data_fim=data_fim,
            observacoes=observacoes
        )
        return JsonResponse({'sucesso': True})
    except Exception as e:
        return JsonResponse({'sucesso': False, 'erro': str(e)})