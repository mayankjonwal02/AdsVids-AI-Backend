from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from services.agent import AdScriptGenerator
from dotenv import load_dotenv
import asyncio
import sys
from fastapi.middleware.cors import CORSMiddleware
    
load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ScriptGenerator = AdScriptGenerator()
# Pydantic model for POST request body
class requestbody(BaseModel):
    url: str

# GET route: fetch all products
@app.get("/")
def get_products():
    return "Welcome to the Product API! Use /products to manage products."

# POST route: add a new product
@app.post("/get_script")
async def add_product(request: requestbody):
    response = await ScriptGenerator.generate_script(request.url)
    return response