#!/usr/bin/env python3
"""
MCPツールのテストスクリプト
"""

from server import (
    count_characters,
    generate_hash,
    base64_encode,
    base64_decode,
    extract_urls,
    format_json,
    generate_timestamp,
    remove_duplicates
)

def test_all_tools():
    print("🧪 Text Tools MCPのテスト開始\n")
    
    # 1. 文字数カウント
    print("1️⃣ 文字数カウント:")
    text = "Hello World!\nこんにちは世界！"
    result = count_characters(text)
    print(f"  入力: '{text}'")
    print(f"  結果: {result}\n")
    
    # 2. ハッシュ生成
    print("2️⃣ ハッシュ生成:")
    result = generate_hash("Hello", "sha256")
    print(f"  入力: 'Hello'")
    print(f"  SHA256: {result['hash']}\n")
    
    # 3. Base64エンコード/デコード
    print("3️⃣ Base64エンコード/デコード:")
    encoded = base64_encode("テスト")
    print(f"  エンコード: {encoded}")
    decoded = base64_decode(encoded['encoded'])
    print(f"  デコード: {decoded}\n")
    
    # 4. URL抽出
    print("4️⃣ URL抽出:")
    text_with_urls = "Check out https://github.com and https://google.com"
    result = extract_urls(text_with_urls)
    print(f"  入力: '{text_with_urls}'")
    print(f"  抽出されたURL: {result}\n")
    
    # 5. JSON整形
    print("5️⃣ JSON整形:")
    ugly_json = '{"name":"太郎","age":20,"city":"東京"}'
    result = format_json(ugly_json)
    print(f"  整形前: {ugly_json}")
    print(f"  整形後:\n{result['formatted']}\n")
    
    # 6. タイムスタンプ生成
    print("6️⃣ タイムスタンプ生成:")
    for fmt in ["iso", "unix", "japanese", "filename"]:
        result = generate_timestamp(fmt)
        print(f"  {fmt}: {result['timestamp']}")
    print()
    
    # 7. 重複削除
    print("7️⃣ 重複行削除:")
    text_with_dupes = "apple\nbanana\napple\norange\nbanana"
    result = remove_duplicates(text_with_dupes)
    print(f"  入力: {text_with_dupes.replace(chr(10), ', ')}")
    print(f"  結果: {result['result'].replace(chr(10), ', ')}")
    print(f"  削除数: {result['removed_count']}\n")
    
    print("✅ すべてのテスト完了！")

if __name__ == "__main__":
    test_all_tools()