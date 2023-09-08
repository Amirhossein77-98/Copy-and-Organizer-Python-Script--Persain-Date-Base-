# Copy and Organize Files

This is a Python script that copies files from a source folder to a destination folder based on their modification dates. The script uses the [jdatetime](https://pypi.org/project/jdatetime/) module to convert the Gregorian dates to the Persian (Jalali) calendar.

## Requirements

- Python 3.6 or higher
- jdatetime 3.6.4 or higher

## Usage

- Edit the `src_folder` and `dest_folder` variables in the script to specify the source and destination folders.
- Run the script as `python copy_files.py`
- The script will copy each file from the source folder to a subfolder in the destination folder named as `{Persian month number} {Persian month name} {Persian year}`. For example, `10 Mehr 1402`.
- Folders name's prefix number is added to organize folders based on the AD Dates. So DAY would be equal to 1.
- The script will also create a log file named `copy.log` in the same directory as the script, which records the copying process and timestamps.

## Example

Suppose the source folder contains these files:

- DSC_001.jpg (modified on 2023-03-21)
- DSC_002.jpg (modified on 2023-03-22)
- DSC_003.jpg (modified on 2023-04-01)

The destination folder will have these subfolders and files after running the script:

- 1402
    - 4 Farvardin 1402
        - DSC_003.jpg
    - 3 Esfand 1401
        - DSC_001.jpg
        - DSC_002.jpg

The log file will have these entries:

```
2023-09-08 10:30:59.051455 - Copying 20230908_102742.jpg to D:\Personal\2023\9 Shahrivar 1402
2023-09-08 10:30:59.061207 - Copying 20230908_102743.jpg to D:\Personal\2023\9 Shahrivar 1402
2023-09-08 10:30:59.071219 - Copying 20230908_102746.mp4 to D:\Personal\2023\9 Shahrivar 1402
```
