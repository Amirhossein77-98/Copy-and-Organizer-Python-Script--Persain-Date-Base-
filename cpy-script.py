import os
import shutil
from datetime import datetime
import jdatetime
import logging

logging.basicConfig(filename='copy.log', level=logging.INFO)

def copy_files(src_folder, dest_folder):
    for filename in os.listdir(src_folder):
        src_file_path = os.path.join(src_folder, filename)
        modification_time = os.path.getmtime(src_file_path)
        modification_date = datetime.fromtimestamp(modification_time)
        ad_year = modification_date.year
        ad_month = modification_date.month
        ad_day = modification_date.day
        persian_date = jdatetime.date.fromgregorian(year=ad_year, month=ad_month, day=ad_day)

        persian_year = persian_date.year
        persian_month = persian_date.month
        persian_day = persian_date.day

        ad_month_name = modification_date.strftime("%B")
        persian_month_name = persian_date.strftime("%B")

        dest_ad_year_folder = os.path.join(dest_folder, str(ad_year))

        if not os.path.exists(dest_ad_year_folder):
            os.makedirs(dest_ad_year_folder)

        dest_persian_month_folder = os.path.join(dest_ad_year_folder, f"{str(persian_month + 3 if persian_month < 10 else persian_month - 11)} {persian_month_name} {str(persian_year)}")
        if not os.path.exists(dest_persian_month_folder):
            os.makedirs(dest_persian_month_folder)
        
        log_message = f"{datetime.now()} - Copying {filename} to {dest_persian_month_folder}"
        print(log_message)
        logging.info(log_message)

        shutil.copy2(src_file_path, dest_persian_month_folder)


src_folder = "E:\Camera"
dest_folder = "E:\Personal"

copy_files(src_folder, dest_folder)