from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.add_show_data, name="home"),
    path('delete/<int:id>/', views.delete_info, name="deleteInfo"),
    path('update/<int:id>/', views.update_info, name="updateInfo"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name='crud/logout.html'),name='logout'),
]