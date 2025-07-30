# 🚗 Travel Matrix Access Visualization API

![Travel Matrix Example](./DATA/5785640_car_r_t.png)

This API allows uploading `.txt` travel time matrix files (e.g. from Helsinki Region Travel Time Matrix), processes them by spatially joining them with a zone grid, and generates **PNG heatmaps** of car travel times.

---

## 🧠 What It Does ?

> Accepts one or more matrix files (`.txt`) with travel time values.
> Extracts the destination zone (`YKR_ID`) from the filename.
> Joins each matrix with a Helsinki grid shapefile (`MetropAccess_YKR_grid_EurefFIN.shp`).
> Exports the result as a `.gpkg` file (GeoPackage).
> Plots a map of car travel times and saves it as a `.png`.

---

## 🚀 Endpoint

### `POST Method --> /AccessViz`

Upload one or more `.txt` travel matrix files.

#### 📥 Request Parameters

- **`matrix_files`**: list of uploaded `.txt` files (multipart/form-data)

Each file must be named like: `travel_matrix_<ykr_id>.txt`  
Example: `travel_matrix_5975371.txt`

## 🧱 Dependencies

This API depends on a preloaded shapefile:

- [`MetropAccess_YKR_grid_EurefFIN.shp`](https://drive.google.com/file/d/17d7fFx2pKpjeCrHpzscrz37AqujqFLov/view)  
  > Download and extract this grid file into the `./DATA/` folder. The path is hardcoded in the script.


#### ✅ Response

Returns simple text confirmation:

```json
"All is good"
```

