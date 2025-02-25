from collections import defaultdict, Counter
import glob
import pandas as pd

def compute_user_histories(train_path):
    histories = defaultdict(Counter)
    for fpath in glob.glob(f'{train_path}/*.csv'):
        df = pd.read_csv(fpath)
        for _, row in df.iterrows():
            user = row['userId']
            hist = row['history']
            hist = (hist.replace('\n', ' ').replace("'", ' ').replace("[", ' ').replace("]", ' ').strip().split())
            histories[user].update(hist)
    return histories

def recommend_top_k(histories, user_id, k=10):
    return [item[0] for item in histories[user_id].most_common(k)]
