from django.urls import path
from .views import getAllCreate,DetailDestroyUpdate,put,today,lastTen,status

urlpatterns=[
    path('getallcreate/',getAllCreate.as_view()),
    path('<int:pk>/',DetailDestroyUpdate.as_view()),
    path('today/',today.as_view()),
    path('lastTen/',lastTen.as_view()),
    path('status/',status.as_view())
]