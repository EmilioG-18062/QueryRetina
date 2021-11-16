import pysftp
import glob
import os.path

folder_path = r'D:\PycharmProjects\QueryRetina'
file_type = '\*py'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

print(max_file)

myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(myHostname, username=myUsername, password=myPassword) as sftp:
    localFilePath = max_file
    remoteFilePath = '/var/integraweb-db-backups/TUTORIAL2.txt'

    sftp.put(localFilePath, remoteFilePath)
