import pandas as pd
from rapidfuzz import process

# Load your schools.csv
# df = pd.read_csv("schools.csv")
df = pd.read_csv("public_schools.csv")

# Your query (not exact, maybe a typo or partial name)
query = "Sampaloc"

# Use rapidfuzz to find the best matches in the "name" column
choices = df["name"].dropna().tolist()
matches = process.extract(query, choices, limit=5)  # top 5 matches

print("Top matches:")
for match in matches:
    name, score, idx = match
    row = df.iloc[idx]
    print(f"{name} (score: {score}) -> Lat: {row['lat']}, Lon: {row['lon']}")
