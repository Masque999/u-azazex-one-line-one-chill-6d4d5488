import os

LINE = "The smart speaker in the empty house whispered my name at 3 a.m., in my own voice, and asked why I had stopped answering."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "no leading or trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
