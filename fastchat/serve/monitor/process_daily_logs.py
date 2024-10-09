import schedule
import os
import subprocess

def get_logs() -> None:
    date = datetime.date.today()
    day = "{:02d}".format(date.day)
    month = "{:02d}".format(date.month)
    file_name = f"{date.year}-{month}-{date.day}-conv.json"
    az_path = "C:\Users\aalothaimen\Downloads\azcopy_windows_amd64_10.24.0\azcopy_windows_amd64_10.24.0"
    storage_location = "https://allamllmuksstandard.blob.core.windows.net/allam-safetySafety_round2/original_files/Chatarena_logs"
    sas_token = os.environ['SAS_TOKEN']
    src_location = f"{storage_location}/{file_name}?{sas_token}
    des_location = "C:\Users\aalothaimen\Documents\Work\Allam\FastChat\data"
    cmd = f"{az_path} azcopy cp {storage_location} {des_location}"
    subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)


schedule.every().minute.do(job)
while True:
    schedule.run_pending()