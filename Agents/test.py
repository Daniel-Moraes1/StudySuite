from youtube_transcript_api import YouTubeTranscriptApi
import requests
from openai import OpenAI
import os

OpenAI.api_key = "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"

client = OpenAI()

def getTranscript(url):
    id = url[url.index("v=")+2:]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript



def createQuiz(transcript):
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant with the goal of creating study materials for users. You generate either a multiple choice quiz based off of transcripts from YouTube videos. You also maintain knowledge of the timestamps and quotes from which you generate questions. You follow user instruction as the user wants."},
            {"role": "user", "content": "Create a multiple choice quiz based off of the following transcript: " + str(transcript)}
        ],
    )


    print(completion.choices[0].message)
    return


def main():
    url = "https://www.youtube.com/watch?v=3KaffTIZ5II"
    transcript = getTranscript(url)
    print(transcript)
    quiz = createQuiz(transcript)
    print(quiz)

    return 0

main()
    