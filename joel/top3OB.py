import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt


tickers = ["EQNR.OL","DNB.OL", "MOWI.OL"]

#Lager en tabell med snittet av dagenes høyeste og laveste snittpris i løpet av oppgitt dato intervall
#Datoene må skrives som en string på formen: "YYYY-MM-DD".
startDato= "2021-01-01"
sluttDato= "2022-09-27"
def createSnittPrisTabell(ticker, startDato, sluttDato):
    data = yf.download(ticker, start=startDato, end=sluttDato, interval = "1d", group_by = "ticker")
    return data

eqnrSnittPris = createSnittPrisTabell(tickers[0], startDato, sluttDato)
sndSnittPris = createSnittPrisTabell(tickers[1], startDato, sluttDato)
mowiSnittPris = createSnittPrisTabell(tickers[2], startDato, sluttDato)

print(eqnrSnittPris)
