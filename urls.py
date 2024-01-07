from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    # this is to view food items
   path ('',views.IndexClassview.as_view(),name='index'),
   # this is to view food item details

   path ('<int:pk>',views.FoodDetail.as_view(), name='detail'),
   path('item/',views.item,name='item'),  

   #add items by user 
   path('add',views.CreateItem.as_view(),name='create_item'), 

   #edit item
   path("update/<int:id>/",views.update_item,name="update_item"),


   #delete item 
   path("delete/<int:id>/",views.delete_item, name="delete_item"),
]
