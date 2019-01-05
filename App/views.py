from django.shortcuts import render, get_object_or_404

from courses.models import Courses, Category_index

def index(request):
    # cours_list = Courses.objects.all()
    category_index_list = Category_index.objects.all()
    template_name = 'pages/index.html'
    context = {
        # 'cours_list': cours_list,
        'category_index_list': category_index_list
    }
    return render(request, template_name, context)

