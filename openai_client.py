import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def getOpenAI():
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

getOpenAI()
