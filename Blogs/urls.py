
from django.urls import path
from Blogs import views

urlpatterns = [
    path('',views.HomeView,name='Blogs'),
    path('add_post/',views.add_post,name='add_post'),
    path('blog/<str:title>/',views.blog_post,name='blog_post'),
    path('edit_post/<int:Post_id>/',views.edit_post,name='edit_post'),
    path('delete_post/<int:Post_id>/',views.delete_post,name='delete_post'),
 
    
]