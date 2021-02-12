from django.shortcuts import render
import os
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
import requests
import zipfile
import time
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.settings import DATA_PATH
import redis
import json

import pandas as pd
import openpyxl




def download_file():
    try:
        print(DATA_PATH)
        downloadUrl = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ050221_CSV.ZIP'
        url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ050221_CSV.ZIP"
        myfile = requests.get(url, headers={"User-Agent": "Chrome"}, allow_redirects=True)
        req = requests.get(downloadUrl)
        filename = "Date-" + time.strftime("%Y-%m-%d-%H") + ".zip"
        open(filename, 'wb').write(myfile.content)
        time.sleep(3)
        print("Extracting")
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            filename = "Date-" + time.strftime("%Y-%m-%d-%H") + ".csv"
            zip_ref.extractall('exctracted')
        return True
    except :
        return False




class IndexView(TemplateView):
    template_name = 'index.html'


class ReadTradeData(APIView):
    def get(self,request):
        
        download_file() #download data
        df = pd.read_csv(str(DATA_PATH)+'/EQ050221.CSV')
        code = df["SC_CODE"].tolist()
        name = df["SC_NAME"].tolist()
        Open = df["OPEN"].tolist()
        high = df["HIGH"].tolist()
        low = df["LOW"].tolist()
        close = df["CLOSE"].tolist()
        final = []
        
        
        for i in range(0,len(name)):
            
            n = name[i].strip()
            
            final.append(
                {
                    'code':code[i],
                    'name':name[i],
                    'open':Open[i],
                    'high':high[i],
                    'low':low[i],
                    'close':close[i]
                }
            )
        
        return JsonResponse(final, safe=False,status=200)
    

class ReadTradeDataSearch(APIView):
    def post(self,request):
        key = request.data['search-key']
        # download_file() #download data
        df = pd.read_csv(str(DATA_PATH)+'/EQ050221.CSV')
        code = df["SC_CODE"].tolist()
        name = df["SC_NAME"].tolist()
        Open = df["OPEN"].tolist()
        high = df["HIGH"].tolist()
        low = df["LOW"].tolist()
        close = df["CLOSE"].tolist()
        final = []
        for i in range(0,len(name)):
            n = name[i].strip()
            key = key.strip()
            if (n == key):
                final.append(
                    {
                        'code':code[i],
                        'name':name[i],
                        'open':Open[i],
                        'high':high[i],
                        'low':low[i],
                        'close':close[i]
                    }
            )
            
        return JsonResponse(final, safe=False,status=200)
    

class ConvertCsv(APIView):
    def post(self,request):
        key = request.data['search-key']
        
        df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33], [31, 32, 33]],columns=['code', 'name', 'open'])
        
        df.to_csv('equity_data.csv')

        return JsonResponse("true", safe=False,status=200)
    




