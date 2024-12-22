"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from toy_department.views import (
    main_page,
    shop_page,
    basket_page,
    login_page,
    registration,
    logout_page,
    buy_toy,
    actions_page,
    show_max,
    present,
    purchase_confirm)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('toys/', shop_page),
    path('basket/', basket_page),
    path('login/', login_page),
    path('logout/', logout_page),
    path('registration/', registration),
    path('buy/', buy_toy),
    path('actions/', actions_page),
    path('show_max/', show_max),
    path('present/', present),
    path('purchase_confirm/', purchase_confirm),
]
