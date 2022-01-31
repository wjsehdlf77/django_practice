from multiprocessing import context
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Members, RendBook

# Create your views here.

def index(request):
    members_list = Members.objects.order_by('-create_date')
    context = {
        'members_list' : members_list
    }

    return render(request, 'pybo/members_list.html', context)

def detail(request, members_id):
    members = get_object_or_404(Members, pk = members_id)
    context = {
        'members' : members
    }

    return render(request, 'pybo/members_detail.html', context)