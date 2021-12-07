
from django.urls import path
from .import views
urlpatterns=[
    path('', views.demo, name='demo'),


    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_product',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

    # path('connection',views.connection,name='connection'),
]