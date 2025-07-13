# Text Tools MCP Server

シンプルで実用的なテキスト処理ツール集のMCPサーバーです。

## 機能

- 文字数カウント
- ハッシュ生成（MD5, SHA1, SHA256, SHA512）
- Base64エンコード/デコード
- URL抽出
- JSON整形
- タイムスタンプ生成
- テキスト差分検出
- 重複行削除

## インストール（どのPCでも3ステップ）

### 1. リポジトリをクローン
```bash
git clone https://github.com/muumuu8181/text-tools-mcp.git
cd text-tools-mcp
```

### 2. 依存関係をインストール
```bash
pip install -r requirements.txt
```

### 3. Claude Desktopに設定を追加

#### Windows
`%APPDATA%\Claude\claude_desktop_config.json` を編集:

#### Mac/Linux
`~/.config/Claude/claude_desktop_config.json` を編集:

```json
{
  "mcpServers": {
    "text-tools": {
      "command": "python",
      "args": ["/path/to/text-tools-mcp/server.py"]
    }
  }
}
```

**注意**: `/path/to/` を実際のパスに置き換えてください。

## 使い方

Claude Desktopを再起動すると、以下のように使えます：

```
「このテキストの文字数を数えて」
「このJSONを整形して」
「SHA256ハッシュを生成して」
「重複行を削除して」
```

## 開発

新しいツールを追加する場合：

```python
@mcp.tool()
def your_new_tool(param: str) -> dict:
    """ツールの説明"""
    # 処理
    return {"result": "..."}
```

## ライセンス

MIT