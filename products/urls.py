from django.urls import path
from . views import * # . same directory cha vane // different folder huda chai . lekhera folder ko naam raakhnu parcha


urlpatterns = [
    path('',index),
    path('show/',showproduct),
    path('addcategory/',addCategory),
    path('addproduct/',postProduct),
    path('allcategory/',showcategory),
    path('deletecategory/<int:category_id>',deletecategory),
    path('updatecategory/<int:category_id>',updatecategory),
]