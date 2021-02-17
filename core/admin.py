from django.contrib import admin
from . import models


class PhysicianAdmin(admin.ModelAdmin):
    fields_display = ('name_given', 'name_family', 'title', 'clinic',)
    list_display = ('name_given', 'name_family', 'title', 'clinic',)
    search_fields = ('name_given', 'name_family', 'title', 'clinic',)


class UserAdmin(admin.ModelAdmin):
    field_display = ('email', 'id', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',)
    list_display = ('email', 'id', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        # changed.
        if obj.pk:
            orig_obj = models.UserProfile.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(models.Physician, PhysicianAdmin)
admin.site.register(models.User, UserAdmin)
