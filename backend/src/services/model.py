import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from src.core.definitions import DATA_PATH, MODEL_NAME

# Загрузка модели и данных
model = SentenceTransformer(MODEL_NAME)
data = pd.read_pickle(DATA_PATH)

def get_recommendations(user_input: str):
    # Создаем эмбеддинг для запроса
    query_embedding = model.encode(user_input).reshape(1, -1)

    # Считаем косинусное расстояние между запросом и статьями
    data['similarity'] = cosine_similarity(data['embeddings'].tolist(), query_embedding).squeeze()
    
    # Сортируем статьи по схожести и выбираем топ-10
    top_articles = data.nlargest(10, 'similarity')[['title', 'url', 'similarity']] # , 'summary'
    results = top_articles.to_dict(orient="records")
    print(results)

    return results
