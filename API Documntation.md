# visualization_tool
visualization tool API is a wep api that transform tabular travel time data into a map
## HTTP Method 
Post
## API Url
[url](http://127.0.0.1:8000/visualization_tool)
## Description 
this endpoint helps you to analysis travel time matrix and display it with spatial layer
## Request params 

folder: required , String, contain folder name
file: required , String, contain traveltime file name
column:required, String , contain column name that you want to visualize on the map
map_type: required , String , contain map type choose between (static/interactive)
outputlayer_name: required, String, contain layer name without file format
output_map_name: required, String , contain map name without file format

## Request Example 

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
## Response Example


```json
{
  "message": "Map saved successfully",
  "output_map_path": "outputs/travel_map.html"
}
```
## Error handleing 
when user try unvalid data
```json
{
  "detail": "Analysis error: the map layer is empty try valid data"
}
```
## the output should be file contain the map and shapefile contain the spatial layer