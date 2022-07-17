from django.urls import path
from .views import ProductGenericView, ProductGenericCreateView, ProductListView,ProductCreateListView,ProductUpdateView

urlpatterns = [
    path('<int:pk>/',ProductGenericView.as_view()),
    path('',ProductGenericCreateView.as_view()),
    path('list',ProductCreateListView.as_view()),
    path('<int:pk>/',ProductUpdateView.as_view())
]
