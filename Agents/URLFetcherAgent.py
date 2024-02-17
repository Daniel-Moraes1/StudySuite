from uagents import Agent, Context, Model, Protocol
from uagents.setup import fund_agent_if_low
from protocol import yt_proto
import requests

AGENT_MAILBOX_KEY = "3c1184b5-bf92-404a-9dfd-e77d01d23092"

yt = Agent(name="youtubeTranscriptGrabber",
            seed="youtube_transcript_grabber",
            mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
            port=8001,
            endpoint=["http://localhost:8001/submit"])

print(f"agent name and addres: {yt.name} at {yt.address}")

fund_agent_if_low(yt.wallet.address())

yt.include(yt_proto, publish_manifest=True);


# @yt.on_interval(5)
# async def interval_task(ctx: Context):
#     ctx.logger.info("Executing periodic task...")
#     ctx.send()

if __name__ == "__main__":
    yt.run()