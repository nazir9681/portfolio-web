from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from blogs.models import Blogs

# Create your views here.
def blogs(request):
    blogsData = Blogs.objects.all()
    return render(request, 'blogs/blogs.html',{'blogsData': blogsData})

def blogDetails(request, blog_id):
    blog_detail = get_object_or_404(Blogs, pk=blog_id)
    return render(request,'blogs/blogDetails.html',{'blog_detail':blog_detail})