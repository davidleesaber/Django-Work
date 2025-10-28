from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# create a database object called ToDoList
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    # this class references ToDoList
    # cascade on deletion, delete same item in todolist if an item is delete here
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # the CharField function requires a max length defined
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text