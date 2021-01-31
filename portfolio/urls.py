from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from jobs.views import *
from blogs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('blogs/', include('blogs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

