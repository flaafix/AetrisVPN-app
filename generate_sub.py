import struct, json, uuid, os

def write_entry(f, key, value_json):
    key_bytes = key.encode('utf-8')
    val_bytes = value_json.encode('utf-8')
    f.write(struct.pack('>I', len(key_bytes)))
    f.write(key_bytes)
    f.write(struct.pack('>I', len(val_bytes)))
    f.write(val_bytes)

subs = [
    ("ЧЁРНЫЕ СПИСКИ", "https://raw.githubusercontent.com/flaafix/AetrisVPN-black-list/refs/heads/main/configs.txt"),
    ("БЕЛЫЕ СПИСКИ", "https://raw.githubusercontent.com/flaafix/AetrisVPN-white-list-lite/refs/heads/main/AetrisVPN.txt"),
]

output_path = "V2rayNG/app/src/main/assets/mmkv/SUB"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'wb') as f:
    for remarks, url in subs:
        guid = uuid.uuid4().hex
        item = {
            "remarks": remarks,
            "url": url,
            "enabled": True,
            "addedTime": int(__import__('time').time() * 1000),
            "lastUpdated": -1,
            "autoUpdate": True,
            "updateInterval": None,
            "prevProfile": None,
            "nextProfile": None,
            "filter": "",
            "allowInsecureUrl": False,
            "userAgent": ""
        }
        write_entry(f, guid, json.dumps(item, ensure_ascii=False))
        print(f"Added: {remarks} -> {guid}")

print(f"\nSUB file generated at: {output_path}")
