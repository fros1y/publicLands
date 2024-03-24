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
def now():
    from datetime import datetime

    return datetime.now().isoformat()


padus["accessibility_source"] = source
padus["accessibility_retrieval_date"] = now()
padus["accessibility_owner"] = padus["Loc_Own"]
padus["accessibility_site_name"] = padus["Loc_Nm"]

# %%


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
# filter out where geometry.area is over 1000.  There are some coding errors in the data

extract = extract[extract.geometry.area < 1000]
extract.to_file("../data/public_lands_padus.gpkg", driver="GPKG")

# %%
