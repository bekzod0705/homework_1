from django.contrib import admin
from .models import todoModel
from .forms import TodoForm
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    form=TodoForm
    list_display=('todo_name','user')
    search_fields=('todo_name',)

admin.site.register(todoModel,TodoAdmin)