from django.test import TestCase
from .models import Category, Location, Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Wildlife')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Masai Mara')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locat = Location.objects.all()
        self.assertTrue(len(locat) > 0) 

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)

class ImageTestClass(TestCase):
    
    def setUp(self):

        self.location = Location(location_name='Masai Mara')
        self.location.save_location()

        self.category = Category(category_name='Wildlife')
        self.category.save_category()

        self.mara= Image(id=1,image_name = 'Elephants', image_details ='Testing images class model',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.mara,Image))
    
    def test_save_image(self):
        self.mara.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_image(self):
        self.mara.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)

    def test_update_image(self):
        self.mara.save_image()
        self.mara.update_image(self.mara.id, 'images/img.jpg')
        new_img = Image.objects.filter(image='media/images/img1.jpg')
        self.assertFalse(len(new_img) > 0)

    def test_get_image_by_id(self):
        self.mara.save_image()
        img = self.mara.get_image_by_id(self.mara.id)
        images = Image.objects.filter(id=self.mara.id)
        self.assertTrue(img, images) 

    def test_search_by_category(self):
        category = 'Wildlife'
        found_img = self.mara.search_by_category(category)
        self.assertFalse(len(found_img) > 1)  

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
