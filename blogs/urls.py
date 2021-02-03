from django.urls import path
from django.urls.conf import include

from blogs.views import *

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<int:blog_id>/', blogDetails, name='blogDetails'),
] 

