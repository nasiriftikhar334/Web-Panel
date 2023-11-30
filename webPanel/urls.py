"""webPanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginView.as_view(), name='public'),
    path('start/',views.check_view,name='start'),
    path('login/',views.signin, name='login'),
    path('signup/',views.signup, name='signup'),
    path('update_data/',views.update_data, name='update_data'),
    path('step-1/',views.save_registration),
    path('step-2/',views.step2,name='step-2'),
    path('step-3/',views.step3,name='step-3'),
    path('step-4/',views.step4,name='step-4'),
    path('status/',views.status,name='status'),
]
