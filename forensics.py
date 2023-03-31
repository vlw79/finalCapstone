#This program will take in a file and return the metadata on it

import os
from datetime import datetime

#Function to extract metadata
def file_metadata(file):
    metadata = {}
    data = os.stat(file)
    size = data.st_size
    metadata.update({"size (bytes)": size})
    acc_time = data.st_atime
    access_time = datetime.fromtimestamp(acc_time)
    metadata.update({"recent access time": str(access_time)})
    mod_time = data.st_mtime
    modification_time = datetime.fromtimestamp(mod_time)
    metadata.update({"recent modification time": str(modification_time)})
    met_change = data.st_ctime
    metadata_change = datetime.fromtimestamp(met_change)
    metadata.update({"recent metadata change": str(metadata_change)})
    file_permission = oct(data.st_mode)[-3:]
    metadata.update({"file permissions": file_permission})
    directory_entry = data.st_nlink
    metadata.update({"number directory entries": directory_entry})
    user_id = data.st_uid
    metadata.update({"user identifier of file owner": user_id})
    group_id = data.st_gid
    metadata.update({"group identifier of file owner": group_id})
#Display metadata in clear and organised way
    print()
    for x in metadata:
        print(x, ':', metadata[x])
    print()
    
#User inputs file to be have metadata extracted
file = input('Please enter file: ') #'CS T50 - Test File.docx'
results = file_metadata(file)