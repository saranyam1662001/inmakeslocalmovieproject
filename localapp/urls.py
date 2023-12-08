from django.urls import path

from . import views
app_name='localapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),

    #path('thanks/',views.thanks,name='thanks')
]

