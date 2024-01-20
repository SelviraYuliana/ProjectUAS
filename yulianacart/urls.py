from django.urls import path
from . import views

urlpatterns = [
    path('', views.yulianacart_detail, name='yulianacart_detail'),
    path('add/<product_id>', views.yulianacart_add, name='yulianacart_add'),
    path('remove/<product_id>', views.yulianacart_remove, name='yulianacart_remove'),
    

]