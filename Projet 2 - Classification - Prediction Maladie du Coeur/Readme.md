<h1>Prediction Maladie du coeur</h1>

# Context 

Le but de ce projet est de prédire si un patient a une maladie du coeur ou non.

# A propos du dataset heart.csv

Cet ensemble de données date de 1988 et se compose de quatre bases de données : Cleveland, Hongrie, Suisse et Long Beach V. Il contient 76 attributs, y compris l'attribut prédit, mais toutes les expériences publiées se réfèrent à l'utilisation d'un sous-ensemble de 14 d'entre eux. Le champ "Target" fait référence à la présence d'une maladie cardiaque chez le patient. 
Il s'agit d'un nombre entier 
    0 = pas de maladie 
    1 = maladie.


    ##Information usr les colonnes du dataset
        age
        sex
        chest pain type (4 values)
        resting blood pressure
        serum cholestoral in mg/dl
        fasting blood sugar > 120 mg/dl
        resting electrocardiographic results (values 0,1,2)
        maximum heart rate achieved
        exercise induced angina
        oldpeak = ST depression induced by exercise relative to rest
        the slope of the peak exercise ST segment
        number of major vessels (0-3) colored by flourosopy
        thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
        The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.



# A propos du notebook

Le notebook est divisé en 3 parties :
- 1. Exploration des données
- 2. Préparation des données (Data Pre processing)
- 3. Modélisation 

# A propos du modèle

Le modèle utilisé est un modèle de classification supervisée.
Nous utiliserons l'algorithe de reression logistique car il s'agit d'un problème de classification binaire.
