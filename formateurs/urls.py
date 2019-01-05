# urls for apps courses

from django.urls import path
# from courses.views import CoursesList
from formateurs.views import formateurs_view, formateurs_details


app_name = 'formateurs'

urlpatterns = [
    path('', formateurs_view, name='home'),
    path('<formateurs_id>', formateurs_details, name='details'),

]
