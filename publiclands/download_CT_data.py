# %%
import esri2gpd
import geopandas as gpd

# https://services1.arcgis.com/FjPcSmEFuDYlIdKC/arcgis/rest/services/2011_Protected_Open_Space_Mapping/FeatureServer
# %%
ct_open_space = esri2gpd.get(
    "https://services1.arcgis.com/FjPcSmEFuDYlIdKC/arcgis/rest/services/2011_Protected_Open_Space_Mapping/FeatureServer/0"
)

# %%
# Unclear how to interpret the above data
