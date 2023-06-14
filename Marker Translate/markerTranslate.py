# Ethan Vosburg
# 6/14/2023
# Purpose: To translate markers from a timeline to a FrameIO marker

# Import DaVinci Resolve Scripting API
import modules.DaVinciResolveScript as dvr_script

# Create instance of DaVinci Resolve and Project Variables
resolve = dvr_script.scriptapp("Resolve")
fusion = resolve.Fusion()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
timeline = project.GetCurrentTimeline()
print ("Timeline: " + timeline.GetName() + "\n")


# Get Markers from Timeline
markers = timeline.GetMarkers()
# print ("Markers: " +  str(markers))

# Iterate through markers and print out information
for marker in markers:
    if markers[marker]["color"] == "Blue":
        print ("Blue Marker Found: " + str(markers[marker]["name"]))
        isMarker = timeline.AddMarker( marker + 1, "FrameIO", markers[marker]["name"], markers[marker]["name"], 1, "")
        print (isMarker)

        # Check if marker is a FrameIO marker to update the marker
        if isMarker == False and markers[marker + 1]["color"] == "FrameIO" and markers[marker + 1]["name"] != markers[marker]["name"]:
            print ("Marker Already Exists Changing Parameters")
            timeline.DeleteMarkerAtFrame(marker + 1)
            isMarker = timeline.AddMarker( marker + 1, "FrameIO", markers[marker]["name"], markers[marker]["name"], 1, "")

        print (str(marker) + "\n")