#GEOG 885 Project 1 part II
#Create contours for Fox Lake DEM

import arcpy
from arcpy import env
from arcpy.sa import *
# set geoprecessing environment

arcpy.env.overwriteOutput=True

#import DEM
inRaster = "C:/Users/stncon1sq/Downloads/Lesson1/foxlake"

try:
    #create contours
    baseContour=0
    contourInterval=50
    outContours="C:/Users/stncon1sq/Downloads/Lesson1/FoxLake_contours.shp"
    arcpy.CheckOutExtension("Spatial")
    Contour(inRaster,outContours,contourInterval, baseContour)
    
except:
    #report an error message
    arcpy.AddError("Could not create contours from DEM")
    
    #report and error message that the create contours tool might have generated
    arcpy.AddMessage(arcpy.GetMessages())

try:
    #calculate slope
    outMeasure="degree"
    zFactor=0.3043
    outSlope=Slope(inRaster,outMeasure,zFactor)
    outSlope.save("C:/Users/stncon1sq/Downloads/Lesson1/FoxLake_slope")
except:
    #report an error message
    arcpy.AddError("Could not calculate slope from DEM")
    
    #report and error message that the calculate slope tool might have generated
    arcpy.AddMessage(arcpy.GetMessages())

print("Script Complete")

         



