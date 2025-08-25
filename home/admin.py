from django.contrib import admin

# Register your models here.
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")   # columns in admin list view
    search_fields = ("name", "email")               # search bar
    list_filter = ("created_at",) 