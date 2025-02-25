import pandas as pd

def preprocess_validation_data(validation_path, output_path):
    df = pd.read_csv(validation_path)
    order = (df['history'].str.replace('\n', ' ').str.replace("'", ' ').str.replace("[", ' ').str.replace("]", ' ').str.strip().str.split().explode())
    aux = pd.merge(df['userId'], order, left_index=True, right_index=True)
    rel_col = []
    prev_user = None
    inverse_aux = aux[::-1].copy()
    for i in range(len(aux)):
        user = inverse_aux.userId.iloc[i]
        if user != prev_user:
            relevance = 1
        else:
            relevance = relevance + 1
        rel_col.append(relevance)
        prev_user = user
    inverse_aux['relevance'] = rel_col
    final = inverse_aux[::-1]
    final.to_csv(output_path, header=True, index=False)
