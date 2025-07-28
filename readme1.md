# AccessViz
AccessViz project is a wep api built with fastapi that transform tabular travel time data into (interactive/static)map

## features

Read and process spatial grid data.
Automatically locate and merge travel time files.
Join tabular data with spatial data to produce GeoDataFrames.
Create either interactive (HTML) or static (image) maps.
Export the spatial layer as a Shapefile.
Save the generated map to a specified output path

## requirements
check the requirements text

## installation

git clone https://github.com/yousefeleraky/team.git
cd team
pip install -r requirements.txt
uvicorn main:app --reload

## Usage

To run the API locally:
 
uvicorn main:app --reload

Once the server is running, you can use a tool like Postman or `curl` to make requests to the API.

### Example Request for AccessViz
**Endpoint**: `post/ visualization_tool`
 
Request Body:
```json
{
  
  "folder": "578",
  "file": "57840",
  "column": "car_m_d",
  "map_type": "interactive",
  "output_layer_name": "travel_map",
  "output_map_name": "travel_map"

}
```
example response
```json
{
  "message": "Map saved successfully",
  "output_map_path": "outputs/travel_map.html"
}
```
## on error
```json
{
  "detail": "Analysis error: the map layer is empty try valid data"
}
```