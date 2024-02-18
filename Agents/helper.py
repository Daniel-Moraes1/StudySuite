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

def get_summary_helper(transcript: str):
    prompt = f"As a text string summarizer expert. Summarize this {transcript}"
    # we just have to prompt the json to fix
    response = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a class notes summarizer. Give me the notes only. No other fluff. Keep it concise"},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1500,
    )

    return response.choices[0].message.content

def get_summary(transcripts, chunk_size=10):
    summaries = ""  # Initialize a list to hold all summaries
    total_transcripts = len(transcripts)
    start = 0  # Initialize start index for chunk processing

    while start < total_transcripts:
        end = min(start + chunk_size, total_transcripts)  # Determine end index for the current chunk
        transcript_chunk = ' '.join([transcripts[i]['text'] for i in range(start, end)])
        transcript_chunk = transcript_chunk.replace("\n", " ")
        # print("\n\n")
        # print(transcript_chunk)
        summary_result = get_summary_helper(transcript_chunk)  
        summaries += summary_result
        start += chunk_size  # Move to the next chunk
    return summaries  # Return the aggregated list of summaries

def main():
    # VIDEO about productivity
    url1 = "https://youtu.be/0CmtDk-joT4?si=q5AMUjRgaD37Xgnm"

    # VIDEO about ai video
    url2 = "https://youtu.be/NXpdyAWLDas?si=AMRXgzlvinyFApKI"
    transcripts = getTranscript(url1)
    # we loop every 10 transcript to create a quiz
    # quizzes = quiz_generator(transcripts)  # This creates a generator object but doesn't start the function yet.
    # print(get_next_question(quizzes))

    transcripts2 = getTranscript(url2)
    summary = get_summary(transcripts2, len(transcripts) // 5)
    print(summary)

    return 0

main()
    