from uagents import Agent, Context, Model
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from urllib.parse import parse_qs, urlparse


yt = Agent(name="youtubeTranscriptGrabber", 
            seed="youtube_transcript_grabber",
            port=8001,
            endpoint=["http://localhost:8001/submit"])


class Message(Model):
    string_field: str


@yt.on_interval(5)
async def interval_task(ctx: Context):
    ctx.logger.info("Executing periodic task...")

@yt.on_message(Message)
async def handle_message(ctx: Context, sender: str, url: Message):
    transcript = getTranscript(url)
    ctx.logger.info(f"Got message from {sender}: {url}")
    if response.status_code == 200:
        ctx.logger.info(f"Got message from {sender}: {url}")

    else:
        return None
@yt.on_event("startup")
async def say_hello(ctx: Context):
    url = "https://youtu.be/fH2777jU4EI?si=0em1aa9X486DHbqj"
    transcript = getTranscript(url)
    print(transcript)
    ctx.logger.info(f"Got url : {url}")

def getTranscript(url):
    id = url[url.index("v=")+2:]
    # url_data = urlparse("https://youtu.be/OgBF3N3MhYw?si=CrEwhdV8e0zpflEe")
    # id = url_data.query[2::]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript


if __name__ == "__main__":
    yt.run()