import json

with open("users.json", "r") as f:
	text = json.load(f)
	print(text)