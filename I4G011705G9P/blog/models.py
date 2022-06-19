from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class Post(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
   created_date = models.DateTimeField()
   published_date = models.DateTimeField()

   def __str__(self)-> str:
    return self.title
   def __str__(self)-> str:
    return self.text
   def __str__(self)-> str:
    return self.author
   def __str__(self)-> str:
    return self.created_date
   def __str__(self)-> str:
    return self.published_date