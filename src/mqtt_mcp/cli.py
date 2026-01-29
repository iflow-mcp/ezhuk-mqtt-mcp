import asyncio
import typer

from mqtt_mcp.server import MQTTMCP


app = typer.Typer(
    name="mqtt-mcp",
    help="MQTTMCP CLI",
)


@app.command()
def run(
    transport: str = typer.Option("stdio", help="Transport protocol: stdio or http")
):
    server = MQTTMCP()
    asyncio.run(server.run_async(transport=transport))