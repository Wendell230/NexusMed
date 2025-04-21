from django.urls import path
from .views import (
    PacienteListView, PacienteCreateView,
    AtendimentoListView, AtendimentoCreateView,
    AgendaCalendarView, atendimento_create_ajax, atendimentos_json
)

urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/novo/', PacienteCreateView.as_view(), name='paciente_create'),

    path('atendimentos/', AtendimentoListView.as_view(), name='atendimento_list'),
    path('atendimentos/novo/', AtendimentoCreateView.as_view(), name='atendimento_create'),

    path('agenda/', AgendaCalendarView.as_view(), name='agenda_calendar'),
    path('api/atendimentos/', atendimentos_json, name='atendimentos_json'),
    path('api/atendimentos/criar/', atendimento_create_ajax, name='atendimento_create_ajax'),

]