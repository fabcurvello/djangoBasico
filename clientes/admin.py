from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento', 'email')


admin.site.register(Cliente, ClienteAdmin)






