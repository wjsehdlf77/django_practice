from django.urls import path

from pybo.views import index, detail

app_name = 'pybo'

urlpatterns = [
    path('', index, name = 'index'),
    path('<int:members_id>/', detail, name = 'detail'),
]