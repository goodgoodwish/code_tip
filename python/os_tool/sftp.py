import pysftp
import datetime
from datetime import date
import zipfile
import os
import glob
import sys
sys.path.insert(0, "/Users/charliezhu/work/code_tip/python")
from db import DbTool

db_name = "local_db"
local_path = "/Users/charliezhu/app/bw/responsys/raw/"

event_type = {"COMPLAINT", "SENT", "FAIL", "BOUNCE", "CLICK", "OPEN", "CONVERT", "SKIPPED"}
copy_cmd = {}
copy_cmd["SENT"] = "copy email_metrics_sent_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID,dynamic_content_signature_id)) "
copy_cmd["CLICK"] = "copy email_metrics_click_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID)) "
copy_cmd["OPEN"] = "copy email_metrics_open_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID)) "
copy_cmd["SKIPPED"] = "copy email_metrics_skipped_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID,offer_signature_id,dynamic_content_signature_id)) "
copy_cmd["COMPLAINT"] = "copy email_metrics_complaint_stg FROM STDIN with (FORMAT CSV, HEADER true, Null 'unknown', FORCE_NULL(CUSTOMER_ID)) "
copy_cmd["BOUNCE"] = "copy email_metrics_bounce_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID)) "
copy_cmd["FAIL"] = "copy email_metrics_fail_stg FROM STDIN with (FORMAT CSV, HEADER true, FORCE_NULL(CUSTOMER_ID,offer_signature_id,dynamic_content_signature_id)) "
copy_cmd["CONVERT"] = ""

def get_files():
    """
    get raw email matrics from responsys sftp server,
    """
    today_date = date.today()
    file_date = today_date + datetime.timedelta(days=-2)
    file_date_str = "{:%Y%m%d}".format(file_date) # example: 2018-07-20
    curt_files = []

    with pysftp.Connection(host="files.responsys.net",
                        username="blastwork_scp",
                        private_key="/Users/charliezhu/.ssh/rn_games_responsys_id_rsa",
                        ) as sftp:
        sftp.chdir('download')
        files = sftp.listdir()
        for file in files:
            if file.find(file_date_str) > 0:
                sftp.get(remotepath = file, localpath = local_path + file)
                print(file)
                curt_files.append(file)
            if file == "v2-Slingo_arcade_users.zip":
                sftp.get(remotepath = file, localpath = local_path + file)
                print(file)
                curt_files.append(file)
    return curt_files

def unzip_files(curt_files):
    """
    unzip files, rename user_id.csv
    """
    os.chdir(local_path)
    print(os.getcwd())

    for file in curt_files:
        print(f"Unzip file {file} ... ")
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(local_path)

    os.rename("v2-Slingo_arcade_users", "user_id.csv")

    csv_files = []
    for file in curt_files:
        csv_files.append(file[:-4])
    return csv_files

def load_csv(csv_file, event_type, ftp_date, db="local_db"):
    """
    load csv per topic,
    """
    csv_db = DbTool("/Users/charliezhu/app/box/aws/database.ini")
    # list files
    csv_dir = local_path

    stg_table = "email_metrics_" + event_type + "_stg"

    export_date = ftp_date
    # truncate interim table,
    csv_db.run_sql(f"truncate table {stg_table} ", db_name=db)
    # load data into interim table
    full_file_name = csv_file
    # print(full_file_name)
    with open(full_file_name, "r", encoding="utf-8") as file:
        print(":")
        csv_db.psql_copy_raw(file, copy_cmd[event_type], stg_table, db_name=db_name)
    # insert into target with export date
    target_table = "email_metrics_raw_sum"
    sql = f"delete from {target_table} where ds = '{export_date}' "
    print(sql)
    # csv_db.run_sql(sql, db_name=db)
    sql = f"""insert into {target_table} select '{export_date}'::date, campaign_id, 'type'
            , count(*)
        from {stg_table} 
        group by campaign_id
    """
    print(sql)
    # csv_db.run_sql(sql, db_name=db)
    # move file to archive folder
    archive_file = os.path.join(csv_dir + "/archive/" + os.path.basename(csv_file))
    print(archive_file)
    # os.rename(full_file_name, archive_file)

def load_metrics():
    csv_dir = local_path
    files = [f for f in glob.glob(csv_dir+"/*20181002*.txt")]
    for file in files:
        if file.find("CONVERT") > 0:
            continue
        print(file)
        file_attr = file.split("_")
        event_type = file_attr[1]
        date_str = file_attr[2][:4] + "-" + file_attr[2][4:6] + "-" + file_attr[2][6:]
        load_csv(file, event_type, date_str)

    csv_db = DbTool("/Users/charliezhu/app/box/aws/database.ini")
    with open(local_path + "/user_id.csv", "r", encoding="utf-8") as file:
        print(":")
        csv_db.psql_copy(file=file, table = "email_metrics_user_id", db_name=db_name)


def main():
    # curt_files = get_files()
    # curt_files = unzip_files(curt_files)
    load_metrics()

if __name__ == '__main__':
    main()
