from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Cliente
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = "Panel de Administración"

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("nombre","rut","telefono","direccion","modelo","cantidad","instagram","fecha_pedido","fecha_envio","estado")
    list_filter=('estado',)
    search_fields=('nombre','rut',)
    resource_class = ClienteResource


#admin.site.unregister(Group)



# class ClienteAdmin(ImportExportModelAdmin):
#     resource_class = ClienteResource


admin.site.register(Cliente,ClienteAdmin)
#admin.site.register(Cliente,ClienteAdmin)