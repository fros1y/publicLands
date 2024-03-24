# %%
import geopandas as gpd
import pandas as pd

# %%
public_lands_ri_local = gpd.read_file("https://data.rigis.org/env/locCons18.zip")

# %%
from accessibility import Accessibility


def normalize_accessibility(accessibility):
    if accessibility == "YES":
        return Accessibility.OPEN
    elif accessibility == "NO":
        return Accessibility.CLOSED
    elif accessibility == "LIM":
        return Accessibility.LIMITED
    else:
        return None


public_lands_ri_local["accessibility"] = public_lands_ri_local["PUBACC"].apply(
    lambda x: str(normalize_accessibility(x))
)

# %%
public_lands_ri_local["accessibility_site_name"] = (
    public_lands_ri_local["Com_Name"] + " - " + public_lands_ri_local["Site"]
)
public_lands_ri_local["accessibility_owner"] = public_lands_ri_local["Fee_Own"]


public_lands_ri_local["accessibility_source"] = (
    "https://www.rigis.org/datasets/edc::local-conservation-areas/about"
)
public_lands_ri_local["accessibility_retrieval_date"] = "2024-03-24"

# %%

# https://www.rigis.org/datasets/edc::state-conservation-areas/explore

public_lands_ri_state = gpd.read_file("https://data.rigis.org/env/staCons18.zip")

# %%
public_lands_ri_state["accessibility"] = public_lands_ri_state["Pub_Access"].apply(
    lambda x: str(normalize_accessibility(x))
)
# %%
# set the accessilibility_site_name by joining the "NAME" and "DEM_AREA" columns with a " - "
public_lands_ri_state["accessibility_site_name"] = (
    public_lands_ri_state["NAME"] + " - " + public_lands_ri_state["DEM_AREA"]
)

# %%
public_lands_ri_state["accessibility_owner"] = "State of Rhode Island"
public_lands_ri_state["accessibility_source"] = (
    "https://www.rigis.org/datasets/edc::state-conservation-areas/about"
)
public_lands_ri_state["accessibility_retrieval_date"] = "2024-03-24"

# %%

# Merge the two dataframes
public_lands_ri = gpd.GeoDataFrame(
    pd.concat([public_lands_ri_local, public_lands_ri_state])
)

# %%
extract = public_lands_ri[
    [
        "accessibility_site_name",
        "accessibility_owner",
        "accessibility_source",
        "accessibility_retrieval_date",
        "accessibility",
        "geometry",
    ]
]

extract.to_file("../data/public_lands_ri.gpkg", driver="GPKG")

# %%
