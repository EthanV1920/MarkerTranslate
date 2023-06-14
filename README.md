# Marker Translation for FrameIO

This script translates markers from a timeline in DaVinci Resolve to FrameIO markers. It utilizes the DaVinci Resolve Scripting API to interact with the Resolve application and perform the marker translation.

## Purpose

The purpose of this script is to automate the process of converting markers in DaVinci Resolve to FrameIO markers. It allows you to easily transfer marker information from your timeline to FrameIO for collaboration and sharing purposes.

## Requirements

To run this script, you need to have the following:

- DaVinci Resolve Studio: Make sure you have DaVinci Resolve installed on your system.
- DaVinci Resolve Scripting API: This script uses the DaVinci Resolve Scripting API to interact with Resolve. Ensure that the necessary API is set up and accessible.


## Installation

1. Ensure the [DaVinci Resolve Studio](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion) is installed to allow for scripting
2. Ensure that [Python 3.6 or greater](https://www.python.org/) is installed
3. Put the contents of ["Marker Translate"](https://github.com/EthanV1920/MarkerTranslate/tree/main/Marker%20Translate) in to the folder that corrisponds to your system<br>
    Mac OS X:
      - All users: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts
      - Specific user:  /Users/<UserName>/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts<br>

    Windows:
      - All users: %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts
      - Specific user: %APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts<br>

    Linux:
      - All users: /opt/resolve/Fusion/Scripts  (or /home/resolve/Fusion/Scripts/ depending on installation)
      - Specific user: $HOME/.local/share/DaVinciResolve/Fusion/Scripts


## Usage

1. Open DaVinci Resolve Studio
2. Open a project and export and upload the timeline to [Frame.io](https://www.frame.io) to link timeline to Frame.io
3. Create Blue marker with titles of the comments you would like to leave in Frame.io
4. Select workspace > scripts > "YOUR_SCRIPT"
5. Add a keyboard short cut if desired


## Understanding the Script

1. Import the DaVinci Resolve Scripting API module using the following command:

   ```python
   import DaVinciResolveScript as dvr_script
   ```

2. Create an instance of DaVinci Resolve and define project-related variables:

   ```python
   resolve = dvr_script.scriptapp("Resolve")
   fusion = resolve.Fusion()
   projectManager = resolve.GetProjectManager()
   project = projectManager.GetCurrentProject()
   timeline = project.GetCurrentTimeline()
   ```

3. Retrieve markers from the timeline using the `GetMarkers()` method:

   ```python
   markers = timeline.GetMarkers()
   ```

4. Iterate through the markers and perform the necessary marker translation operations. The script checks if a marker is blue and adds a FrameIO marker in its place:

   ```python
   for marker in markers:
       if markers[marker]["color"] == "Blue":
           # Perform marker translation
           # ...
   ```

5. Run the script to execute the marker translation.

## Notes

- Make sure you have the appropriate permissions and access rights to use the DaVinci Resolve Scripting API.
- Customize the script according to your specific marker translation requirements.

## Author

- Name: Ethan Vosburg
- Date: 6/14/2023
