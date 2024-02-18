from youtube_transcript_api import YouTubeTranscriptApi
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

from urllib.parse import urlparse

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def getTranscript(url):
    url_data = urlparse(url)
    video_id = ''

    if 'youtu.be' in url_data.netloc:
        # Extract video ID from path for shortened URLs
        video_id = url_data.path[1:]  # Remove the leading '/'
    else:
        # Extract video ID from query parameters for standard URLs
        query_params = dict(qc.split('=') for qc in url_data.query.split('&') if qc)
        if 'v' in query_params:
            video_id = query_params['v']

    if not video_id:
        raise ValueError("Could not extract video ID from URL.")

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript


# given a transcript, we create a quiz question
def createQuiz(transcript: str):
    json_format = """{
        "question": "blblablabla",
        "options": ["blablabla", "blablabla", "blablabla", "blablabla"],
        "answer_index": 1,
    }"""
    prompt = f"Create me 1 multiple question quiz with 3 options. Return me the json format: {str(json_format)} based on {str(transcript)}. Remember just the json string."
    # we just have to prompt the json to fix
    response = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a question generator AI. Don't generate a question if it's not necessary. "},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1500,
    )

    return response.choices[0].message.content

# a question generator that lazy loads. Call next on a gnerator to get the question
def quiz_generator(transcripts: list[str]):
    i = 0
    while i < len(transcripts):
        transcript = ' '.join([d['text'] for d in transcripts[i:i+9]])
        transcript = transcript.replace("\n", " ")
        # print(transcript)
        quiz = createQuiz(transcript)[7:-3]
        # print(quiz)
        testObj = json.loads(quiz)
        
        yield testObj  # This yields control back to the caller, resuming from here when next() is called again.
        i += 9

def get_next_question(question_gen):
    return next(question_gen)

def main():
    # VIDEO about productivity
    url1 = "https://youtu.be/0CmtDk-joT4?si=q5AMUjRgaD37Xgnm"

    # VIDEO about ai video
    url2 = "https://youtu.be/NXpdyAWLDas?si=AMRXgzlvinyFApKI"
    transcripts = getTranscript(url1)
    # we loop every 10 transcript to create a quiz
    quizzes = quiz_generator(transcripts)  # This creates a generator object but doesn't start the function yet.
    print(get_next_question(quizzes))

    return 0

main()
    