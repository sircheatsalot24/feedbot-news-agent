from fastapi import FastAPI, Request
from agents.parser import parse
from agents.curator import curate
from agents.formatter import format
from config import getConfig

feedbot = FastAPI()

@feedbot.post("/process")
async def process_news(request: Request):
    body = await request.json()
    if isinstance(body, list):
        data = body
        userConfig = "general"
    else:
        data = body.get("data")
        userConfig = body.get("config")

    parsedData = parse(data)
    curatedData = curate(parsedData, userConfig)
    formatedData = format(curatedData)

    return {"digest": formatedData}