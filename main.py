from fastapi import FastAPI
from routes import knowledge_base

app = FastAPI()


@app.get("/")
def ping_server():
    return "server is running"


app.include_router(router=knowledge_base.router, prefix="/api/knowledge-base")
