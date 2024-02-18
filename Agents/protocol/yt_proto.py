from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
from youtube_transcript_api import YouTubeTranscriptApi

yt_proto = Protocol("ProcessYT", "1.1")

class Message(Model):
    # defines the request model. information needed for the video
    string_field: str



def getTranscript(url) -> str:
    id = url[url.index("v=")+2:]
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return str(transcript)



@yt_proto.on_message(model=Message, replies={UAgentResponse})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}")
    try:
        transcript = getTranscript(msg.string_field)
        print(transcript)
        ctx.logger.info(f"Got message from {sender}: {msg.string_field}")
        await ctx.send(
            sender,
            UAgentResponse(
                message=transcript,
                type=UAgentResponseType.FINAL
            ),
        )
        
    except Exception as exc:
        ctx.logger.error(exc)
        await ctx.send(
            sender, UAgentResponse(message=str(exc), type=UAgentResponseType.ERROR)
        )
