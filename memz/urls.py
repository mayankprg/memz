from django.urls import path


from . import views

urlpatterns = [
   path('', views.front, name="index"),
   path('sticker', views.upload_Image, name="sticker")
]
