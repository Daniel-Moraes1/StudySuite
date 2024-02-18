from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
from .protocol_models import *


# the summarizer protocol will perform as a subtask that returns information 
summarizer_proto = Protocol("Summarizer Protocol", version="0.1")


@summarizer_proto.on_message(model=summaryRequest, replies=summaryResponse)
async def handle_query_request(ctx:Context, sender:str, msg:summaryRequest):
    url = msg.url
    transcript = getTranscript(msg.url)
    summary = generateSummary(url)


def generateSummary(url):
    pass