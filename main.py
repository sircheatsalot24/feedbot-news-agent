from fastapi import FastAPI, Request

feedbot = FastAPI()

@feedbot.post("/process")
async def process_news(request: Request):
    data = await request.json()
    
    return {"digest": ""}