# Myti Practice Test


Per testare il codice bisogna avere python3>=7 e nessun'altra libreria esterna da installare. Sulla propria macchina clonare il repository e scrivere sul terminale 
python3 e il nome del file che si vuole testare (e.g python3 fase_1.py), oppure usare un IDE e farli partire lì.<br>
Per quanto riguarda il webserver il content-type della richiesta POST dev'essere 'application/json' e il body dev'essere del formato JSON:
```javascript
[
  {
    "firstname": "DamianoNuovo2",
    "lastname": "Mancini",
    "birthdate": "14-11-1994",
    "grades": "6-7-7-8-4"
  },
  {
    "firstname": "MarioNuovo2",
    "lastname": "Rossi",
    "birthdate": "01-12-1990",
    "grades": "2-3-7-10-4"
  }
]
```
La porta per testarlo in locale è la 8000, perciò il request url dev'essere http://localhost:8000/ sia per GET che POST.
Lo status 400 per il POST è perchè nell'header c'è un content-type sbagliato, altrimenti non restituisce nulla ma con lo status 200. 
Testato su Advance REST client.
