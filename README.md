# ArcPy DEM Processing Project

A geospatial analysis pipeline for processing Digital Elevation Model (DEM) data and satellite imagery using ArcGIS Pro's ArcPy library. This project demonstrates terrain analysis techniques applied to the Mount Fuji region in Japan.

## Overview

This project processes raw elevation data and multi-band satellite imagery to generate:
- **Elevation contour maps** at 100-meter intervals
- **Multi-band composite imagery** from satellite data
- **Clipped raster outputs** bounded to a study area
- **3D mesh-ready outputs** for terrain visualization

## Features

- Polygon-to-raster conversion with boundary cleaning
- DEM clipping using vector extent boundaries
- Automated contour generation from elevation data
- Multi-band satellite image compositing (bands 2, 3, 4)
- Raster processing for 3D mesh generation

## Requirements

- **ArcGIS Pro** with Spatial Analyst extension
- **Python 3.x** (via ArcGIS Pro's Python environment)
- **arcpy** module

## Data Requirements

This project requires the following input data (not included due to file size):

| File | Description | Source |
|------|-------------|--------|
| `gt30e100n40.tif` | GTOPO30 DEM tile (30 arc-second resolution) | [USGS Earth Explorer](https://earthexplorer.usgs.gov/) |
| `FujiArea.shp` | Study area boundary shapefile | Create manually or obtain from administrative boundary data |
| `jband2.tif`, `jband3.tif`, `jband4.tif` | Satellite imagery bands | [USGS Earth Explorer](https://earthexplorer.usgs.gov/) (Landsat) |

## Project Structure

```
├── dem_processor.py      # Main processing script
├── FujiArea.shp          # Study area boundary (+ associated files)
├── gt30e100n40.tif       # Input DEM
├── jband*.tif            # Satellite imagery bands
└── output/               # Generated outputs
    ├── FujiBounds.tif    # Rasterized boundary
    ├── FujiRaster.tif    # Clipped DEM
    ├── FujiRasterCon.shp # Contour lines
    ├── fujiStack.tif     # Composite satellite imagery
    ├── fujiStackClip.tif # Clipped composite
    └── oneBandMesh.tif   # Single-band mesh output
```

## Usage

1. **Set up workspace**: Update the `workspace` variable in `dem_processor.py` to match your directory path.

2. **Place input data**: Ensure all required input files are in the workspace directory.

3. **Run the script**:
   ```python
   # From ArcGIS Pro Python environment
   python dem_processor.py
   ```

4. **Outputs**: Processed files will be saved to the `output/` directory.

## Processing Pipeline

```
Input DEM ─────────────┐
                       ├──> Clip DEM ──> Generate Contours
Study Area Boundary ───┴──> Polygon to Raster ──> Boundary Clean
                                    │
Satellite Bands (2,3,4) ──> Composite Bands ──> Clip to Boundary ──> 3D Mesh Output
```

## Output Specifications

| Output | Format | Description |
|--------|--------|-------------|
| FujiRaster.tif | GeoTIFF (16-bit) | Clipped elevation data |
| FujiRasterCon.shp | Shapefile | 100m contour polylines |
| fujiStackClip.tif | GeoTIFF (3-band) | RGB satellite composite |
| oneBandMesh.tif | GeoTIFF | Flattened image for 3D modeling |

## Coordinate System

- **Input CRS**: GCS_ITRF_1994 / WGS 1984
- **Extent**: 138.5°E - 139.0°E, 34.9°N - 35.6°N

## Author

Dexter Ferguson

## License

This project is available for educational and portfolio purposes.
