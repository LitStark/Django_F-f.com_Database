from django.urls import path
from . import views
urlpatterns = [
    path ('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('data_table/', views.crm, name='crm'),
    path('add_member/', views.add_member, name='add_member'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('data_table/delete/<int:id>', views.delete, name='delete'),
    path('data_table/edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('signup/', views.signup, name='signup'),
    path('handleSignup/', views.handleSignup, name='handleSignup'),
    path('login/', views.loginpage, name='login'),
    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handlelogout, name='logout'),
]
