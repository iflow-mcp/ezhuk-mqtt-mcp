#!/usr/bin/env python3
"""
MCP服务器包装脚本
"""
import sys
import os

# 添加src到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mqtt_mcp.cli import app

if __name__ == "__main__":
    app()