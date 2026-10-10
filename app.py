from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv() #загружает скрытые переменные из файла .env

allow_origins = os.getenv("ALLOWED_ORIGIN" , '')

app= FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
@app.get("/app/hello")
def hello():   
    return{"message": 'Сервак запущен'}



