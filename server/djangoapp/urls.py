from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='about/', view=views.about, name='about'),

    # path for contact us view
    path(route='contact/', view=views.contact, name='contact'),

    path(route='registration/', view=views.registration, name='register'),
    # path for login
    path(route='login/', view=views.login, name='login'),
    # path for logout
    path(route='logout/', view=views.logout, name='logout'),
    
    path(route='home/', view=views.home, name='index'),

    # path for dealer reviews view
    
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
