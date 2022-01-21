from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):

    apiresponse = GetData()
    data = apiresponse.rates()
    USD_series = list()
    JPY_series = list()
    BRL_series = list()
    USD_series = data['USD'].tolist()
    JPY_series = data['JPY'].tolist()
    BRL_series = data['BRL'].tolist()


    chart = {

        'series': [USD_series, JPY_series, BRL_series]
    }
    contexto = {"USD_series": USD_series, 'JPY_series': JPY_series, 'BRL_series':BRL_series}

    return render(request, 'rates.html', context=contexto)

class GetData:
    def rates(self):
       import requests
       import  pandas as pd
       dataset = pd.DataFrame()
       df = pd.DataFrame(columns=['USD','JPY','BRL'])

       i= 0
       while i < 5:

            import datetime as dt
            today = dt.date.today()
            data = today - dt.timedelta(days=i)
            data = data.strftime('%Y-%m-%d')
            url = f'https://api.vatcomply.com/rates?date={data}'
            payload = ""
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            res_json = response.json()
            resultado = res_json['rates']
            dataset = dataset.append({'USD':resultado['USD'] ,'JPY':resultado['JPY'],'BRL':resultado['BRL']},ignore_index=True)
            i+=1

       return dataset



