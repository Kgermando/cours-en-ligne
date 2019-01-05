from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Debugger

# Create your views here.

def debug_list(request):
    debugger_list = Debugger.objects.all()
    template_name = 'debugger/debugger_list.html'
    context = {
        'debugger_list': debugger_list
    }
    return render(request, template_name, context )

def debug_detail(request, debug_id):
    debugger = get_object_or_404(Debugger, id=debug_id)
    template_name = 'debugger/debugger_details.html'
    context = {
        'debugger': debugger
    }
    return render(request, template_name, context)
