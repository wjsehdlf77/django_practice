
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Members, RendBook
from django.utils import timezone


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

def rendbook_add(request, members_id):

    members = get_object_or_404(Members, pk = members_id)
    members.rendbook_set.create(book_name = request.POST.get('book_name'),
                                money = request.POST.get('money'),
                                create_date = timezone.now())
                                

    return redirect('pybo:detail', members_id = members.id)