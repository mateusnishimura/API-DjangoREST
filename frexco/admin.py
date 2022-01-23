from django.contrib import admin
from frexco.models import Fruit, Region

class Fruits(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    search_fields = ('name', 'region')
    list_per_page = 10

admin.site.register(Fruit, Fruits)

class Regions(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
 
admin.site.register(Region, Regions)