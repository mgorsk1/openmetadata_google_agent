from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    SseServerParams,
)
import os
from rich import print
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("OM_JWT_TOKEN")
om_url = os.getenv("OM_URL")


async def get_tools_async():
    """Gets tools from the File System MCP Server."""
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(
            url=f"{om_url}/mcp/sse", headers={"Authorization": f"Bearer {token}"}
        )
    )
    print("MCP Toolset created successfully.")
    return tools, exit_stack


# can you get me full impact analysis on sample_data.ecommerce_db.shopify.raw_customer table?
async def get_agent_async():
    """Creates an ADK Agent equipped with tools from the MCP Server."""
    tools, exit_stack = await get_tools_async()
    print(f"Fetched {len(tools)} tools from MCP server.")
    module_dir = os.path.dirname(os.path.abspath(__file__))
    instruction_path = os.path.join(module_dir, "../resources/agent_prompt.txt")
    agent = LlmAgent(
        model="gemini-2.5-flash-preview-05-20",
        name="metadata_assistant",
        instruction=open(instruction_path, "r").read().strip(),
        tools=tools,
    )

    return agent, exit_stack


root_agent = get_agent_async()
