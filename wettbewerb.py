# -*- coding: utf-8 -*-
"""
Diese Datei sollte nicht verändert werden und wird von uns gestellt und zurückgesetzt.

Funktionen zum Laden der Dateien
"""
__author__ = "Jad Haidamous"

from typing import Tuple
import scipy.io as sio
import numpy as np

### Achtung! Diese Variable nicht veraendern.
CONST_FEATURE_NAMES = ['HR',
                    'O2Sat',
                    'Temp',
                    'SBP',
                    'MAP',
                    'DBP',
                    'Resp',
                    'EtCO2',
                    'BaseExcess',
                    'HCO3',
                    'FiO2',
                    'pH',
                    'PaCO2',
                    'SaO2',
                    'AST',
                    'BUN',
                    'Alkalinephos',
                    'Calcium',
                    'Chloride',
                    'Creatinine',
                    'Bilirubin_direct',
                    'Glucose',
                    'Lactate',
                    'Magnesium',
                    'Phosphate',
                    'Potassium',
                    'Bilirubin_total',
                    'TroponinI',
                    'Hct',
                    'Hgb',
                    'PTT',
                    'WBC',
                    'Fibrinogen',
                    'Platelets',
                    'Age',
                    'Gender']

### Achtung! Diese Funktion nicht veraendern.
def load_data(mat_file_path:str) -> Tuple[np.ndarray]:
    """
    Liest die Daten aus der .mat Datei ein.

    Parameters
    ----------
    mat_file_path : str
        Pfad zur .mat Datei.

    Returns
    -------
    X : ndarray
        Die Datenmatrix
    y : ndarray
        Die Annotationen
    feature_names : Tuple[str]
        Namen der Features in der Datenmatrix
    """
    
    dataset = sio.loadmat(mat_file_path)
    X:np.ndarray = dataset["data"]
    y:np.ndarray = dataset["labels"].flatten()
        
    print(f"{X.shape[0]} Zeilen wurden geladen.")
    return X, y, CONST_FEATURE_NAMES

### Achtung! Diese Funktion nicht veraendern.
def save_predictions(predictions:np.ndarray, save_path:str) -> Tuple[np.ndarray]:
    """
    Liest die Daten aus der .mat Datei ein.

    Parameters
    ----------
    predictions : ndarray
        Vorhersagen
    save_path : str
        Pfad zum Speichern der .mat Datei.

    Returns
    -------
    """
       
    sio.savemat(save_path, {"predictions": predictions})
