from uagents import Agent, Context, Model
from youtube_transcript_api import YouTubeTranscriptApi
import requests


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
    

def getTranscript(url):
    id = url[url.index("v=")+2:]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript


if __name__ == "__main__":
    yt.run()