from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
from .protocol_models import Empty, QuizParams

def grade_answers(answers, responses):
    wrong = 0
    for i in range(len(answers)):
        if answers[i] != responses[i]:
            wrong+=1
    return round((len(answers) - wrong)/len(answers)*100, 2)

home_proto = Protocol("Study Suite Welcome", version="0.1")

# @home_proto.on_message(model=Empty, replies={UAgentResponse})
# async def welcome(ctx: Context, sender: str, req:Empty):
#     try: 
#         message = "Welcome to {ctx.name}! My purpose is to help you study.\nCurrently, you can generate quizzes and summaries from videos to check and improve your understanding!\n"
#         await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.SELECT_FROM_OPTIONS, options=[]))
#     except Exception as exc:
#         ctx.logger.error(exc)
#         await ctx.send(
#             sender, UAgentResponse(
#                 message=str(exc), 
#                 type=UAgentResponseType.ERROR
#             )
#         )

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

# @home_proto.on_message(model=summaryResponse, replies={UAgentResponse})
# async def handle_generate_summary(ctx: Context, sender: str, req:summaryResponse):
#     ctx.logger.info(f"Received message from {sender}")
#     try:
#         ctx.logger.info(f"Got message from {sender}: {req.summary}")
#         await ctx.send(
#             sender,
#             UAgentResponse(
#                 message=req.summary, 
#                 type=UAgentResponseType.FINAL
#             ),
#         )
#     except Exception as exc:
#         ctx.logger.error(exc)
#         await ctx.send(
#             sender, UAgentResponse(
#                 message=str(exc), 
#                 type=UAgentResponseType.ERROR
#             )
#         )
