from uagents import Agent
from uagents.setup import fund_agent_if_low
from protocol import grader_proto

AGENT_MAILBOX_KEY = "83342e4b-18c6-4d93-bcb6-bc958de3fd13"

grader = Agent(name="Quiz Grader",
            seed="Quiz Grader Agent",
            mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
            port=8001,
            endpoint=["http://localhost:8001/submit"])

print(f"agent name and addres: {grader.name} at {grader.address}")

fund_agent_if_low(grader.wallet.address())

grader.include(grader_proto, publish_manifest=True);

if __name__ == "__main__":
    grader.run()