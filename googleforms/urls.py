from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page,name='login'),
    path('',home,name='home'),
    path('add-form/',add_form,name='add_form'),
    path('add-form/<str:id>/',add_form_id,name='add_form_id'),
    path('add-image-fields/<str:id>/',add_image_fields,name='add_image_fields'),
    path('google-form/<str:id>/',share_form,name='share_form'),
    path('see-all-details/<str:id>/',see_all_details,name='see_all_details'),
    path('log-out/',logout_user,name='logout_user')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

