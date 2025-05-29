# Student Habits and Academic Performance Prediction

Questo è il progetto di Programmazione di Applicazioni Data Intensive del corso di Laurea Triennale di Ingegneria e scienze informatiche.

## Come Iniziare

### 1. Clona il Repository

```bash
git clone https://github.com/FrancescoPazz/Students-Habits-and-Academic-Perfomance.git
cd Students-Habits-and-Academic-Perfomance
```

### 2. Crea un Ambiente Virtuale

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installa le Dipendenze

```bash
pip install -r requirements.txt
```

### 4. Scarica il Dataset

Il dataset deve essere scaricato da [Kaggle](https://www.kaggle.com/datasets/aryan208/student-habits-and-academic-performance-dataset) e posizionato in:
```
data/enhanced_student_habits_performance_dataset.csv
```

### 5. Esegui il Notebook (Opzionale)

Per ricreare l'analisi e il modello:
```bash
jupyter notebook student_habits_and_academic_performance.ipynb
```

### 6. Avvia l'Applicazione Web

```bash
python run.py
```

L'applicazione sarà disponibile su `http://localhost:5000`

## Autori

- **Francesco Pazzaglia** - 0001077423
- **Filippo Massari** - 0001071420

*Progetto sviluppato per il corso di Programmazione di Data Intensive - A.A. 2024-2025*  
*Alma Mater Studiorum - Università di Bologna*
