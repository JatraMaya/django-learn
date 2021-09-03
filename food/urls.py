from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='Index'),
    path('item/', views.FoodDetail.as_view(), name='Item'),
    path('item/<int:id>/', views.detail, name="Detail"),
    path('item/add', views.create_item, name="Add_item"),
    path('item/edit/<int:id>', views.edit_item, name="Edit_item"),
    path('item/delete/<int:id>', views.delete_item, name="Delete_item")
]
