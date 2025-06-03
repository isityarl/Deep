import re
import pandas as pd


def parse_emoji_test(file_path):
    emoji_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or "group:" in line or "subgroup:" in line:
                continue

            match = re.match(r"([\dA-F\s]+)\s*;\s*([\w-]+)\s*#\s*(\S+)\s*E[\d.]+\s*(.*)", line)

            if match:
                code_points, status, emoji, name = match.groups()

                emoji_char = ''.join(chr(int(cp, 16)) for cp in code_points.split())

                emoji_data.append({
                    "emoji": emoji_char,
                    "code_points": code_points,
                    "status": status,
                    "name": name.strip(),
                })

    return pd.DataFrame(emoji_data)


file_path = "2.txt"

emoji_df = parse_emoji_test(file_path)

emoji_df.to_csv("2.csv", index=False, encoding="utf-8")

print(emoji_df.head())