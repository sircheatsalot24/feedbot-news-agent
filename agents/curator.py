import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from openai_client import getOpenAI
from agents.parser import parse
from config import getConfig

client = getOpenAI()

def curate(parsedData, config):
    response = client.chat.completions.create(
        model="o4-mini",
        messages=[
            {"role": "system", "content": "Given news stories, pick the strongest stories that match/relate to the user's provided preference. For example, if the user's preference is Politics, then return all the news stories with one of the topics listed as Politics. Also, separate the user's prefrences and run through the stories for each one to find matches for multiple prefrences."},
            {"role": "user", "content": f"My prefrence(s) are {config} and here are the news stories: {parsedData}"}
        ]
    )
    return response.choices[0].message.content