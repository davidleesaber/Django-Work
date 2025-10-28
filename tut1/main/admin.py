from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.

# do this so we can actually see the list on the django admin site
admin.site.register(ToDoList)
admin.site.register(Item)