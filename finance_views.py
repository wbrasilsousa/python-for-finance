from django.shortcuts import render
from datetime import date
from django.conf import settings
import yfinance
import pandas
from matplotlib import pyplot as plt


def finance(request):

    ativos = [
        'IVV',
        'Gold',
        'EWZ',
        'BTC-USD'
    ]

    inicio = date.today().replace(year = date.today().year - 1)
    fim = date.today()

    # Grafico Preço
    precos = pandas.DataFrame()
    for i in ativos:
        precos[i] = yfinance.download(i, start=inicio, end=fim)['Adj Close']

    normalizado = precos/precos.iloc[0]
    normalizado.plot(legend=True)

    plt.ylabel('Preço ($)')
    plt.xlabel('Data')
    plt.title('EUA x Gold x Brasil x BTC (dolarizado)')
    plt.savefig(str('graficos/price.png')


    # Grafico Volume
    for i in ativos:
        precos[i] = yfinance.download(i, start=inicio, end=fim)['Volume']

    normalizado = precos/precos.iloc[0]
    normalizado.plot(subplots=True, title='Volume')

    plt.xlabel('Data')
    plt.savefig('graficos/volume.png')

    return render(request, 'finance.html')
