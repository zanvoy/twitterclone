from django.contrib import admin
from twitteruser.models import SomeUser 
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (                    
            'Following',
            {
                'fields': (
                    'following',
                ),
            },
        ),
    )




admin.site.register(SomeUser, CustomUserAdmin)