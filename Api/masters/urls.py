from django.urls import path
from . views import *

# Create your views here.

urlpatterns = [
    path('',IndexView.as_view(), name = 'index'),
    path('getTradeData/',ReadTradeData.as_view(),name='getTradeData'),
    path('getTradeDataSearch/',ReadTradeDataSearch.as_view(),name='getTradeDataSearch'),
    path('getCsv/',ConvertCsv.as_view(),name='getCsv'),
]
