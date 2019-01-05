from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Courses

# Create your views here.

def coursesView(request):
    category_list = Category.objects.all()
    courses_list = Courses.objects.all()
    template_name = 'courses/courses.html'
    context = {
        'category_list': category_list,
        'courses_list': courses_list
    }
    return render(request, template_name, context)


# class CoursesList(ListView):
#     template_name = 'courses/courses.html'
#     model = Category
#     paginate_by = 18

#     # def get_queryset(self, *wargs, **kwargs):
#     #     context = super(Category).object.all().get_queryset(self, *wargs, **kwargs)
#     #     return context

class CoursesDetails(DetailView):
    pass

def details(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'courses/details.html', {'category': category})
