import os
import urllib.request
import warnings
from typing import Dict, List
warnings.filterwarnings("ignore")
import geopandas as gpd
import matplotlib.pyplot as plt



class CSP:
    def __init__(self, variables, domains):
        self.variables = variables          #list of districts
        self.domains = domains              #colors for each district
        self.constraints = {v: [] for v in variables}

    def add_constraint(self, var1, var2):
        self.constraints[var1].append(var2)
        self.constraints[var2].append(var1)

    def is_valid(self, var, color, assignment):
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        for var in self.variables:
            if var not in assignment:
                current = var
                break

        for color in self.domains[current]:
            if self.is_valid(current, color, assignment):
                assignment[current] = color

                result = self.backtrack(assignment)
                if result:
                    return result

                del assignment[current]

        return None


#Downloading map of telangana
def download_map(file):
    url = "https://raw.githubusercontent.com/gggodhwani/telangana_boundaries/master/districts.json"
    if not os.path.exists(file):
        urllib.request.urlretrieve(url, file)


def main():
    file = "telangana.geojson"
    download_map(file)

    gdf = gpd.read_file(file)

    name_col = None
    for col in gdf.columns:
        if col.lower() in ["district", "name", "dtname"]:
            name_col = col
            break

    if not name_col:
        name_col = [c for c in gdf.columns if c != 'geometry'][0]

    districts = gdf[name_col].tolist()

    #Color choices
    colors = ["#00FF2F", "#0D00FF", "#FFE600", "#FF0000"]

    domains = {d: colors for d in districts}

  
    csp = CSP(districts, domains)


    added = set()

    for i, row1 in gdf.iterrows():
        d1 = row1[name_col]
        g1 = row1.geometry

        for j, row2 in gdf.iterrows():
            if j <= i:
                continue

            d2 = row2[name_col]
            g2 = row2.geometry

            if g1.touches(g2) or g1.intersects(g2):
                pair = tuple(sorted([d1, d2]))
                if pair not in added:
                    csp.add_constraint(d1, d2)
                    added.add(pair)

    solution = csp.backtrack({})

    if not solution:
        print("No solution found")
        return

    print("Solution found!")

    #Assign colors to map
    gdf["color"] = gdf[name_col].map(solution)

    print("Drawing map...")

    fig, ax = plt.subplots(figsize=(12, 12))
    gdf.plot(color=gdf["color"], edgecolor="black", linewidth=0.5, ax=ax)

    #label districts
    for x, y, name in zip(gdf.geometry.centroid.x,
                          gdf.geometry.centroid.y,
                          gdf[name_col]):
        ax.text(x, y, name, fontsize=7, ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

    plt.title("Telangana Map Coloring")
    plt.axis("off")

    plt.show()



main()