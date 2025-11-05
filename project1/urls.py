from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),


    path('product/add/', views.add_product, name='add_product'),
    path('order/add/', views.add_order, name='add_order'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('orderdetails/add/', views.add_orderdetails, name='add_orderdetails'),


    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('orderdetails/', views.orderdetails_list, name='orderdetails_list'),


    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('order/delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('employee/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('orderdetails/delete/<int:pk>/', views.delete_orderdetails, name='delete_orderdetails'),

    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('order/update/<int:pk>/', views.update_order, name='update_order'),
    path('orderdetails/update/<int:pk>/', views.update_orderdetails, name='update_orderdetails'),
    path('employee/update/<int:pk>/', views.update_employee, name='update_employee'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)