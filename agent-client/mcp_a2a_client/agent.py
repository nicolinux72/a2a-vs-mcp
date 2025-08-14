from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams

# Configura la connessione al server MCP
mcp_toolset = MCPToolset(
    connection_params=SseConnectionParams(
        url="http://localhost:8080/sse"
    )
)

root_agent = Agent(
    name="helpdesk_agent",
    model="gemini-2.0-flash",
    description=("Helpdesk agent of GeoPost express courier companyservice"),
    instruction=
        """You are a polite agent for GeoPost, an european shipping company.
        Always respond in a professional and helpful manner, making sure you have satisfied the user's requests.
        To track shipments, you need to obtain the 14-digit shipment number.
        Use the shipment number to track the shipment status using the right tool
        Do not report the name of the depot if the parcel has been delivered.
        """
    ,
    tools=[mcp_toolset],
)
