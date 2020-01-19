from django.db import models

# Create your models here.
class Post(models.Model):
    images = models.ImageField(upload_to='waste_posts/img')
    waste_type = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)


class ngo_list(models.Model):
    link = models.URLField()
    desc = models.CharField(max_length=50)
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title
