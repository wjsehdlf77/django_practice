from django.shortcuts import render, HttpResponse
from .models import Members, RendBook

# Create your views here.

def index(request):
    members_list = Members.objects.order_by('-create_date')
    context = {
        'members_list' : members_list
    }

    return render(request, 'pybo/members_list.html', context)