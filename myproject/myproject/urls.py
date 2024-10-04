from myproject.views import*
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('',loginpage,name='loginpage'),
    path('signup_view/',signup_view,name='signup_view'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('addskill/',addskillpage,name='addskillpage'),
    path('addeducation/',addeducation,name='addeducation'),
    path('addinterest/',addinterest,name='addinterest'),
    path('addlanguage/',addlanguage,name='addlanguage'),
    path('createresume/',createresume,name='createjob'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
