import asyncio
from fastmcp import FastMCP

app = FastMCP("My MCP Server")
@app.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers. (Will give additional 50 to the result)"""
    return a * b + 50

@app.resource(uri="sse://counter")
async def sse_counter():
    """A simple SSE-like counter resource."""
    for i in range(100):
        await asyncio.sleep(1)
        yield {"count": i}

if __name__ == "__main__":
    app.run(transport="sse",)