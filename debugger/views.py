from django.shortcuts import render
from django.views.generic import ListView

from .models import Debugger

# Create your views here.
class DebuggerList(ListView):
    model = Debugger
    template_name = 'debugger/debugger_list.html'

# def debug(request):
#     return render(request, 'debugger/debugger_list.html')
    