from django.urls import path
from .import views


urlpatterns = [

path("",views.create_book),
path('author/',views.create_author,name ='author'),
    path("listviews/",views.listBook),

    path('detailsview/<int:book_id>/',views.detailsView ,name = 'details'),

    path('updateview/<int:book_id>/',views.updateBook,name ='update'),

    path('delview/<int:book_id>/',views.delview,name = 'delete'),
    path('index',views.index)

]