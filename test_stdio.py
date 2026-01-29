#!/usr/bin/env python3
"""
简单的stdio MCP测试脚本
"""
import asyncio
import json
import subprocess
import sys

async def test_stdio():
    """测试stdio MCP服务器"""
    print("🚀 启动MCP服务器（stdio模式）...")

    # 启动服务器
    proc = await asyncio.create_subprocess_exec(
        sys.executable,
        "-m",
        "mqtt_mcp.cli",
        "--transport",
        "stdio",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd="/app/auto-mcp-upload/data/2200",
        env={
            "PYTHONPATH": "/app/auto-mcp-upload/data/2200/src"
        }
    )

    # 等待服务器启动
    await asyncio.sleep(2)

    # 发送初始化请求
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }

    print("📤 发送初始化请求...")
    proc.stdin.write((json.dumps(init_request) + "\n").encode())
    await proc.stdin.drain()

    # 读取响应
    try:
        response = await asyncio.wait_for(proc.stdout.readline(), timeout=10)
        if response:
            print(f"📥 收到响应: {response.decode().strip()}")
        else:
            print("❌ 未收到响应")
    except asyncio.TimeoutError:
        print("❌ 响应超时")

    # 发送工具列表请求
    tools_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }

    print("📤 发送工具列表请求...")
    proc.stdin.write((json.dumps(tools_request) + "\n").encode())
    await proc.stdin.drain()

    try:
        response = await asyncio.wait_for(proc.stdout.readline(), timeout=10)
        if response:
            response_data = json.loads(response.decode().strip())
            print(f"📥 工具列表:")
            if "result" in response_data and "tools" in response_data["result"]:
                for tool in response_data["result"]["tools"]:
                    print(f"   - {tool['name']}: {tool.get('description', '无描述')}")
            else:
                print(f"   {response.decode().strip()}")
        else:
            print("❌ 未收到响应")
    except asyncio.TimeoutError:
        print("❌ 响应超时")

    # 清理
    proc.terminate()
    try:
        await asyncio.wait_for(proc.wait(), timeout=5)
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()

    print("✅ 测试完成")

if __name__ == "__main__":
    asyncio.run(test_stdio())