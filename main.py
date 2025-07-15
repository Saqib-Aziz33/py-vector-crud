from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def ping_server():
    return "server is running"
