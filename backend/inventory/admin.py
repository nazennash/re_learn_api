from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
# Register your models here.

# admin.site.register(Product)

admin.site.unregister(User)
admin.site.unregister(Group)


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # return request.user.is_superuser
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('inventory.change_product'):
            return True
        else:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        # return request.user.is_superuser
        return False
    
    def has_view_permission(self, request, obj=None):
        return True

@admin.register(Product)
class ProductAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    # list_display = ('web_id', 'slug', 'name', 'description', 'is_active', 'created_at', 'updated_at')
    list_display = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser

    #     if not is_superuser:
    #         form.base_fields['name'].disabled = True
    #         form.base_fields['description'].disabled = True

    #     # form.base_fields['web_id'].widget.attrs['readonly'] = True
    #     return form
    