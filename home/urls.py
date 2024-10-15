from django.urls import  path
from .views import homepage, order, success

urlpatterns = [
    path('', homepage, name='homepage'),
    path('order>', order, name='order'),
    path('success', success, name='success' )
]
