import geopandas as gpd


def addGeoData(countryData):
    url = "https://opendata.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1.geojson"
    # world = gpd.read_file(url)
    # world.to_file("backupWorld.geojson", driver="GeoJSON")
    world = gpd.read_file("backupWorld.geojson")
    world = world.drop(columns=['OBJECTID'])
    world = world.rename(columns={"CNTRY_NAME": "Country"})
    combined_gdf = world.merge(countryData, on='Country', how='left').dropna()
    return combined_gdf
