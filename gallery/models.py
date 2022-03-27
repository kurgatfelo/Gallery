from django.db import models
import datetime as dt

# from cloudinary.models import CloudinaryField

#Location class model
class Location(models.Model):
    """
    Location class for creating our location instances
    """
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        location = Location.objects.all()
        return location

    class Meta:
        ordering = ['location_name']

#Category class model
class Category(models.Model):
    """
    Category class for creating our categories instances
    """
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete() 

#Image class model
class Image(models.Model):
    """
    Image class for creating our image instances
    """
    image = models.ImageField(upload_to = 'images/',default='')
   
    image_name =models.CharField(max_length=100)
    image_details =models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location ,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,category):
        image = cls.objects.filter(category__category_name__icontains = category)
        return image

    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id=id).update(image=image)

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

    @classmethod
    def get_images_by_location(cls,location_name):
        location = cls.objects.filter(location__location_name = location_name).all()
        return location

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image
