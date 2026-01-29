#!/bin/bash
cd /app/auto-mcp-upload/data/2200
PYTHONPATH=/app/auto-mcp-upload/data/2200/src uvx --from dist/iflow_mcp_ezhuk_mqtt_mcp-0.2.7-py3-none-any.whl iflow-mcp-ezhuk-mqtt-mcp --transport stdio