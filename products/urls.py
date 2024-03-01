from django.urls import path
from . views import index,showproduct,addCategory # . same directory cha vane // different folder huda chai . lekhera folder ko naam raakhnu parcha


urlpatterns = [
    path('',index),
    path('show/',showproduct),
    path('addcategory/',addCategory),
]