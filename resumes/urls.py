from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name= "home"),
    path('profiles', views.CandidateListView.as_view(), name= "profiles"),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

