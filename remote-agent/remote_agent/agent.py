from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH

# Load environment variables from .env file
load_dotenv()


class Response(BaseModel):
    costumer_request: str = Field(description="the original customer request")
    hostility_degree: int = Field(description="the hostility tone of user request on a scale from 1 (friendly) to 10 (furious)")

root_agent = Agent(
    name="sentiment_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for sentiment analysis that evaluates the hostility "
                "tone of user request on a scale from 1 (friendly) to 10 (furious).",
    instruction="""
        You are a sentiment analysis agent.         
    """,
    output_schema=Response,
)

# Crea l'app A2A e serve l'agente su uvicorn
a2a_app = to_a2a(root_agent, port=8001)
