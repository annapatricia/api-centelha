from fastapi import FastAPI
app = FastAPI(title="API Escolas")
@app.get("/")
def home():
    return {"mensagem": "Sistema de Escolas online"}

