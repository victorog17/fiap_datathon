def preprocess_history(history_str):
    """Transforma a string do histórico de acessos em uma lista limpa."""
    if isinstance(history_str, str):
        return history_str.replace("\n", " ").replace("'", " ").replace("[", " ").replace("]", " ").strip().split()
    return []
