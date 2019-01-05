# urls for apps debugger
from django.urls import path
from debugger.views import DebuggerList
# from . import views

app_name = 'debugger'

urlpatterns = [
    path('', DebuggerList.as_view(), name='home'),
    # path('', views.debug, name='home')
]
