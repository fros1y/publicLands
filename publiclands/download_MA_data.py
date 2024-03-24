# %%
import geopandas as gpd

# %%

# Description

# The protected and recreational open space datalayer contains the boundaries of conservation lands and outdoor recreational facilities in Massachusetts. The associated database contains relevant information about each parcel, including ownership, level of protection, public accessibility, assessor’s map and lot numbers, and related legal interests held on the land, including conservation restrictions. Conservation and outdoor recreational facilities owned by federal, state, county, municipal, and nonprofit enterprises are included in this datalayer. Not all lands in this layer are protected in perpetuity, though nearly all have at least some level of protection.

# Open spaces may comprise:
# conservation land- habitat protection with minimal recreation, such as walking trails
# recreation land-  outdoor facilities such as town parks, commons, playing fields, school fields, golf courses, bike paths, scout camps, and fish and game clubs. These may be privately or publicly owned facilities.
# town forests
# parkways - green buffers along roads, if they are a recognized conservation resource
# agricultural land- land protected under an Agricultural Preservation Restriction (APR) and administered by the state Department of Agricultural Resources (DAR, formerly the Dept. of Food and Agriculture (DFA))
# aquifer protection land  -  not zoning overlay districts
# watershed protection land - not zoning overlay districts
# cemeteries - if a recognized conservation or recreation resource
# forest land -- if designated as a Forest Legacy Area
# Definitions of "Level of Protection":

# In Perpetuity (P)- Legally protected in perpetuity and recorded as such in a deed or other official document. Land is considered protected in perpetuity if it is owned by the town’s conservation commission or, sometimes, by the water department; if a town has a conservation restriction on the property in perpetuity; if it is owned by one of the state’s conservation agencies (thereby covered by article 97); if it is owned by a non-profit land trust; or if the town received federal or state assistance for the purchase or improvement of the property.

# Private land is considered protected if it has a deed restriction in perpetuity, if an Agriculture Preservation Restriction has been placed on it, or a Conservation Restriction has been placed on it.

# Temporary (T) - Legally protected for less than perpetuity (e.g. short term conservation restriction), or temporarily protected through an existing functional use. For example, some water district lands are only temporarily protected while water resource protection is their primary use.

# These lands could be developed for other uses at the end of their temporary protection or when their functional use is no longer necessary. These lands will revert to unprotected status at a given date unless protection status is extended.

# Limited (L) - Protected by legal mechanisms other than those above, or protected through functional or traditional use.

# These lands might be protected by a requirement of a majority municipal vote for any change in status. This designation also includes lands that are likely to remain open space for other reasons (e.g. cemeteries and municipal golf courses).

# None (N) - Totally unprotected by any legal or functional means. This land is usually privately owned and could be sold without restriction at any time for another use (e.g. scout camps, private golf course, and private woodland).

# Where the level of protection is unknown, a polygon will be coded as X for this field.
# %%
public_lands_ma = gpd.read_file(
    "https://s3.us-east-1.amazonaws.com/download.massgis.digital.mass.gov/gdbs/openspace_gdb.zip"
)

# %%


# PUB_ACCESS	Y - Yes (open to public)
# N - No (not open to public)
# L - Limited (membership only)
# X - Unknown

from accessibility import Accessibility


def normalize_accessibility(accessibility):
    if accessibility == "Y":
        return Accessibility.OPEN
    elif accessibility == "N":
        return Accessibility.CLOSED
    elif accessibility == "L":
        return Accessibility.LIMITED
    elif accessibility == "X":
        return Accessibility.UNKNOWN
    else:
        return None


# %%
public_lands_ma["accessibility"] = public_lands_ma["PUB_ACCESS"].apply(
    lambda x: str(normalize_accessibility(x))
)

# %%
public_lands_ma["accessibility_site_name"] = public_lands_ma["SITE_NAME"]
public_lands_ma["accessibility_owner"] = public_lands_ma["FEE_OWNER"]
public_lands_ma["accessibility_source"] = (
    "https://www.mass.gov/info-details/massgis-data-protected-and-recreational-openspace"
)
public_lands_ma["accessibility_retrieval_date"] = "2024-03-24"

# %%
public_lands_ma[
    [
        "accessibility_site_name",
        "accessibility_owner",
        "accessibility_source",
        "accessibility_retrieval_date",
        "accessibility",
        "geometry",
    ]
].to_file("../data/public_lands_ma.gpkg", driver="GPKG")

# %%
