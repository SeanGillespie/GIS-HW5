# hw5.py
# Description: does hw4, but in python
# To recap, my hw4 was calculating the number of state parks in each Oregon county and displaying on a map.
# The result of this script is the number of state parks joined into the original county table
# cannot change symbology of map from python, but this is easily done in arcmap from the altered county table
# Requirements: os module, arcpy

import arcpy
import os

#workspace to look for files
workspace = r"C:\Users\gillespi20\Downloads\hw5\hw5.gdb"
#workspace for writing files, same as above.
outWorkspace = r"C:\Users\gillespi20\Downloads\hw5\hw5.gdb"

#part 1: spatial join counties to state parks

#target features for join is the state parks, because we want to know the county the park is in
targetFeatures = os.path.join(workspace, "LO_PARKS")
#join features are the counties because we want the name of the county joined to the state park
joinFeatures = os.path.join(workspace, "county")
#create a new file parks_with_county in the workspace for the results of the join
parks_with_county = os.path.join(outWorkspace, "parks_with_county")
#spatial join the counties to the state parks so that we know which county each park is in and write to file
arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, parks_with_county)

#part 2: summary statistics to count number of state parks in each county

#create a new file that is the count of each county name from the result table of part 1 above
cstats = os.path.join(outWorkspace, "county_count_table")
#use summary statistics to count the frequency of each unique county name (NAME_1)
arcpy.Statistics_analysis(parks_with_county, cstats, [["NAME_1","COUNT"]], "NAME_1")

#part 3: join original county table with county count table

#joining counts of county names back into original county table, shared field is the county name.
arcpy.JoinField_management(joinFeatures, "NAME", cstats, "NAME_1", ["COUNT_NAME_1"])
