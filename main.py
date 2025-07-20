from fastapi import FastAPI
from routes import knowledge_base
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", tags=["Main"])
def ping_server():
    return HTMLResponse("<h1>server is running</h1>")


app.include_router(router=knowledge_base.router, prefix="/api/knowledge-base")
