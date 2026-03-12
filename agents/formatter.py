import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from openai_client import getOpenAI

client = getOpenAI()

def format(curatedData):
    response = client.chat.completions.create(
        model="o4-mini",
        messages=[
            {"role": "system", "content": "Given a set of news stories, format them into a clean and visually appealing daily digest, which explains the story in detail. Keep all the data, no matter how big or small. If you think you need more data, scrape it from the provided link."},
            {"role": "user", "content": f"Here is the news data: {curatedData}"}
        ]
    )

    return response.choices[0].message.content