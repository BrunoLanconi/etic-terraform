from django.contrib import admin

from .models.users import User


class Users(admin.ModelAdmin):  # Admin console model configuration
    # Choosing what fields will be displayed on admin
    list_display = ("username", "created")
    # Choosing what fields will be displayed as links on admin
    list_display_links = ("username",)


admin.site.register(User, Users)  # Registering model on admin console
