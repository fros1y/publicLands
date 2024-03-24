# %%
import geopandas as gpd
import esri2gpd
from accessibility import Accessibility

# %%
url = "https://services1.arcgis.com/RbMX0mRVOFNTdLzd/arcgis/rest/services/Maine_Conserved_Lands_All/FeatureServer/0"
maine_conserved_lands = esri2gpd.get(url)

# %%
maine_conserved_lands["accessibility_source"] = url
maine_conserved_lands["accessibility_retrieval_date"] = "2024-03-24"
maine_conserved_lands["accessibility_owner"] = maine_conserved_lands["HOLD1_NAME"]
maine_conserved_lands["accessibility_site_name"] = (
    maine_conserved_lands["PROJECT"] + " - " + maine_conserved_lands["PARCEL_NAME"]
)


# %%
def normalize_accessibility(accessibility):
    lookup_table = {
        " ": Accessibility.UNKNOWN,
        "Allowed": Accessibility.OPEN,
        "Allowed for general use, contact owner for details: Restricted by time of year - seasonal use, wildl": Accessibility.LIMITED,
        "Allowed for general use, contact owner for details: Restricted by time of year - seasonal use, wildlife breeding seasons, environmental degradation during spring or wet season,": Accessibility.LIMITED,
        "Allowed for general use, contact owner for details: Restricted by type of activity": Accessibility.LIMITED,
        "Allowed for general use, contact owner for details: Restricted by type of activity - no ATV's, no sn": Accessibility.LIMITED,
        "Allowed for general use, contact owner for details: Restricted by type of activity - no ATV's, no snowmobiles, no mountain bikes, no overnight camping, no hunting,": Accessibility.LIMITED,
        "Allowed for general uses, contact owner for details: Certain restrictions may apply - time, activity": Accessibility.LIMITED,
        "Allowed for general uses, contact owner for details: Certain restrictions may apply - time, activity,": Accessibility.LIMITED,
        "Allowed for general uses, contact owner for details: Certain restrictions may apply - time,activity,": Accessibility.LIMITED,
        "Allowed for general uses, contact owner for detials: Certain restrictions may apply - time, acitvity": Accessibility.LIMITED,
        "C": Accessibility.CLOSED,
        "Contact landowner for additional information": Accessibility.LIMITED,
        "Contact landowner for additional information: Do not promote/publish without permission": Accessibility.LIMITED,
        "Easement ROW": Accessibility.LIMITED,
        "Guaranteed Vehicle Access": Accessibility.LIMITED,
        "No public access": Accessibility.CLOSED,
        "Not Allowed": Accessibility.CLOSED,
        "Not allowed": Accessibility.CLOSED,
        "Not allowed - by law, for safety reasons,": Accessibility.CLOSED,
        "Private": Accessibility.CLOSED,
        "Restricted - land owner permission required": Accessibility.CLOSED,
        "Restricted - landowner permission required": Accessibility.CLOSED,
        "Restricted to trail area only": Accessibility.LIMITED,
        "Restricted: access restricted to certain geographic areas": Accessibility.LIMITED,
        "Unknown": Accessibility.UNKNOWN,
        "Water access": Accessibility.LIMITED,
    }
    return lookup_table.get(accessibility, None)


maine_conserved_lands["accessibility"] = maine_conserved_lands["PUB_ACCESS"].apply(
    lambda x: str(normalize_accessibility(x))
)

# %%

extract = maine_conserved_lands[
    [
        "accessibility_site_name",
        "accessibility_owner",
        "accessibility_source",
        "accessibility_retrieval_date",
        "accessibility",
        "geometry",
    ]
]
extract.to_file("../data/public_lands_me.gpkg", driver="GPKG")

# %%
