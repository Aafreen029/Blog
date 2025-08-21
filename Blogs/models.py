from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid
 

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title=models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    thumbnail=models.ImageField(upload_to="upload")
    slug = models.SlugField(unique=True, blank=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)  

    def save(self, *args, **kwargs): 
        if not self.slug:
            token=str(uuid.uuid4())
            current_slug=slugify(self.title)
            final_slug=f"{current_slug}-{token}"
            self.slug = final_slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


    

    

