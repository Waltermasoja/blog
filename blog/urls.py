from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,PostDeleteView

urlpatterns = [
       path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
       path('post/<int:pk>/gadzirisa/',BlogUpdateView.as_view(),name='post_edit'),
       path('',BlogListView.as_view(),name='home'),
       path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
       path('post/newer/',BlogCreateView.as_view(),name='post_new'),
    
]