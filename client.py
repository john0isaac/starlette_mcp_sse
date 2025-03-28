from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            # Initialize the connection
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", tools)
            # List prompts
            prompts = await session.list_prompts()
            print("Prompts:", prompts)

            # Call a tool
            result = await session.call_tool("get_alerts", arguments={"state": "CA"})
            print("Tool result:", result.content[0].text)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())