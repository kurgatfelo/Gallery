from gallery.models import Location,Image,Category
from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404


# Create your views here.
def homepage(request):
    """
    View function to render homepage
    """
    images = Image.objects.all()
    location=Location.get_locations()

    return render(request, 'all-gallery/gallery.html', {"images":images,"location":location})

def search_category(request):
    
    location=Location.get_locations()

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'all-gallery/search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'all-gallery/search.html')

def get_image_location(request,location_name):
    location=Location.get_locations()
    image= Image.get_images_by_location(location_name)
    message = f"{location_name}"
    return render(request, 'all-gallery/image-location.html',{"message":message,"image": image,"location":location})

def image_properties(request,image_id):
    location=Location.get_locations()

    image = Image.get_image_by_id(image_id)
    return render(request, {"image" : image,"location":location})
