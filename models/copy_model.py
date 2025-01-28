import os
import shutil
from datetime import datetime
import jdatetime
import logging
import time
from models.constants import *

logging.basicConfig(filename='copy.log', level=logging.INFO)

    
    
class CopyModel:
    def __init__(self, controller):
        self.controller = controller

    def _update_progress_bar(self, items_count, items_copied):
        percentage = items_copied / items_count
        self.controller.update_progress_bar(percentage)

    def _get_file_details(self, src_file_path):
        modification_time = os.path.getmtime(src_file_path)
        modification_date = datetime.fromtimestamp(modification_time)
        ad_year = modification_date.year
        ad_month = modification_date.month
        ad_day = modification_date.day
        return modification_date, ad_year, ad_month, ad_day

    def _copy_machine(self, filename, src_file_path, dest_folder):
        log_message = f"{datetime.now()} ^ Copying|||{filename}|||to|||{dest_folder}"
        print(log_message)
        logging.info(log_message)
        try:
            shutil.copy2(src_file_path, dest_folder)
            return True
        except PermissionError:
            logging.error(f"{datetime.now()} ^ Your|||system|||does|||not|||allow|||to|||use|||this|||folder")
            return False
    
    def _valid_dir(self, src_folder):
        try:
            os.listdir(src_folder)
            return True
        except (FileNotFoundError, TypeError):
            logging.error(f"{datetime.now()} ^ File|||or|||Folder|||not|||found.")
            return False
        
    def _create_folders(self, dest_folder, mode, month_name, ad_year, persian_year=0):
        if mode == COPY_MODES["gg"] or mode == COPY_MODES["gp"]:
            parent_year_folder = os.path.join(dest_folder, str(ad_year))
        else:
            parent_year_folder = os.path.join(dest_folder, str(persian_year))

        if not os.path.exists(parent_year_folder):
            os.makedirs(parent_year_folder)

        if mode == COPY_MODES["gp"]:
            sub_folder_format = f"{PERSIAN_MONTHS_DICT.get(month_name, 0)}- {month_name} {str(persian_year)}"
        elif mode == COPY_MODES["pp"]:
            sub_folder_format = f"{PERSIAN_MONTHS_DICT.get(month_name, 0)}- {month_name}"
        else:
            sub_folder_format = f"{GEORGIAN_MONTHS_DICT.get(month_name, 0)}- {month_name}"
       
        dest_month_folder = os.path.join(parent_year_folder, sub_folder_format)
        
        if not os.path.exists(dest_month_folder):
            os.makedirs(dest_month_folder)
        
        return dest_month_folder

    def copy_and_organize_files_shamsi_order_with_georgian_years(self, src_folder, dest_folder):
        if self._valid_dir(src_folder):
            listdir = os.listdir(src_folder)
        else:
            return False

        items_count = len(listdir)
        items_copied_count = 0
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            modification_date, ad_year, ad_month, ad_day = self._get_file_details(src_file_path)
            
            persian_date = jdatetime.date.fromgregorian(year=ad_year, month=ad_month, day=ad_day)
            persian_year = persian_date.year
            persian_month = persian_date.month
            persian_month_name = persian_date.strftime("%B")
            
            destination_folder = self._create_folders(dest_folder, COPY_MODES["gp"], persian_month_name, ad_year, persian_year)
            
            result = self._copy_machine(filename, src_file_path, destination_folder)
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
            modification_date, ad_year, ad_month, ad_day = self._get_file_details(src_file_path)
            
            persian_date = jdatetime.date.fromgregorian(year=ad_year, month=ad_month, day=ad_day)
            persian_year = persian_date.year
            persian_month = persian_date.month
            persian_month_name = persian_date.strftime("%B")
            
            destination_folder = self._create_folders(dest_folder, COPY_MODES["pp"], persian_month_name, ad_year, persian_year)
            
            result = self._copy_machine(filename, src_file_path, destination_folder)
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
            modification_date, ad_year, *other = self._get_file_details(src_file_path)

            ad_month_name = modification_date.strftime("%B")

            destination_folder = self._create_folders(dest_folder, COPY_MODES["gg"], ad_month_name, ad_year)

            result = self._copy_machine(filename, src_file_path, destination_folder)
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
            result = self._copy_machine(filename, src_file_path, dest_folder)
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