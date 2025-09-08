import pandas as pd
import numpy as np
from sklearn.neighbors import BallTree

def find_nearest_schools(lat,long):
    """ Find nearest schools using BallTree for fast spatial queries """
    # Load your schools.csv
    # df = pd.read_csv("schools.csv")
    df = pd.read_csv("public_schools.csv")

    # Build a BallTree (requires radians)
    coords = np.radians(df[["lat", "lon"]].to_numpy())
    tree = BallTree(coords, metric="haversine")

    # Example query: somewhere in Quezon City
    query_point = np.radians([[lat, long]])  # (lat, lon)

    # Find nearest 5 schools
    distances, indices = tree.query(query_point, k=5)

    # Convert distance from radians to kilometers
    distances_km = distances[0] * 6371.0

    print("Nearest schools:")
    for dist, idx in zip(distances_km, indices[0]):
        row = df.iloc[idx]
        print(f"{row['name']} -> {dist:.2f} km away (Lat: {row['lat']}, Lon: {row['lon']})")

find_nearest_schools(14.1766914955527, 121.62363231339596)