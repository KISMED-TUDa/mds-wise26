# -*- coding: utf-8 -*-
"""
Diese Datei sollte nicht verändert werden und wird von uns gestellt und zurückgesetzt.

Skript testet das vortrainierte Modell


@author: Maurice Rohr und Jad Haidamous
"""


from predict import predict_labels
from wettbewerb import load_data, save_predictions
import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict given Model')
    parser.add_argument('--test_data_path', action='store',type=str)
    parser.add_argument('--model_name', action='store',type=str)
    parser.add_argument('--allow_fail',action='store_true',default=False)
    args = parser.parse_args()
    
    X, y, _ = load_data(args.test_data_path)
    print(f"Teste Modell auf {X.shape[0]} Aufnahmen")
    
    start_time = time.time()

    try:
        predictions = predict_labels(X, args.model_name)
    except:
        if args.allow_fail:
            raise
        
    pred_time = time.time()-start_time
    
    save_predictions(predictions, "predictions.mat") # speichert Prädiktion in CSV Datei
    print("Runtime", pred_time, "s")
