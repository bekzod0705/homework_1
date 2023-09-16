from django.urls import path
from .views import getAll,Create,DetailDestroyUpdate,put,today,lastTen,status

urlpatterns=[
    path('getall/',getAll.as_view()),
    path('create/',Create.as_view()),
    path('<int:pk>/',DetailDestroyUpdate.as_view()),
    path('today/',today.as_view()),
    path('lastTen/',lastTen.as_view()),
    path('status/',status.as_view())
]