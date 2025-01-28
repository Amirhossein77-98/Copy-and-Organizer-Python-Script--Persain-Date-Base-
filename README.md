# Copy and Organize Files

This is a Python script that copies files from a source folder to a destination folder based on their modification dates. The script uses the [jdatetime](https://pypi.org/project/jdatetime/) module to convert the Gregorian dates to the Persian (Jalali) calendar.

<div align="center">
    <img src="assets/screenshots/image0.png" alt="Main Window" width="300"/>
    <img src="assets/screenshots/image1.png" alt="Main Window After Copy" width="300"/>
</div>

## Download

<a link="https://objects.githubusercontent.com/github-production-release-asset-2e65be/688850101/06ab4281-6aa6-4ccd-a632-8e4df71ee2c9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250128T163926Z&X-Amz-Expires=300&X-Amz-Signature=7d44bfe2d64d87dc9543887f6c89909b1d479da86ee4d9be2bfc178efcad5cca&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dcopy.script.exe">Download for Windows</a>

## Requirements

- Python 3.6 or higher
- jdatetime 3.6.4 or higher
- CustomTkinter

## Installation

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the required packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. Use the GUI to select the source and destination folders:
    - Click the "Browse" button next to "Origin" to select the source folder.
    - Click the "Browse" button next to "Destination" to select the destination folder.
    - Select the operation mode from the dropdown menu.
    - Optionally, check the "Delete files after copy" checkbox if you want to delete the files after copying.
    - Click the "Copy!" button to start copying files.

3. The script will copy each file from the source folder to a subfolder in the destination folder based on the selected operation mode:
    - **Simple Bulk Copy**: Copies files without organizing.
    - **Copy & Organize (Shamsi)**: Organizes files into folders based on the Persian (Jalali) calendar.
    - **Copy & Organize (Shamsi with Georgian Years)**: Organizes files into folders based on the Persian (Jalali) calendar with Georgian years.
    - **Copy & Organize (Georgian)**: Organizes files into folders based on the Gregorian calendar.

4. The script will also create a log file named [copy.log](http://_vscodecontentref_/1) in the same directory as the script, which records the copying process and timestamps.

## Example

Suppose the source folder contains these files:

- DSC_001.jpg (modified on 2023-03-21)
- DSC_002.jpg (modified on 2023-03-22)
- DSC_003.jpg (modified on 2023-04-01)

The destination folder will have these subfolders and files after running the script:

- 1402
    - 4 Farvardin 1402
        - DSC_003.jpg
    - 3 Farvardin 1402
        - DSC_001.jpg
        - DSC_002.jpg

## Logging

The script logs the copying process to both the console and a [Text](http://_vscodecontentref_/2) widget in the GUI. The log messages are colorized for better readability:
- Timestamp: Cyan
- Operation mode: Red
- Filename: Yellow
- Destination: Yellow

## License

This project is licensed under the MIT License.
