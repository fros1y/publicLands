# %%
import geopandas as gpd
import pandas as pd

# %%
# Load the data
nh = gpd.read_file("../data/public_lands_nh.gpkg").to_crs("EPSG:4326")
# %%
ma = gpd.read_file("../data/public_lands_ma.gpkg").to_crs("EPSG:4326")
# %%
me = gpd.read_file("../data/public_lands_me.gpkg").to_crs("EPSG:4326")
# %%
ri = gpd.read_file("../data/public_lands_ri.gpkg").to_crs("EPSG:4326")
# %%
padus = gpd.read_file("../data/public_lands_padus.gpkg").to_crs("EPSG:4326")

# %%
# Merge the data
public_lands = gpd.GeoDataFrame(pd.concat([nh, ma, me, ri, padus], ignore_index=True))

# %%
public_lands.to_file("../data/public_lands.gpkg", driver="GPKG")

# %%
