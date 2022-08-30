from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('index/', views.index), #https://127.0.0.1:8000/index/가 왔을때 실행
    path('greeting/',views.greeting),
    path('dinner/',views.dinner),
    path('image/',views.image),
    path('template_language',views.template_language),
    path('throw',views.throw),
    path('catch/',views.catch),
    path('hello/<str:name>/<int:age>/',views.hello),
]
