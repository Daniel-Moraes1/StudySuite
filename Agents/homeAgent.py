from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from protocol import home_proto

#AGENT_MAILBOX_KEY = "83342e4b-18c6-4d93-bcb6-bc958de3fd13"
AGENT_MAILBOX_KEY = "ababf13b-88fd-4fc9-ad8d-a5b2289b3784"

home = Agent(name="StudySuite",
            seed="StudySuite",
            mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
            port=8001,
            endpoint=["http://localhost:8001/welcome"]
            )

fund_agent_if_low(home.wallet.address())

if __name__ == "__main__":
    home.include(home_proto, publish_manifest=True)
    home.run()
