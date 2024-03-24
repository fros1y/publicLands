# %%
import geopandas as gpd
import esri2gpd
from accessibility import Accessibility

# %%
source = "https://nhgeodata.unh.edu/nhgeodata/rest/services/EC/Conservation/MapServer/6"
nh_conservation = esri2gpd.get(source)
# %%
nh_conservation["accessibility_source"] = source
nh_conservation["accessibility_retrieval_date"] = "2024-03-24"
nh_conservation["accessibility_site_name"] = nh_conservation["P_NAME"]

# %%
# 1 Allowed (Minor use restrictions may apply, such as fees charged, vehicular
# access, etc.)
# 2 Restricted to Certain Areas (Access restricted to specific areas or times, or
# member/ resident use only.)
# 3 Not allowed
# 4 Unknown
# 5 No response to access survey received


def normalize_accessibility(accessibility):
    if accessibility == 1:
        return Accessibility.OPEN
    elif accessibility == 2:
        return Accessibility.LIMITED
    elif accessibility == 3:
        return Accessibility.CLOSED
    elif accessibility == 4:
        return Accessibility.UNKNOWN
    elif accessibility == 5:
        return Accessibility.UNKNOWN
    else:
        return Accessibility.UNKNOWN


nh_conservation["accessibility"] = nh_conservation["ACCESS"].apply(
    lambda x: normalize_accessibility(x)
)

# %%
extract = nh_conservation[
    [
        "accessibility_site_name",
        "accessibility_source",
        "accessibility_retrieval_date",
        "accessibility",
        "geometry",
    ]
]

# %%
extract.to_file("../data/public_lands_nh.gpkg", driver="GPKG")
# %%
