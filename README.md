# Projektseminar "Wettbewerb Medical Data Science" Wintersemester 2025/26
Dieses Repository enthält den Demo-Code zum Projektseminar "Wettbewerb Medical Data Science" WiSe 2025/26. Das Beispiel definiert gleichzeitig das Interface zu unserem Evaluierungs-System.

## Erste Schritte

1. Klone/Kopiere dieses Repository
2. Richte ein eigenes privates Repository auf github/gitlab ein. Darüber könnt ihr später die Abgaben eurer Modelle machen. 
3. Füge unseren Account als Collaborator hinzu (Github: Name="wettbewerbKI", Gitlab: auf Anfrage)
3. Lege ein Python Environment an. Am Besten funktioniert das mit [Anaconda](https://www.anaconda.com/products/distribution), und `conda create -n mds-wise25 python=3.8`
4. Installiere alle von uns verwendeten Pakete in diesem Environment, welche in "requirements.txt" gelistet sind mit
```
 conda activate mds-wise25
 pip install -r requirements.txt
``` 
5. Lade die Trainingsdaten herunter (in moodle verlinkt), entpacke sie und lege Sie in einem Dateordner ab
5. Probiere aus, ob alles funktioniert, indem du einmal unseren Predict und Scoring Code bei dir ausführst (und den Testdatenordner entsprechend anpasst):
```
python predict_pretrained.py --test_data_path datasets\training_dataset.mat --model_name model.pkl
python score.py --test_data_path datasets\training_dataset.mat --predictions_path predictions.mat
```

## Wichtig!

Bitte achtet bei der Abgabe darauf, dass alle von uns gestellten Dateien auf dem Top-Level des Repositories liegen. Testet die Funktionsfähigkeit eures Codes mit dem Skript predict_pretrained.py. 

Die Dateien 
- predict_pretrained.py
- wettbewerb.py
- score.py

werden von uns beim testen auf den ursprünglichen Stand zurückgesetzt. Es ist deshalb nicht empfehlenswert diese zu verändern. In predict.py ist für die Funktion `predict_labels` das Interface festgelegt, das wir für die Evaluierung verwenden.

`predict_labels(data:np.ndarray, model_name:str) -> np.ndarray`

Insbesondere den `model_name` könnt ihr verwenden um bei der Abgabe verschiedene Modelle zu kennzeichnen, welche zum Beispiel durch eure Ordnerstruktur dargestellt werden. 

Bitte gebt alle verwendeten packages in "requirements.txt" bei der Abgabe zur Evaluation an und testet dies vorher in einer frischen Umgebung mit `pip install -r requirements.txt`. Als Basis habt ihr immer die vorgegebene "requirements.txt"-Datei. Wir selbst verwenden Python 3.8. Wenn es ein Paket gibt, welches nur unter einer anderen Version funktioniert ist das auch in Ordung. In dem Fall bitte Python-Version mit angeben.
