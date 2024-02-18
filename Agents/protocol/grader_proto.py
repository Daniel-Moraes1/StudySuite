from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
from .protocol_models import QuizParams

grader_proto = Protocol("Quiz Generator", version="0.1")

def grade_answers(questions, answers):
    return "congratulations all your answers are correct!"

@grader_proto.on_message(model=QuizParams, replies={UAgentResponse})
async def handle_generate_quiz(ctx: Context, sender: str, req:QuizParams):
    ctx.logger.info(f"Received message from {sender}")
    student_grade = grade_answers(req.questions, req.answers)
    try:
        ctx.logger.info(f"Got message from {sender}: {req.questions}")
        ctx.logger.info(f"Got message from {sender}: {req.answers}")
        await ctx.send(
            sender,
            UAgentResponse(
                options=[],
                message=student_grade, 
                type=UAgentResponseType.SELECT_FROM_OPTIONS
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

