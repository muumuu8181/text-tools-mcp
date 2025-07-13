#!/usr/bin/env python3
"""
Text Tools MCP Server
簡単で実用的なテキスト処理ツール集
"""

from fastmcp import FastMCP
import hashlib
import base64
import re
from datetime import datetime
import json

# MCPサーバーの初期化
mcp = FastMCP("text-tools")

@mcp.tool()
def count_characters(text: str, include_spaces: bool = True) -> dict:
    """テキストの文字数をカウント"""
    if include_spaces:
        total = len(text)
    else:
        total = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    
    return {
        "total_characters": total,
        "total_with_spaces": len(text),
        "lines": len(text.splitlines()),
        "words": len(text.split())
    }

@mcp.tool()
def generate_hash(text: str, algorithm: str = "sha256") -> dict:
    """テキストのハッシュ値を生成"""
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }
    
    if algorithm not in algorithms:
        return {"error": f"サポートされていないアルゴリズム: {algorithm}"}
    
    hash_obj = algorithms[algorithm](text.encode('utf-8'))
    return {
        "algorithm": algorithm,
        "hash": hash_obj.hexdigest(),
        "input_length": len(text)
    }

@mcp.tool()
def base64_encode(text: str) -> dict:
    """テキストをBase64エンコード"""
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return {
        "encoded": encoded,
        "original_length": len(text),
        "encoded_length": len(encoded)
    }

@mcp.tool()
def base64_decode(encoded_text: str) -> dict:
    """Base64テキストをデコード"""
    try:
        decoded = base64.b64decode(encoded_text).decode('utf-8')
        return {
            "decoded": decoded,
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }

@mcp.tool()
def extract_urls(text: str) -> dict:
    """テキストからURLを抽出"""
    url_pattern = r'https?://[^\s<>"{}|\\^[\]`]+'
    urls = re.findall(url_pattern, text)
    return {
        "urls": urls,
        "count": len(urls)
    }

@mcp.tool()
def format_json(json_string: str, indent: int = 2) -> dict:
    """JSON文字列を整形"""
    try:
        parsed = json.loads(json_string)
        formatted = json.dumps(parsed, indent=indent, ensure_ascii=False)
        return {
            "formatted": formatted,
            "success": True
        }
    except json.JSONDecodeError as e:
        return {
            "error": str(e),
            "success": False
        }

@mcp.tool()
def generate_timestamp(format: str = "iso") -> dict:
    """現在のタイムスタンプを生成"""
    now = datetime.now()
    
    formats = {
        "iso": now.isoformat(),
        "unix": int(now.timestamp()),
        "japanese": now.strftime("%Y年%m月%d日 %H時%M分%S秒"),
        "us": now.strftime("%m/%d/%Y %I:%M:%S %p"),
        "filename": now.strftime("%Y%m%d_%H%M%S")
    }
    
    if format not in formats:
        return {
            "error": f"サポートされていないフォーマット: {format}",
            "supported_formats": list(formats.keys())
        }
    
    return {
        "timestamp": formats[format],
        "format": format,
        "timezone": "local"
    }

@mcp.tool()
def text_diff(text1: str, text2: str) -> dict:
    """2つのテキストの差分を検出"""
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    
    differences = []
    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
        if line1 != line2:
            differences.append({
                "line": i + 1,
                "text1": line1,
                "text2": line2
            })
    
    # 長さが違う場合の処理
    if len(lines1) > len(lines2):
        for i in range(len(lines2), len(lines1)):
            differences.append({
                "line": i + 1,
                "text1": lines1[i],
                "text2": "(なし)"
            })
    elif len(lines2) > len(lines1):
        for i in range(len(lines1), len(lines2)):
            differences.append({
                "line": i + 1,
                "text1": "(なし)",
                "text2": lines2[i]
            })
    
    return {
        "total_differences": len(differences),
        "differences": differences[:10],  # 最初の10個まで
        "lines_text1": len(lines1),
        "lines_text2": len(lines2)
    }

@mcp.tool()
def remove_duplicates(text: str, separator: str = "\n") -> dict:
    """重複行を削除"""
    lines = text.split(separator)
    unique_lines = list(dict.fromkeys(lines))  # 順序を保持
    
    return {
        "original_count": len(lines),
        "unique_count": len(unique_lines),
        "removed_count": len(lines) - len(unique_lines),
        "result": separator.join(unique_lines)
    }

if __name__ == "__main__":
    # サーバーを起動
    mcp.run()