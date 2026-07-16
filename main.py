from fastapi import FastAPI

app = FastAPI(title="CloudMind Test App")


@app.get("/")
def root():
    return {
        "message": "Hello Bassem",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
