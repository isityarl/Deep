import re
import pandas as pd


def parse_emoji_zwj(file_path):
    emoji_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or "group:" in line or "subgroup:" in line:
                continue

            match = re.match(
                r"([\dA-F\s]+)\s*;\s*RGI_Emoji_ZWJ_Sequence\s*;\s*([^#]+)\s*#\s*E[\d.]+\s*\[\d+\]\s*\((.+)\)", line)

            if match:
                code_points, description, emoji_char = match.groups()

                emoji_data.append({
                    "emoji": emoji_char,
                    "code_points": code_points,
                    "description": description.strip(),
                })

    return pd.DataFrame(emoji_data)

file_path = "3.txt"

emoji_zwj_df = parse_emoji_zwj(file_path)

emoji_zwj_df.to_csv("3.csv", index=False, encoding="utf-8")

print(emoji_zwj_df.head())
