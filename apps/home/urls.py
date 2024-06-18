# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('rtl/', views.rtl_support, name='rtl'),
    path('icons/', views.icons, name='icons'),
    path('table_list/', views.table_list, name='table_list'),
    path('typography/', views.typography, name='typography'),
    path('login/', views.login, name='login'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
