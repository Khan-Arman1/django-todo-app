from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=50,blank=False, null=False)
    todo_text = models.TextField(max_length=500)
    time_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # remind_time = models.DateTimeField(blank=True, null=False)
    remind_date = models.DateField(blank=True,null=False)
    remind_time = models.TimeField(blank=True, null=False)

    def __str__(self):
            return f"{self.user.username}"

    class Meta:
          ordering = ['remind_time']

# class UserTodo(models.Model):
#     todo_text = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="todos")
      
#     def __str__(self):
#          return f"{self.user.username} - {self.todo_text[:10]}"