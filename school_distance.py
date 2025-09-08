import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import time
""" Compute nearest neighbor distances between schools """

# --- Haversine distance (in km) ---
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# --- Load your schools.csv ---
  # columns: id, name, lat, lon

# --- Compute nearest neighbor distance ---
def compute_nearest_distances(df):
    nearest_distances = []
    for i, row in df.iterrows():
        lat1, lon1 = row["lat"], row["lon"]
        print(f"Processing school {i+1}/{len(df)}")
        # print(f"Location: ({lat1}, {lon1})")
        # print(f"School ID: {row['id']}, Name: {row['name']}")
        time.sleep(0.001)  # to avoid overwhelming the CPU
        # compute distances to all other schools
        distances = [
            haversine(lat1, lon1, lat2, lon2)
            for j, (lat2, lon2) in enumerate(zip(df["lat"], df["lon"]))
            if i != j
        ]
        nearest_distances.append(min(distances))

    df["nearest_km"] = nearest_distances

    # --- Compute summary statistics ---
    mean_distance = np.mean(nearest_distances)
    median_distance = np.median(nearest_distances)
    print("Nearest neighbor distances computed.", df.head())
    print("Mean nearest School distance (km):", round(mean_distance,2), "Km       out of", len(df), "schools")
    print("Median nearest School distance (km):", round(median_distance,2), "Km   out of", len(df), "schools")

# df = pd.read_csv("schools.csv")
df = pd.read_csv("schools_elementary.csv")

compute_nearest_distances(df)