from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [                                                                                                                                         
    path("", views.Docsdata, name="API-Documentation"),
    path("test-form/", views.TestData, name="Test-Form"),

    path('nin-info/', views.NINInfo.as_view()),
    path('nin-info/<int:id>/', views.NINInfo.as_view()),

    path('business-info/', views.BusinessInfo.as_view()),
    path('business-info/<int:id>/', views.BusinessInfo.as_view()),
    
    path('license-info/', views.DriversInfo.as_view()),
    path('license-info/<int:id>/', views.DriversInfo.as_view()),
]

if settings.DEBUG:                                                                                                                                          
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)