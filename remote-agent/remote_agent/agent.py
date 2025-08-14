from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

# Load environment variables from .env file
load_dotenv()

root_agent = Agent(
    name="sentiment_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for sentiment analysis that evaluates the emotional tone of text on a scale from 1 (friendly) to 5 (furious).",
    instruction="""
        You are a sentiment analysis agent.
        Read the provided text and return only a JSON object:
        {"sentiment_level": n}
        where n is an integer between 1 (friendly) and 5 (furious).
    """

)

# Crea l'app A2A e serve l'agente su uvicorn
a2a_app = to_a2a(root_agent, port=8001)

# poetry run uvicorn a2a_agent.agent:a2a_app --host localhost --port 8001