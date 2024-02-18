from youtube_transcript_api import YouTubeTranscriptApi
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



def getTranscript(url):
    id = url[url.index("v=")+2:]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript


from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)


def createQuiz(transcript):
    json_format = {
        "question": "blblablabla",
        "options": ["blablabla", "blablabla", "blablabla", "blablabla"],
        "answer_index": 1,
    }
    # we just have to prompt the json to fix
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Create me 1 multiple question quiz with 3 options. Return me the json format: " + str(json_format) + "based on " + str(transcript)},
        {"role": "user", "content": "Hello!"}
    ],
    max_tokens=25000,
    )

    return response.choices[0].message


def main():
    url = "https://www.youtube.com/watch?v=3KaffTIZ5II"
    transcript = getTranscript(url)
    print(os.getenv("OPENAI_API_KEY"))
    quiz = createQuiz(transcript)
    print(quiz)

    return 0

main()
    