from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
# from routes import router as api_router
from fastapi.responses import RedirectResponse
import uvicorn

config = dotenv_values(".env")

app = FastAPI()

# app.include_router(api_router, tags=["paciente"], prefix="/pacientes")

@app.get("/", include_in_schema=False)
async def root():
    # return RedirectResponse(url='/docs')
    return {"message": "Pero mirá"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# Start APP
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8080, reload=True)
      