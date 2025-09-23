# -*- coding: utf-8 -*-
"""

Skript testet das vortrainierte Modell


@author: Jad Haidamous
"""

import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

###Signatur der Methode (Parameter und Anzahl return-Werte) darf nicht verändert werden
def predict_labels(data:np.ndarray, model_name:str) -> np.ndarray:
    '''
    Parameters
    ----------
    data : ndarray
        Datenmatrix
    model_name : str
        Name eures Models,das ihr beispielsweise bei Abgabe genannt habt. 
        Kann verwendet werden um korrektes Model aus Ordner zu laden
    
    Returns
    -------
    prediction : ndarray
        enthält Vorhersage, ob Sepsis vorhanden ist
    '''

    #------------------------------------------------------------------------------
    # Euer Code ab hier  

    model:LogisticRegression = joblib.load(model_name)

    data = data.reshape(data.shape[0], -1)
    data[np.isnan(data)] = 0

    preds:np.ndarray = model.predict(data)
  
    return preds
                               
                               
        
