import geopandas as gpd
from shapely.geometry import box
from pyproj import CRS

# ---- constants ---------------------------------------------------------------
OUT_CRS = CRS.from_epsg(4326)          # lat/long; re-project later if needed
LAT_ROWS = range(0, (84 - 42) * 6)     # 0 … 252 ten-minute rows  (6 per °)
LON_COLS = range(0, (144 - 52) * 6)    # 0 … 552 ten-minute cols (6 per °)

def major_lat_letter(i):   return chr(ord('A') + i // 12)          # 12×10′=2°
def minor_lat_letter(i):   return chr(ord('a') + i  % 12)
def major_lon_letter(j):   return chr(ord('A') + j // 24)          # 24×10′=4°
def minor_lon_letter(j, i):
    if i >= (62 - 42) * 6:              # ≥ 62 ° N  ⇒ 20′ wide
        return chr(ord('a') + (j % 48) // 2)    # 48 cols of 10′ collapse to 24
    return chr(ord('a') +  j % 24)

records = []
for i in LAT_ROWS:
    lat0 = 42 + (i * 10) / 60          # exact minutes
    lat1 = lat0 + 10/60
    step = 20/60 if lat0 >= 62 else 10/60
    for j in LON_COLS:
        lon0 = -52 - (j * 10) / 60
        if lat0 >= 62 and (j % 2):      # skip every second 10′ column ≥62° N
            continue
        lon1 = lon0 - step
        code = (major_lat_letter(i) + minor_lat_letter(i) +
                major_lon_letter(j) + minor_lon_letter(j, i))
        records.append({"code": code,
                        "geometry": box(lon1, lat0, lon0, lat1)})

gdf = gpd.GeoDataFrame(records, geometry="geometry", crs=OUT_CRS)
gdf.to_file("borden_grid_canada.gpkg", driver="GPKG")
print(f"Wrote {len(gdf):,} blocks.")
