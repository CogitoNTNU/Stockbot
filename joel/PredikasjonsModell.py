import yfinance as yf
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score




ticker, stockName, startDatoPåDataYYYYMMDD = "EQNR.OL", "Equinor", "2005-01-01"


stockName = yf.Ticker(ticker)
stockName = stockName.history(period="max") 
stockName.index = pd.to_datetime(stockName.index)

#Sletter rader fra tabellen
del stockName["Dividends"]
del stockName["Stock Splits"]

#Opretter en ny kollonne for morgendagnespris
#Morgendagenspris tilsvarer neste dags pris ved "Close":
stockName["Tomorrow"]=stockName["Close"].shift(-1)

#Sjekker om prisen i morgen er større en prisen som var i dag. Kollonnen target får verdi 1 om dette er tilfellet.
#Evnt kan endre på dette til at verdien blir kun 1 om prisen økte med to prosent (????)
stockName["Target"]=(stockName["Tomorrow"] > stockName["Close"]).astype(int)

#Fjerner all data før denne datoen fordi det kan være utdatert
stockName = stockName.loc[startDatoPåDataYYYYMMDD:].copy()

print(stockName)


#Lager modeller
model = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
model1 = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
model2 = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
model3 = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
model4 = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
model5 = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)


#Sorterer datasettet etter trenings datsett og test datsett. Vil at datasett skal være delelig på 5.
train = stockName.iloc[:-100]
test = stockName.iloc[-100:]
rest = len(train.index) % 5
train = train[(rest):]



#Deler treningsdatasettet opp i 5 biter:
dataChunkSize = len(train.index)//5
train1 = train[0:dataChunkSize]
train2 = train[0:(2*dataChunkSize)]
train3 = train[0:(3*dataChunkSize)]
train4 = train[0:(4*dataChunkSize)]
train5 = train[0:(5*dataChunkSize)]



#Ramdom forest modellene skal nå trenes på predikerikteringfaktorene (?) under.
# Etter dette skal vi ha trent ai modellen. 
predictors = ["Close", "Volume", "Open", "High", "Low"]
model1.fit(train1[predictors], train1["Target"])
model2.fit(train2[predictors], train2["Target"])
model3.fit(train3[predictors], train3["Target"])
model4.fit(train4[predictors], train4["Target"])
model5.fit(train5[predictors], train5["Target"])


#Prediksjonene lages
    #predikasjoner på resten av treningsette som modellen ikke er trent på. 
    #Modellen under er basert på modell1:
train2new = train[(dataChunkSize):]
preds1 = model1.predict(train2new[predictors])
preds1 = pd.Series(preds1, index=train2new.index)
print("Riktig prosentscore for modell 1:")
print(precision_score(train2new["Target"], preds1))
print("\n")


    #predikasjoner på resten av treningsette som modellen ikke er trent på. 
    #Modellen under er basert på modell2:
train3new = train[(2*dataChunkSize):]
preds2 = model2.predict(train3new[predictors])
preds2 = pd.Series(preds2, index=train3new.index)
print("Riktig prosentscore for modell 2:")
print(precision_score(train3new["Target"], preds2))
print("\n")


    #predikasjoner på resten av treningsette som modellen ikke er trent på. 
    #Modellen under er basert på modell3:
train4new = train[(3*dataChunkSize):]
preds3 = model3.predict(train4new[predictors])
preds3 = pd.Series(preds3, index=train4new.index)
print("Riktig prosentscore for modell 3:")
print(precision_score(train4new["Target"], preds3))
print("\n")


    #predikasjoner på resten av treningsette som modellen ikke er trent på. 
    #Modellen under er basert på modell4:
train5new = train[(4*dataChunkSize):]
preds4 = model4.predict(train5new[predictors])
preds4 = pd.Series(preds4, index=train5new.index)
print("Riktig prosentscore for modell 4:")
print(precision_score(train5new["Target"], preds4))
print("\n")


    #predikasjoner på resten av treningsette som modellen ikke er trent på. 
    #Modellen under er basert på modell5: 
    ####OBS TESTER PÅ TRENINGSETTET. MENINGLØS TEST. FJERN!
preds5 = model5.predict(train5new[predictors])
preds5 = pd.Series(preds4, index=train5new.index)
print("Riktig prosentscore for modell 5:")
print(precision_score(train5new["Target"], preds5))
print("\n")