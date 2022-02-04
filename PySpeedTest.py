import speedtest
from datetime import datetime

download_speed = speedtest.Speedtest().download()
dspd = round(download_speed / 2 ** 20, 2)
print('DownloadSpd = ', dspd, ' Mbps')

upload_speed = speedtest.Speedtest().upload()
uspd = round(upload_speed / 2 ** 20, 2) 
print('UploadSpd   = ', uspd, ' Mbps')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(dt_string)