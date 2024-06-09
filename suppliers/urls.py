from django.urls import path
from suppliers.apps import SuppliersConfig
from suppliers.view.API_supplier import SupplierDetailAPIView, SupplierListAPIView, SupplierCreateAPIView, SupplierUpdateAPIView, \
    SupplierDeleteAPIView

app_name = SuppliersConfig.name

urlpatterns = [
    # API Supplier
    path('API/', SupplierListAPIView.as_view()),
    path('API/<int:pk>/', SupplierDetailAPIView.as_view()),
    path('API/create/', SupplierCreateAPIView.as_view()),
    path('API/update/<int:pk>/', SupplierUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', SupplierDeleteAPIView.as_view()),

]
