import uvicorn
from fastapi import FastAPI
import routers.product as product
import routers.inventory as inventory
import models
from database import engine


models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(product.router)
app.include_router(inventory.router)


@app.get("/")
def read_root():
    return {"message": "FastAPI is running on a custom port"}


if __name__ == "__main__":
    uvicorn.run('main:app', port=8501, reload=True)