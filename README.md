# File-managment-Automator

This Python program is an automated file organizer that monitors a specified folder (typically a downloads folder) and moves files into categorized destination folders based on their file type. 

Here's a summary of what it does:

🔍 Key Features:
Real-Time Monitoring: Uses the watchdog library to watch for changes in a source directory.

Automatic File Sorting: When a new file is added or modified in the source directory, it checks the file type and moves it accordingly:

Audio files smaller than 10MB or containing "SFX" in the name → moved to the SFX directory

Other audio files → moved to the Music directory

Video files → moved to the Video directory

Image files → moved to the Image directory

Document files → moved to the Documents directory

Name Conflict Resolution: If a file with the same name already exists in the destination, a unique name is generated by appending a number to it.

Logging: Logs each file move operation with timestamps.

⚠️ Setup Required:
The program won’t work until you fill in the following directory paths:

    PYTHON
    source_dir = ""
    dest_dir_sfx = ""
    dest_dir_music = ""
    dest_dir_video = ""
    dest_dir_image = ""
    dest_dir_documents = ""

Once these are correctly set, the program will automatically organize files based on their type as they appear in the source folder.






---Examples---
----------------------
*Have a folder that is mixed with Images and Docs and want to have them seperate now you can with this Program

    Image = I
    Docs = D
     
        MIX FILE                                       IMAGE FILE                         DOC FILE
                            
    |    I    D     D     |                       |    I                |            |        D     D     |
    |    I    I     D     |      SEPARATE         |    I    I           |            |              D     |
    |    I    D     D     |      ------->         |    I                |            |        D     D     |
    |    D    I     I     |        FILE           |         I     I     |            |    D               |
    |    D    I     D     |                       |         I           |            |    D         D     |
