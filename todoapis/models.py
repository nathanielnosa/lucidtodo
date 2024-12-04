from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# class Todo(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     complete = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now=)
#     update = models.DateTimeField(auto_now_add=)
    
#     def __str__(self):
#         return self.title