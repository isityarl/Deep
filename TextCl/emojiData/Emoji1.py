import re
import pandas as pd


def parse_emoji_sequences(file_path):
    emoji_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            match = re.match(r"([\dA-F\s]+)\s*;\s*(\w+)\s*;\s*(.*?)\s*#", line)

            if match:
                code_points, category, description = match.groups()

                # Convert hex code points to actual emoji
                emoji = ''.join(chr(int(cp, 16)) for cp in code_points.split())

                emoji_data.append({
                    "emoji": emoji,
                    "code_points": code_points,
                    "category": category,
                    "description": description.strip(),
                })

    return pd.DataFrame(emoji_data)


file_path = "1.txt"

emoji_df = parse_emoji_sequences(file_path)

emoji_df.to_csv("1.csv", index=False, encoding="utf-8")

print(emoji_df.head())
