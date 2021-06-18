from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_single/', blog_single, name='blog_single'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact_us', contact_us, name='contact_us'),
    path('login/', login, name='login'),
    path('product_detail/<str:slug>/', product_detail, name='product_detail'),
    path('shop/', shop, name='shop'),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('add-recipe/', add_recipe, name='add-recipe'),
    path('update_recipe/<int:pk>/', update_recipe, name='update-recipe'),
    path('delete-recipe/<int:pk>/',  DeleteRecipeView.as_view(), name='delete-recipe')
]
