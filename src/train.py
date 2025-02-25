import sys
import os
import glob
import pandas as pd
import pickle
from collections import defaultdict, Counter
from src.utils import preprocess_history

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TRAIN_PATH = "data/train/"
MODEL_PATH = "models/recommender.pkl"

def train_model():
    """Treina um modelo de recomendação baseado na frequência de leitura."""
    histories = defaultdict(Counter)

    for fpath in glob.glob(os.path.join(TRAIN_PATH, "*.csv")):
        df = pd.read_csv(fpath)
        for _, row in df.iterrows():
            user = row['userId']
            hist = preprocess_history(row['history'])
            histories[user].update(hist)

    # Salva o modelo treinado
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(histories, f)
    
    print(f"Modelo salvo em {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
