# OpenMetadata Google Agent

This repository is an exemplary implementation of an LLM agent that demonstrates the usage of the OpenMetadata MCP server.

## Running the Agent from `src` Using Google ADK

### Prerequisites

Ensure the following before running the agent:
- All dependencies are installed.
- You are in the correct directory.
- Environment variables set in `src/.env`:
- `OM_JWT_TOKEN` 
- `OM_URL` 
- `GOOGLE_API_KEY` (can be obtained from Google AI Studio with free tier usage)

### Running the agent

To run the agent, use the following command in root directory of this repository:

```sh
uv run adk web
```

and select `src` from agent list.