from django.db import models

is_published=((0,"NO"),(1,"YES"))

class posts(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length = 255)
    slug = models.SlugField(max_length=200, unique=True)
    created_date= models.DateTimeField(auto_now_add=True)
    modify_date= models.DateTimeField(auto_now= True)
    description=models.TextField()
    is_published=models.IntegerField(choices=is_published, default=0)
    author=models.CharField(max_length = 50)
    intro =models.CharField(max_length = 225)
    image=models.ImageField(upload_to='images/')
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length = 255)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name