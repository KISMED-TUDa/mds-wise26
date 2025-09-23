__author__ = "Jad Haidamous"

import numpy as np
from typing import Dict
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy.io import loadmat, savemat
import argparse

def score(mat_file_labels:str, mat_file_predictions:str) -> Dict[str, float]:
    """
    Berechnet relevante Metriken des Wettbewerbs, sowie weitere Metriken

    Parameters
    ----------
    mat_file_labels : str
        Pfad zu der mat Datei mit den Labels.
    mat_file_predictions : str
        Pfad zu der mat Datei mit den Vorhersagen.

    Returns
    -------
    Dict, wobei die folgenden keys existieren:
        accuracy : float
            Genauigkeit des Modells
        precision : float
            Anteil der positiven Klassifizierungen des Modells, die tatsächlich positiv sind
        recall : float
            Anteil der positiven Fälle, die vom Modell als positiv klassifiziert worden sind
        f1 : float
            Harmonischer Mittelwert von precision und recall
    """
    labels:np.ndarray = loadmat(mat_file_labels)["labels"].flatten() # Shape (N, )
    preds:np.ndarray = loadmat(mat_file_predictions)["predictions"].flatten()  # Shape (N, )
    
    metrics = {"accuracy":accuracy_score(y_true=labels, y_pred=preds),
               "precision":precision_score(y_true=labels, y_pred=preds),
               "recall":recall_score(y_true=labels, y_pred=preds),
               "f1":f1_score(y_true=labels, y_pred=preds)}
    
    return metrics

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict given Model')
    parser.add_argument('--test_data_path', action='store',type=str)
    parser.add_argument('--predictions_path', action='store',type=str)
    parser.add_argument('--allow_fail', action='store_true',default=False)
    args = parser.parse_args()

    metrics = score(args.test_data_path, args.predictions_path)
    print(metrics)