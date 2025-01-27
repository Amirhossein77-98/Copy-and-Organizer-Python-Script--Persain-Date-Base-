# Copy and Organize Files

This is a Python script that copies files from a source folder to a destination folder based on their modification dates. The script uses the [jdatetime](https://pypi.org/project/jdatetime/) module to convert the Gregorian dates to the Persian (Jalali) calendar.

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
    - Click the "Copy!" button to start copying files.

3. The script will copy each file from the source folder to a subfolder in the destination folder named as `{Persian month number} {Persian month name} {Persian year}`. For example, `10 Mehr 1402`.
    - Folders name's prefix number is added to organize folders based on the AD Dates. So DAY would be equal to 1.
    - If a file with the same name already exists in the destination folder, the script will rename the file by appending a counter to the filename (e.g., `filename_1.ext`, `filename_2.ext`, etc.).

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

The script logs the copying process to both the console and a `Text` widget in the GUI. The log messages are colorized for better readability:
- Timestamp: Cyan
- Operation mode: Red
- Filename: Yellow
- Destination: Yellow

## License

This project is licensed under the MIT License.
