# Experimental Borden Grid

**THIS IS *NOT* AN OFFICIAL GRID.**

This repo contains an automatically generated, *experimental* GIS layer of the Canada Borden archaeological grid. It is **not** affiliated with the Canadian Archaeological Association or with any provincial or federal heritage branch. This experimental grid is intended for use between 42 ° N and 62 ° N. Accuracy north of 62 ° N is not valid.

The script was developed with the assistance of ChatGPT (OpenAI o3) and has been verified against Québec archaeological site point data.

**File:** `borden_experimental.py`
**Output:** `borden_grid_canada.gpkg`

The layer follows the public description of the Borden system:

- **Major blocks:** 2 ° × 4 ° (8 ° wide north of 62 ° N)  
- **Minor blocks:** 10′ × 10′ (20′ wide north of 62 ° N)

Always double-check the validity of any grid-unit code against known archaeological sites.

**Coordinate reference system:** The exported layer (`borden_grid_canada.gpkg`) is in unprojected latitude/longitude, EPSG 4326 (WGS 84). Re-project in any GIS software if you need an equal-area provincial CRS.
