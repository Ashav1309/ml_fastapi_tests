from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
classifier = pipeline("sentiment-analysis")

class Item(BaseModel):
    text: str

# Корневой маршрут
@app.get("/")
def root():
    return {"message": "Hello World"}

# Функция для получения экземпляра классификатора
def get_classifier():
    return classifier

# Маршрут для предсказания сентимента текста
@app.post("/predict/")
def predict(item: Item, classifier = Depends(get_classifier)):
    try:
        result = classifier(item.text)[0]  # Получаем результат от классификатора
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Обработка ошибки в случае возникновения исключения
