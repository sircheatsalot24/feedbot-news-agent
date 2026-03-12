import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from openai_client import getOpenAI

client = getOpenAI()

def parse(data):
    response = client.chat.completions.create(
        model="o4-mini",
        messages=[
            {"role": "system", "content": f"You are a news parser. Extract key news information from raw data. INCLUDE NOTHING BUT THE PARSED DATA. The format should be:\nProvider: [this is the News Publisher]\nTopic: [this is the topic (or list of topics) that the news story relates to/is.]\nDescription: [go in-depth with the news's description. It should be enough information to make a digest out of it.]\nLink: [provide the link to the story.]"},
            {"role": "user", "content": "Parse this: " + str(data)},
        ],
    )

    return response.choices[0].message.content