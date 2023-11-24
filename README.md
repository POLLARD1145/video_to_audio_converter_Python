# Video to Audio Converter

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![PyQt Version](https://img.shields.io/badge/PyQt-6.x-brightgreen.svg)
![MoviePy Version](https://img.shields.io/badge/MoviePy-Latest-red.svg)

## Description

This Python application allows you to convert MP4 files to MP3 files using the `moviepy` library and the `PyQt` library for the user interface.

## Visual Appearance
   ### Home Screen
![home](https://github.com/POLLARD1145/video_to_audio_converter_Python/assets/69053974/d8307a4b-33b1-4375-b042-fd55941f48a3)




## How to Use

1. Install the required Python packages by running the following command:
2. 
   -PyQt:   ```pip install PyQt6```
   
   -MoviePy:  ```pip install MoviePy```

4. Clone or download this repository.

5. Open a terminal or command prompt and navigate to the project directory:


6. Run the converter application:
   The Home screen will show up
   ![home](https://github.com/POLLARD1145/video_to_audio_converter_Python/assets/69053974/d8307a4b-33b1-4375-b042-fd55941f48a3)

8. The application will open with a simple user interface. Click on the "Choose Video Folder" button to select the folder containing the video files you want to convert.
   The list of videos in the selected folder will be listed under the videos section
   ![videos](https://github.com/POLLARD1145/video_to_audio_converter_Python/assets/69053974/20f4ba8d-a3d1-4a0e-9077-d018bf4ddd16)


10. After selecting the folder, the video files available for conversion will be listed. Double-click on a video to convert it to an MP3 file. Alternatively, you can click once on a video and then click the "Convert" button to choose the destination folder for the converted audio file.

    ![converting](https://github.com/POLLARD1145/video_to_audio_converter_Python/assets/69053974/b5e1d691-b5ce-48c8-832e-ed3978c0e25b)

12. The converted audio files will be listed in the "Converted Audios" section.

    ![Audios](https://github.com/POLLARD1145/video_to_audio_converter_Python/assets/69053974/e3d1e134-d697-4a79-9c84-62680e9f9b73)

    You can locate the audios in the folder indicated at the bottom.


## Developer

- **Developer:** Pollard Samba
- **Email:** pollardsamba1@gmail.com
- **GitHub:** [POLLARD1145](https://github.com/POLLARD1145)

## Dependencies

- [MoviePy](https://zulko.github.io/moviepy/)
- [PyQt6](https://pypi.org/project/PyQt6/)

---
## Code Snippet

```python

#END OF THE PROGRAM, ALLOW SYSTEM TO DISPLAY YOUR PROGRAM
if __name__ == "__main__":
 import sys
 app = QtWidgets.QApplication(sys.argv)
 MainWindow = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(MainWindow)
 MainWindow.show()
 sys.exit(app.exec())
