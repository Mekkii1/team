import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
import contextily as ctx

class AccessViz:
    MODE2COL = dict(walk="walk_t", bike="bike_s_t", pt="pt_r_t", car="car_r_t")

    def __init__(self, grid_shp_path: Path):
        self.grid_shp = grid_shp_path

    def join_tables(self, matrix_paths, out_folder: Path, fmt="gpkg"):
        """
        Joins the uploaded matrix files to the base grid and writes output files
        directly into 'out_folder'.
        """
        out_folder.mkdir(exist_ok=True)
        grid = gpd.read_file(self.grid_shp)
        print(f" Base grid loaded: {self.grid_shp}")

        for mp in matrix_paths:
            ykr_id = mp.stem.split("_")[-1].strip()
            mat = pd.read_csv(mp, sep=";")
            joined = grid.merge(mat, left_on="YKR_ID", right_on="from_id")
            out = out_folder / f"{ykr_id}.{fmt}"

            driver = "GPKG"
            joined.to_file(out, driver=driver)
            print(f"Joined & saved: {out} ({len(joined)} rows)")

    def plot(self, ykr_ids, out_folder: Path, column="car_r_t"):
        """
        Plots the GPKG outputs and saves maps as PNGs directly into 'out_folder'.
        The file name pattern is: {ykr_id}_{column}.png
        """
        out_folder.mkdir(exist_ok=True)

        for yid in ykr_ids:
            gpkg_path = out_folder / f"{yid}.gpkg"
            if not gpkg_path.exists():
                print(f" Skipping {yid} — {gpkg_path} not found.")
                continue

            gdf = gpd.read_file(gpkg_path)
            gdf= gdf.to_crs(epsg=3857)
            ax = gdf.plot(
                column=column,
                scheme="quantiles",
                cmap="Reds",
                legend=True,
                figsize=(15, 15),
                alpha=0.6,
                linewidth=0.1
            )
            ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
            ax.set_title(f"{column} to {yid}")
            ax.set_axis_off()

            out = out_folder / f"{yid}_{column}.png"
            plt.savefig(out, dpi=250,bbox_inches='tight')
            plt.close()
            print(f"Plot saved → {out}")