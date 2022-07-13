from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Group)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'group',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name', )
