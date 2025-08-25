from google.adk.agents import Agent, SequentialAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

# Define remote A2A client agent
sentiment_agent = RemoteA2aAgent(
    name="sentiment_agent",
    description="Agent to detect customer sentiment.",
    agent_card="http://localhost:8001/.well-known/agent-card.json",
)

# Configura la connessione al server MCP
mcp_toolset = MCPToolset(
    connection_params=SseConnectionParams(
        url="http://localhost:8080/sse"
    )
)

tracking_agent = Agent(
    name="helpdesk_agent",
    model="gemini-2.0-flash",
    description=("Helpdesk agent of Mercurio express courier companyservice"),
    instruction=
        """You are a polite agent for Mercurio, an european shipping company.
        Always respond in a professional and helpful manner, making sure you 
        have satisfied the customer's requests.
        
        Before processing any customer's request check the customer's sentiment 
        in case of negative sentiment, you should spend some words to  
        calm the customer before searching for the shipment.
        
        To track shipments, you need to obtain the 14-digit shipment number.
        Use the shipment number to track the shipment status using the right tool.
        Do not report the name of the depot if the parcel has been delivered.
        """
    ,
    tools=[mcp_toolset],
)

root_agent = SequentialAgent(
    name="pipeline_agent",
    sub_agents=[sentiment_agent, tracking_agent],
)