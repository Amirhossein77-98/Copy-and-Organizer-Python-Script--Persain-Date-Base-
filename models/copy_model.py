import os
import shutil
from datetime import datetime
import jdatetime
import logging

logging.basicConfig(filename='copy.log', level=logging.INFO)

def _get_file_details(src_file_path):
    modification_time = os.path.getmtime(src_file_path)
    modification_date = datetime.fromtimestamp(modification_time)
    ad_year = modification_date.year
    ad_month = modification_date.month
    ad_day = modification_date.day
    return modification_date, ad_year, ad_month, ad_day

def _copy_machine(filename, src_file_path, dest_folder):
    log_message = f"{datetime.now()} - Copying {filename} to {dest_folder}"
    print(log_message)
    logging.info(log_message)
    try:
        shutil.copy2(src_file_path, dest_folder)
        return True
    except PermissionError:
        logging.error(f"{datetime.now()} - Your system does not allow to use this folder")
        return False
    
class CopyModel:
    @staticmethod
    def copy_and_organize_files_shamsi_order(src_folder, dest_folder):
        try:
            listdir = os.listdir(src_folder)
        except (FileNotFoundError, TypeError):
            return False
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

            dest_persian_month_folder = os.path.join(dest_ad_year_folder, f"{str(persian_month + 3 if persian_month < 10 else persian_month - 11)} {persian_month_name} {str(persian_year)}")
            if not os.path.exists(dest_persian_month_folder):
                os.makedirs(dest_persian_month_folder)
            
            result = _copy_machine(filename, src_file_path, dest_persian_month_folder)
            if not result:
                return False
        return True

    @staticmethod
    def copy_and_organize_files_georgian_order(src_folder, dest_folder):
        try:
            listdir = os.listdir(src_folder)
        except (FileNotFoundError, TypeError):
            return False
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            modification_date, ad_year, *other = _get_file_details(src_file_path)

            ad_month_name = modification_date.strftime("%B")

            dest_ad_year_folder = os.path.join(dest_folder, str(ad_year))
            if not os.path.exists(dest_ad_year_folder):
                os.mkdir(dest_ad_year_folder)

            dest_ad_month_folder = os.path.join(dest_ad_year_folder, str(ad_month_name))
            if not os.path.exists(dest_ad_month_folder):
                os.mkdir(dest_ad_month_folder)
            
            result = _copy_machine(filename, src_file_path, dest_ad_month_folder)
            if not result:
                return False
        return True

    @staticmethod
    def simple_bulk_copy(src_folder, dest_folder):
        try:
            listdir = os.listdir(src_folder)
        except (FileNotFoundError, TypeError):
            return False
        for filename in listdir:
            src_file_path = os.path.join(src_folder, filename)
            result = _copy_machine(filename, src_file_path, dest_folder)
            if not result:
                return False
        return True