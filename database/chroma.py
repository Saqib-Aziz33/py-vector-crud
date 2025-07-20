# import chromadb
from config import CHROMA_DB_DIR
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from chromadb.config import Settings

CHROMA_DIR = rf"{CHROMA_DB_DIR}"
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2")

vector_store = Chroma(
    collection_name="past_experience",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR,
    client_settings=Settings(anonymized_telemetry=False)
)
