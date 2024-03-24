# %%
import geopandas as gpd
import esri2gpd
from accessibility import Accessibility

# %%
source = (
    "https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-download"
)
# %%
padus = gpd.read_file("../data/PADUS3_0Geopackage.gpkg")
# %%

padus["accessibility_source"] = source
padus["accessibility_retrieval_date"] = "2024-03-24"
padus["accessibility_owner"] = padus["Loc_Own"]
padus["accessibility_site_name"] = padus["Loc_Nm"]


# %%
def normalize_accessibility(accessibility):
    lookup_table = {
        "OA": Accessibility.OPEN,
        "RA": Accessibility.LIMITED,
        "XA": Accessibility.CLOSED,
        "UK": Accessibility.UNKNOWN,
    }
    return lookup_table.get(accessibility, None)


# %%
padus["accessibility"] = padus["Pub_Access"].apply(
    lambda x: str(normalize_accessibility(x))
)

# %%
extract = padus[
    [
        "accessibility_site_name",
        "accessibility_owner",
        "accessibility_source",
        "accessibility_retrieval_date",
        "accessibility",
        "geometry",
    ]
]
extract.to_file("../data/public_lands_padus.gpkg", driver="GPKG")

# %%
