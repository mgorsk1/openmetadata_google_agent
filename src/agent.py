from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    SseServerParams,
)
import os
from dotenv import load_dotenv
from .prompt import DATA_GOVERNANCE_EXPERT_PROMPT  # Import prompt

load_dotenv()

token = os.getenv("OM_JWT_TOKEN")
om_url = os.getenv("OM_URL")

root_agent = LlmAgent(
    model="gemini-2.5-flash-preview-05-20",
    name="metadata_assistant",
    instruction=DATA_GOVERNANCE_EXPERT_PROMPT,
    tools=[
        MCPToolset(
            connection_params=SseServerParams(
                url=f"{om_url}/mcp/sse", headers={"Authorization": f"Bearer {token}"}
            )
        )
    ],
)
