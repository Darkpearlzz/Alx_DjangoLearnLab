from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                      
            'Custom Fields',
            {
                'fields': (
                    'date_of_birth',
                    'profile_photo',
                ),
            },
        ),
    )
    
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom Fields',
            {
                'fields': (
                    'date_of_birth',
                    'profile_photo',
                ),
            },
        ),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'date_of_birth',
    )
   
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}), # Use email instead of username
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'password', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)