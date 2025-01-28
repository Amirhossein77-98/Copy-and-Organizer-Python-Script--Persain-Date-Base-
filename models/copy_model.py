import os
import shutil
from datetime import datetime
import jdatetime
import logging
import time

logging.basicConfig(filename='copy.log', level=logging.INFO)

PERSIAN_MONTHS_DICT = {
    "Farvardin": 1,
    "Ordibehesht": 2,
    "Khordad": 3,
    "Tir": 4,
    "Mordad": 5,
    "Shahrivar": 6,
    "Mehr": 7,
    "Aban": 8,
    "Azar": 9,
    "Dey": 10,
    "Bahman": 11,
    "Esfand": 12
}

GEORGIAN_MONTHS_DICT = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "Auguest": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def _get_file_details(src_file_path):
    modification_time = os.path.getmtime(src_file_path)
    modification_date = datetime.fromtimestamp(modification_time)
    ad_year = modification_date.year
    ad_month = modification_date.month
    ad_day = modification_date.day
    return modification_date, ad_year, ad_month, ad_day

def _copy_machine(filename, src_file_path, dest_folder):
    log_message = f"{datetime.now()} ^ Copying|||{filename}|||to|||{dest_folder}"
    print(log_message)
    logging.info(log_message)
    try:
        shutil.copy2(src_file_path, dest_folder)
        return True
    except PermissionError:
        logging.error(f"{datetime.now()} ^ Your|||system|||does|||not|||allow|||to|||use|||this|||folder")
        return False
    
    
class CopyModel:
    def __init__(self, controller):
        self.controller = controller

    def _update_progress_bar(self, items_count, items_copied):
        percentage = items_copied / items_count
        self.controller.update_progress_bar(percentage)
    
    def _valid_dir(self, src_folder):
        try:
            os.listdir(src_folder)
            return True
        except (FileNotFoundError, TypeError):
            logging.error(f"{datetime.now()} ^ File|||or|||Folder|||not|||found.")
            return False

    def copy_and_organize_files_shamsi_order_with_georgian_years(self, src_folder, dest_folder):
        if self._valid_dir(src_folder):
            listdir = os.listdir(src_folder)
        else:
            return False

        items_count = len(listdir)
        items_copied_count = 0
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            modification_date, ad_year, ad_month, ad_day = _get_file_details(src_file_path)
            
            persian_date = jdatetime.date.fromgregorian(year=ad_year, month=ad_month, day=ad_day)
            persian_year = persian_date.year
            persian_month = persian_date.month
            persian_month_name = persian_date.strftime("%B")
            
            dest_ad_year_folder = os.path.join(dest_folder, str(ad_year))
            if not os.path.exists(dest_ad_year_folder):
                os.makedirs(dest_ad_year_folder)

            dest_persian_month_folder = os.path.join(dest_ad_year_folder, f"{PERSIAN_MONTHS_DICT.get(persian_month_name, 0)}- {persian_month_name} {str(persian_year)}")
            if not os.path.exists(dest_persian_month_folder):
                os.makedirs(dest_persian_month_folder)
            
            result = _copy_machine(filename, src_file_path, dest_persian_month_folder)
            if not result:
                return False
            items_copied_count += 1
            self._update_progress_bar(items_count, items_copied_count)
        return True
    
    def copy_and_organize_files_shamsi_order(self, src_folder, dest_folder):
        if self._valid_dir(src_folder):
            listdir = os.listdir(src_folder)
        else:
            return False

        items_count = len(listdir)
        items_copied_count = 0
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            modification_date, ad_year, ad_month, ad_day = _get_file_details(src_file_path)
            
            persian_date = jdatetime.date.fromgregorian(year=ad_year, month=ad_month, day=ad_day)
            persian_year = persian_date.year
            persian_month = persian_date.month
            persian_month_name = persian_date.strftime("%B")
            
            dest_persian_year_folder = os.path.join(dest_folder, str(persian_year))
            if not os.path.exists(dest_persian_year_folder):
                os.makedirs(dest_persian_year_folder)

            dest_persian_month_folder = os.path.join(dest_persian_year_folder, f"{PERSIAN_MONTHS_DICT.get(persian_month_name, 0)}- {persian_month_name}")
            if not os.path.exists(dest_persian_month_folder):
                os.makedirs(dest_persian_month_folder)
            
            result = _copy_machine(filename, src_file_path, dest_persian_month_folder)
            if not result:
                return False
            items_copied_count += 1
            self._update_progress_bar(items_count, items_copied_count)
        return True

    def copy_and_organize_files_georgian_order(self, src_folder, dest_folder):
        if self._valid_dir(src_folder):
            listdir = os.listdir(src_folder)
        else:
            return False

        
        items_count = len(listdir)
        items_copied_count = 0
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            modification_date, ad_year, *other = _get_file_details(src_file_path)

            ad_month_name = modification_date.strftime("%B")

            dest_ad_year_folder = os.path.join(dest_folder, str(ad_year))
            if not os.path.exists(dest_ad_year_folder):
                os.mkdir(dest_ad_year_folder)

            dest_ad_month_folder = os.path.join(dest_ad_year_folder, f"{GEORGIAN_MONTHS_DICT.get(ad_month_name, 0)}- {ad_month_name}")
            if not os.path.exists(dest_ad_month_folder):
                os.mkdir(dest_ad_month_folder)
            
            result = _copy_machine(filename, src_file_path, dest_ad_month_folder)
            if not result:
                return False
            items_copied_count += 1
            self._update_progress_bar(items_count, items_copied_count)
        return True

    def simple_bulk_copy(self, src_folder, dest_folder):
        if self._valid_dir(src_folder):
            listdir = os.listdir(src_folder)
        else:
            return False

        
        items_count = len(listdir)
        items_copied_count = 0
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            result = _copy_machine(filename, src_file_path, dest_folder)
            if not result:
                return False
            items_copied_count += 1
            self._update_progress_bar(items_count, items_copied_count)
        return True
    
    def delete_files_after_copy(self, source):
        max_retries = 3
        retry_delay = 1  # seconds

        for attempt in range(max_retries):
            try:
                # Ensure all file handles are closed
                import gc
                gc.collect()
                time.sleep(retry_delay)
                
                if os.path.isfile(source):
                    os.chmod(source, 0o777)  # Give full permissions
                    os.remove(source)
                elif os.path.isdir(source):
                    for root, dirs, files in os.walk(source):
                        for f in files:
                            filepath = os.path.join(root, f)
                            try:
                                os.chmod(filepath, 0o777)
                            except:
                                pass
                    shutil.rmtree(source, ignore_errors=True)
                return (True, "Success", "All files and the folders copied and deleted successfully.")
                
            except PermissionError as e:
                if attempt == max_retries - 1:
                    return (False, "Error", f"Could not delete {source} after {max_retries} attempts")
                time.sleep(retry_delay)
                continue
                
            except Exception as e:
                return (False, "Error", f"Unexpected error: {str(e)}")