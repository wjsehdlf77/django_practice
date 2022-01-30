from django.contrib import admin
from .models import Members
from .models import RendBook

class MembersAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Members, MembersAdmin)
admin.site.register(RendBook)

