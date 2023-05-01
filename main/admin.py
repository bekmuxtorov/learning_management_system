from django.contrib import admin
from .models import Department, Topic, Resource


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)
