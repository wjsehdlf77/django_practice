from django.urls import path

from pybo.views import index, detail, rendbook_add

app_name = 'pybo'

urlpatterns = [
    path('', index, name = 'index'),
    path('<int:members_id>/', detail, name = 'detail'),
    path('rendbook/add/<int:members_id>/', rendbook_add,
            name = 'rendbook_add')
]