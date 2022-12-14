from django.urls import path
from .views import CoffeeListView, CoffeeDetailView,PostListView,PostDetailView

urlpatterns = [
   path('', CoffeeListView.as_view(), name='coffee_list'),
   path('<int:pk>', CoffeeDetailView.as_view(),name='coffee_detail'),
   path('post/', PostListView.as_view(), name='post_list'),
   path('post/<int:pk>', PostDetailView.as_view(),name='post_detail')
]
