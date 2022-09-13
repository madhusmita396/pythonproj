from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

# from django_resized import ResizedImageField



from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from resizeimage import resizeimage


# Create your models here.
class QuoteTable(models.Model):
    quote=models.TextField(max_length=300,null=False,blank=False)
    qauthor=models.CharField(max_length=150,null=True,blank=True)
    type_choice=[('Motivational','Motivational'),('Success','success'),('Friendship','Friendship'),('Inspirational','Inspirational'),('Positive','Positive'),('Life','Life'),('Wisdom','Wisdom'),('Faith','Faith'),('Freedom','Freedom')]
    qtype=models.CharField(max_length=20,choices=type_choice,default='Motivational',)
    qimage=models.ImageField(upload_to="uploaded")
   
    tags=TaggableManager()




    def save(self,*args,**kwargs):
        img=Image.open(self.qimage)
        new_img=resizeimage.resize_cover(img,[300,300])
        new_img_io=BytesIO()
        new_img.save(new_img_io,new_img.format)
        temp_name=self.qimage.name
        self.qimage.delete(save=False)

        self.qimage.save(temp_name,content=ContentFile(new_img_io.getvalue()),save=False)
        
        super(QuoteTable,self).save(*args,**kwargs)



   
    def __str__(self):
        return self.qauthor
        
    def get_absolute_url(self):
        return reverse("list", kwargs={"pk": self.pk})
        