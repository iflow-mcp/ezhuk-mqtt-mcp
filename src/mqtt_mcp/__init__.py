from importlib.metadata import version

from mqtt_mcp.server import MQTTMCP


try:
    __version__ = version("iflow-mcp_ezhuk_mqtt-mcp")
except:
    __version__ = "0.2.7"
__all__ = ["MQTTMCP"]
