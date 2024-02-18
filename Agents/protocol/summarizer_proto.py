from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType


# the summarizer protocol will perform as a subtask that returns information 


@grader_proto.on_message(model=summaryRequest, replies=summaryResponse)
async def handle_query_request(ctx:Context, sender:str, msg:summaryRequest):
    url = msg.url
    transcript = getTranscript(msg.url)
    summary = generateSummary(url)


def generateSummary(url):
    pass