# Extraction_Info
# Extraction d'Entités Nommées Médicales (NER) - Projet NLP

## 📦 Structure du Projet

```
/Extraction_Info/
├── Corpus/
│   ├── FRASIMED/
│   └── QUAERO_FrenchMed/
├── Outputs/
│   ├── frasimed_bio.txt
│   ├── quaero_bio.txt
│   ├── merged_bio.txt
│   ├── train.txt
│   ├── dev.txt
│   ├── test.txt
│   ├── train.spacy
│   ├── dev.spacy
│   └── test.spacy
├── Scripts/
│   ├── parse_frasimed.py
│   ├── parse_quaero.py
│   ├── convert_and_merge.py
│   ├── split_dataset.py
│   ├── train_spacy.py
│   ├── predict_entities.py
│   └── evaluate_ner.py
├── config.cfg
└── config_filled.cfg
```

---

## 🚀 Objectif

Le projet vise à entraîner un modèle NLP pour la reconnaissance d'entités nommées médicales (NER) à partir des corpus FRASIMED et QUAERO. L'objectif est d'identifier des entités telles que les **maladies**, **symptômes**, **traitements**, etc.

---

## ⚙️ Installation

1. Créer un environnement virtuel :

   ```bash
   python -m venv spacy_env
   source spacy_env/bin/activate  # Mac/Linux
   .\spacy_env\Scripts\activate  # Windows
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Installer SpaCy :

   ```bash
   pip install spacy
   python -m spacy download fr_core_news_md
   ```

---

## ✅ Étapes d'Exécution

### 1. Extraction des Entités - FRASIMED

```bash
python Scripts/parse_frasimed.py
```

### 2. Extraction des Entités - QUAERO

```bash
python Scripts/parse_quaero.py
```

### 3. Fusion des Datasets

```bash
python Scripts/convert_and_merge.py
```

### 4. Division des Données (Train/Dev/Test)

```bash
python Scripts/split_dataset.py
```

### 5. Conversion au Format SpaCy

```bash
python Scripts/train_spacy.py
```

### 6. Génération de la Configuration

```bash
python -m spacy init config config.cfg --lang fr --pipeline ner --optimize efficiency
python -m spacy init fill-config config.cfg config_filled.cfg
```

### 7. Entraînement du Modèle

```bash
python -m spacy train config_filled.cfg --output ./output --paths.train Outputs/train.spacy --paths.dev Outputs/dev.spacy
```

### 8. Évaluation du Modèle

```bash
python Scripts/evaluate_ner.py
```

### 9. Prédiction des Entités

```bash
python Scripts/predict_entities.py
```

---


## 📅 Auteur

Zeinab Omar - Kaouther Abderrahmane 
