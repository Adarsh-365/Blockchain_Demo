"""
URL configuration for blockchaindemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('hash/', views.hash, name='hash'),
    path('block/', views.block, name='block'),
    path('blockchain/', views.blockchain, name='blockchain'),
    path('distributed/', views.distributed, name='distributed'),
    path('tokens/', views.tokens, name='tokens'),
    path('coinbase/', views.coinbase, name='coinbase'),
     path('public-private-keys/keys/', views.keys, name='keys'),
      path('public-private-keys/signature/', views.signature, name='signature'),
       path('public-private-keys/transactions/', views.transactions, name='transactions'),
    path('public-private-keys/blockchain/', views.blockchainpub, name='blockchainpub'),
]
