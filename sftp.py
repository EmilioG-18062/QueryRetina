import pysftp
import glob
import os.path

folder_path = r'D:\PycharmProjects\QueryRetina'
file_type = '\*py'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
folder_path = "{0}\\".format(folder_path)
file = max_file.replace(folder_path, '')


myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(myHostname, username=myUsername, password=myPassword) as sftp:
    localFilePath = max_file
    remoteFilePath = f'/var/integraweb-db-backups/{file}'

    sftp.put(localFilePath, remoteFilePath)
