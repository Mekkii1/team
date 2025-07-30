from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from typing import List
from pathlib import Path
import zipfile
from AccessVizClass import AccessViz

app = FastAPI()

#one folder for all outputs
PROJECT_OUTPUT_DIR = Path("project_outputs")
PROJECT_OUTPUT_DIR.mkdir(exist_ok=True)


@app.post("/AccessViz")
async def process_files(
    matrix_files: List[UploadFile],         
    ):
   
    GRID_SHP_PATH = Path("../Data/MetropAccess_YKR_grid/MetropAccess_YKR_grid_EurefFIN.shp")

    # Save every uploaded matrix file into the same folder
    saved_matrix_paths = []
    ykr_ids = []

    for txt in matrix_files:
        txt_path = PROJECT_OUTPUT_DIR / txt.filename
        with open(txt_path, "wb") as f:
            f.write(await txt.read())
        saved_matrix_paths.append(txt_path)

        ykr_id = txt.filename.split("_")[-1].replace(".txt", "").strip()
        ykr_ids.append(ykr_id)

    # Join GeoPackages 
    viz = AccessViz(grid_shp_path=GRID_SHP_PATH)
    viz.join_tables(saved_matrix_paths, out_folder=PROJECT_OUTPUT_DIR)

    # Plot → PNGs 
    viz.plot(ykr_ids, out_folder=PROJECT_OUTPUT_DIR)

    return "All is good"

