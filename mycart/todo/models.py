from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_id = models.AutoField
    todo_domain = models.CharField(max_length=50,default='',blank=True,null=True)
    todo_work = models.CharField(max_length=100)
    todo_deadline = models.DateField()
    todo_status = models.BooleanField()
    todo_comment = models.CharField(max_length=150,default='-')


    def __str__(self):
        return self.todo_work