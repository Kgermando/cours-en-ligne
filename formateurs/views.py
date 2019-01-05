from django.shortcuts import render, get_object_or_404

from formateurs.models import Formateurs
# Create your views here.

def formateurs_view(request):
    formateurs_list = Formateurs.objects.all()
    template_name = 'formateurs/formateurs.html'
    context = {
        'formateurs_list': formateurs_list
    }
    return render(request, template_name, context )


def formateurs_details(request, formateurs_id):
    formateurs = get_object_or_404(Formateurs, id=formateurs_id)
    template_name = 'formateurs/formateurs_details.html'
    return render(request, template_name, {'formateurs': formateurs})
