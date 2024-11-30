# Файл core/definitions.py 
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

# BACKEND_DIR = ROOT_DIR / "backend"
SRC_DIR =  ROOT_DIR / "src" # BACKEND_DIR / "src"
MODEL_DIR = SRC_DIR / "models"

DATA_PATH = MODEL_DIR / "medium_articles_with_embeddings.pkl"
MODEL_NAME = 'all-MiniLM-L6-v2'
