from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

# Load environment variables from .env file
load_dotenv()

root_agent = Agent(
    name="sentiment_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for sentiment analysis that evaluates the hostility "
                "tone of user request on a scale from 1 (friendly) to 10 (furious).",
    instruction="""
        You are a sentiment analysis agent. 
        Read the provided customer request and return *only* a JSON object
        like the following:
        {   
            "costumer_request": "the original customer request",
            "hostility_degree": n
        }
        Where n is an integer between 1 (friendly) and 10 (furious).
    """
)

# Crea l'app A2A e serve l'agente su uvicorn
a2a_app = to_a2a(root_agent, port=8001)
