from django.conf.urls import url
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

# urlpatterns = [
#     url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
#     url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
#     url(r"signup/$", views.SignUp.as_view(), name="signup"),
# ]
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contacts,name='contact'),
    path('listings/',views.details,name='details'),
    path('signup/',views.signup,name='signup'),
    path('farmer_details/',views.farmerform,name='farmerform'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('detail_view/<int:pk>',views.detail_view,name='detail_view')
]
