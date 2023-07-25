# Video to Audio Converter

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![PyQt Version](https://img.shields.io/badge/PyQt-6.x-brightgreen.svg)
![MoviePy Version](https://img.shields.io/badge/MoviePy-Latest-red.svg)

## Description

This Python application allows you to convert MP4 files to MP3 files using the `moviepy` library and the PyQt library for the user interface.

## How to Use

1. Install the required Python packages by running the following command:
    ```pip install PyQt6```
    ```pip install MoviePy```

2. Clone or download this repository.

3. Open a terminal or command prompt and navigate to the project directory:


4. Run the converter application:


5. The application will open with a simple user interface. Click on the "Choose Video Folder" button to select the folder containing the video files you want to convert.

6. After selecting the folder, the video files available for conversion will be listed. Double-click on a video to convert it to an MP3 file. Alternatively, you can click once on a video and then click the "Convert" button to choose the destination folder for the converted audio file.

7. The converted audio files will be listed in the "Converted Audios" section.

## Developer

- **Developer:** Pollard Samba
- **Email:** pollardsamba1@gmail.com
- **GitHub:** [POLLARD1145](https://github.com/POLLARD1145)

## Dependencies

- [MoviePy](https://zulko.github.io/moviepy/)
- [PyQt6](https://pypi.org/project/PyQt6/)

---

```python
# Paste your Python code here
# ...

#END OF THE PROGRAM, ALLOW SYSTEM TO DISPLAY YOUR PROGRAM
if __name__ == "__main__":
 import sys
 app = QtWidgets.QApplication(sys.argv)
 MainWindow = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(MainWindow)
 MainWindow.show()
 sys.exit(app.exec())
