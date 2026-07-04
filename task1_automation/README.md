# File Organizer & Cleaner — Python Automation Script

## What it does
Organizes any messy folder by sorting files into subfolders by type
(Images, Documents, Videos, Audio, Archives, Code, Others), handles
duplicate filenames automatically, removes leftover empty folders,
and logs every action to `file_organizer_log.txt`.

## Requirements met
- Uses `os` module + full exception handling (`FileNotFoundError`,
  `PermissionError`, generic `Exception`)
- Generates logs for every operation (via Python `logging` module)
- Takes user input for the folder path

## How to run
```bash
python file_organizer.py
```
You'll be prompted:
```
Enter the full path of the folder to organize: /path/to/your/folder
```

## Sample Input
A test folder containing:
```
photo1.jpg  photo2.PNG  report.pdf  notes.txt  song.mp3
movie.mp4   script.py   archive.zip randomfile.xyz duplicate.txt
```

## Sample Output (console)
```
=======================================================
 FILE ORGANIZER & CLEANER - Automation Script
=======================================================
Enter the full path of the folder to organize:
Starting organization of: sample_test
Created folder: sample_test/Audio
Moved: 'song.mp3' -> 'Audio/song.mp3'
Created folder: sample_test/Documents
Moved: 'report.pdf' -> 'Documents/report.pdf'
Moved: 'duplicate.txt' -> 'Documents/duplicate.txt'
Created folder: sample_test/Archives
Moved: 'archive.zip' -> 'Archives/archive.zip'
Created folder: sample_test/Images
Moved: 'photo2.PNG' -> 'Images/photo2.PNG'
Created folder: sample_test/Videos
Moved: 'movie.mp4' -> 'Videos/movie.mp4'
Moved: 'notes.txt' -> 'Documents/notes.txt'
Moved: 'photo1.jpg' -> 'Images/photo1.jpg'
Created folder: sample_test/Code
Moved: 'script.py' -> 'Code/script.py'
Created folder: sample_test/Others
Moved: 'randomfile.xyz' -> 'Others/randomfile.xyz'
Organization complete. Moved: 10, Errors: 0
-------------------------------------------------------
Files moved : 10
Errors      : 0
Log saved to: /home/claude/automation_script/file_organizer_log.txt
-------------------------------------------------------
```

## Resulting folder structure
```
sample_test/
├── Archives/archive.zip
├── Audio/song.mp3
├── Code/script.py
├── Documents/
│   ├── duplicate.txt
│   ├── notes.txt
│   └── report.pdf
├── Images/
│   ├── photo1.jpg
│   └── photo2.PNG
├── Others/randomfile.xyz
└── Videos/movie.mp4
```
