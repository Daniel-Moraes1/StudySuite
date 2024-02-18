from uagents import Agent, Context, Model, Protocol, Bureau
from uagents.setup import fund_agent_if_low
from youtube_transcript_api import YouTubeTranscriptApi


user = Agent(name="userAgent", 
            seed="userAgent")

class Begin(Model):
    url: str


@user.on_interval(5)
async def interval_task(ctx: Context):
    ctx.logger.info("User executing periodic task...")

@user.on_message(model=Begin)
async def handle_message(ctx: Context, sender: str, msg: Begin):
    transcript = getTranscript(msg.url)
    quiz = generateQuiz(transcript)

    ctx.logger.info(f"Got message from {sender}: {url}")

    
    if response.status_code == 200:
        ctx.logger.info(f"Got message from {sender}: {url}")

    else:
        return None
    

def getTranscript(url):
    id = url[url.index("v=")+2:]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript

def generateQuiz(transcript)

    


if __name__ == "__main__":
    yt.run()