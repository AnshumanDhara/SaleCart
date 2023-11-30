from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name = 'homepage'),
    path('login', views.login, name = 'login'),
    path('cart', views.cart, name = 'cart'),
    path('category1', views.category1, name = 'category1'),
    path('category2', views.category2, name = 'category2'),
    path('searchresult', views.searchresult, name = 'searchresult'),
    path('signup', views.signup, name = 'signup'),
    path('', views.Fhomepage, name = 'Fhomepage'),
    path('Flogin', views.Flogin, name = 'Flogin'),
    path('Fresetpassword', views.Fresetpassword, name = 'Fresetpassword'),
    path('Fsearch_category', views.Fsearch_category, name = 'Fsearch_category'),
    path('Fsearch_name', views.Fsearch_name, name = 'Fsearch_name'),
    path('Fsignup', views.Fsignup, name = 'Fsignup'),
    path('Fuserprofile', views.Fuserprofile, name = 'Fuserprofile'),
    path('Fcart', views.Fcart, name = 'Fcart'),
]