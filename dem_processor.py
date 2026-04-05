# -*- coding: utf-8 -*-
"""
DEM Processor - Geospatial Analysis Pipeline

Processes Digital Elevation Model data and satellite imagery using ArcPy.
Generates contour maps, composite imagery, and 3D mesh-ready outputs.

Author: Dexter Ferguson
"""


import arcpy

#Setting up the Workspace
workspace = "C:/Python/GeospatialProgramming/DCF_Final"
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True

#Setting up variables
dem = "gt30e100n40.tif" #DEM of Area
fujiArea = "FujiArea.shp" #Area in which Mt. Fuji Resides
fujiBounds = workspace + "/output/FujiBounds.tif" #Raster for extent
fujiDEM = workspace +"/output/FujiRaster.tif" #DEM of Mt. Fuji's extent
fujiRasterCon = workspace +"/output/FujiRasterCon.shp" #Contour Map of Mt. Fuji
jstack = workspace +"/output/fujiStack.tif" #Stack of images of Mt. Fuji Area
fujiStackClip = workspace +"/output/fujiStackClip.tif" #Clipping of stack
oneBndMsh = workspace + "/output/oneBandMesh.tif" #Turning the stack into a flat image

##Creating Extent for Mt. Fuji
arcpy.conversion.PolygonToRaster(fujiArea, "f_code", fujiBounds)
bndCln = arcpy.sa.BoundaryClean(fujiBounds, "ASCEND", "TWO_WAY")
bndCln.save(fujiBounds)

##Creating Contours
arcpy.management.Clip(dem,"",fujiDEM, fujiBounds)
arcpy.sa.Contour(fujiDEM, fujiRasterCon, 100)

##Creating Mesh Overlay
#Stacking Images, Clipping them by extent, and flattening them to one band
arcpy.management.CompositeBands("jband4.tif;jband3.tif;jband2.tif", jstack)
arcpy.management.Clip(jstack,"",fujiStackClip, fujiBounds)
arcpy.management.CopyRaster(fujiStackClip, oneBndMsh)

#Cleaning up
del(bndCln)
