import speedtest
from datetime import datetime

f = open("speedtest.txt","a")

download_speed = speedtest.Speedtest().download()
dspd = round(download_speed / 2 ** 20, 2)
dl_out = 'DownloadSpd = ' + str(dspd) + ' Mbps'
print(dl_out)
f.write(dl_out + '\n') 

upload_speed = speedtest.Speedtest().upload()
uspd = round(upload_speed / 2 ** 20, 2) 
ul_out = 'UploadSpd   = ' + str(uspd) + ' Mbps' 
print(ul_out)
f.write(ul_out + '\n')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(dt_string)
f.write(dt_string + '\n\n')

f.close()
