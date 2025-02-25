import sys
import os
import pickle
import pandas as pd
from collections import Counter
from src.utils import preprocess_history

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

MODEL_PATH = "models/recommender.pkl"
VALIDATION_PATH = "data/validacao.csv"
OUTPUT_PATH = "data/predictions.csv"

def load_model():
    """Carrega o modelo treinado."""
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def generate_predictions():
    """Gera recomendações para os usuários de validação."""
    model = load_model()
    df_test = pd.read_csv(VALIDATION_PATH)

    recommendations = []
    for _, row in df_test.iterrows():
        user_id = row['userId']
        history = preprocess_history(row['history'])
        recs = [item[0] for item in model.get(user_id, Counter()).most_common(10)]
        recommendations.append((user_id, recs))

    # Salva as previsões
    df_output = pd.DataFrame(recommendations, columns=["userId", "recommendations"])
    df_output.to_csv(OUTPUT_PATH, index=False)
    print(f"Previsões salvas em {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_predictions()
