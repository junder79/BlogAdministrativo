from django.conf.urls import include, url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'), 
    path('post/new', views.post_new, name='post_new'),
    path('post/contacto', views.post_contacto, name='post_contacto'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #Eliminar POST
    path('post/<int:pk>', views.post_delete, name='post_delete'),

]

