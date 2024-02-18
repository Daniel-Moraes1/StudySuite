from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
from Agents.protocol import Empty
home_proto= Protocol("", version="0.1")

@home_proto.on_event("startup")
async def welcome(ctx: Context):
    ctx.logger.info(f"Welcome to {ctx.name}! My purpose is to help you study.")
    ctx.logger.info(f"Currently, you can generate quizzes and summaries from videos to check and improve your understanding!")
    ctx.logger.info(f"Would you like to start by generating a quiz or a summary?")

@home_proto.on_message(model=Empty)
async def welcome(ctx: Context, sender: str, req:Empty):
    try: 
        await ctx.send("Welcome to {ctx.name}! My purpose is to help you study.\nCurrently, you can generate quizzes and summaries from videos to check and improve your understanding!\n")
    except Exception as exc:
        ctx.logger.error(exc)
        await ctx.send(
            sender, UAgentResponse(
                message=str(exc), 
                type=UAgentResponseType.ERROR
            )
        )

@home_proto.on_message(model=QuizParams, replies={UAgentResponse})
async def handle_generate_quiz(ctx: Context, sender: str, req:QuizParams):
    ctx.logger.info(f"Received message from {sender}")
    student_grade = grade_answers(req.questions, req.answers)
    try:
        ctx.logger.info(f"Got message from {sender}: {req.questions}")
        ctx.logger.info(f"Got message from {sender}: {req.answers}")
        await ctx.send(
            sender,
            UAgentResponse(
                message=student_grade, 
                type=UAgentResponseType.FINAL
            ),
        )
    except Exception as exc:
        ctx.logger.error(exc)
        await ctx.send(
            sender, UAgentResponse(
                message=str(exc), 
                type=UAgentResponseType.ERROR
            )
        )

@home_proto.on_message(model=summaryResponse, replies={UAgentResponse})
async def handle_generate_summary(ctx: Context, sender: str, req:summaryResponse):
    ctx.logger.info(f"Received message from {sender}")
    try:
        ctx.logger.info(f"Got message from {sender}: {req.summary}")
        await ctx.send(
            sender,
            UAgentResponse(
                message=req.summary, 
                type=UAgentResponseType.FINAL
            ),
        )
    except Exception as exc:
        ctx.logger.error(exc)
        await ctx.send(
            sender, UAgentResponse(
                message=str(exc), 
                type=UAgentResponseType.ERROR
            )
        )
