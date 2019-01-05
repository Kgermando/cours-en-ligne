# urls for apps courses

from django.urls import path
# from courses.views import CoursesList
from courses.views import coursesView, details


app_name = 'courses'

urlpatterns = [
    path('', coursesView, name='home'),
    path('<id>', details, name='details'),

]
