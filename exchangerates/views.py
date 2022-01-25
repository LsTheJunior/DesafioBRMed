from django.shortcuts import render
from django.http import HttpResponse
import json
from controller import CallApi



def home(request):

    apiresponse = CallApi.GetData()
    data = apiresponse.rates()
    EUR_series = list()
    JPY_series = list()
    BRL_series = list()
    Dates_series = list()
    EUR_series = data['EUR'].tolist()
    JPY_series = data['JPY'].tolist()
    BRL_series = data['BRL'].tolist()
    Dates_series = data['Data'].tolist()
    Dates_series.reverse()

    chart = {

        'series': [EUR_series, JPY_series, BRL_series]
    }
    contexto = {"EUR_series": EUR_series, 'JPY_series': JPY_series, 'BRL_series':BRL_series, 'Dates_series':Dates_series}

    return render(request, 'rates.html', context=contexto)





