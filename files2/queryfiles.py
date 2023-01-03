import os
import json

    
def search_path(path:str)->dict:
    files_dict = {}
    files_and_dirs = os.listdir(path)
    files_list = []
    dir_list = []
    

    for name in files_and_dirs:
        if(os.path.isdir(os.path.join(path, name))):
            if(files_dict == {}):
                files_dict['dirs'] = {}
            files_dict['dirs'][name] = search_path(os.path.join(path, name))
            dir_list.append(name)
        else:
            files_list.append(name)

    if(files_list != []):
        files_dict['files'] = files_list
 
    return files_dict
        
if __name__ == '__main__':
    d = search_path('.')
    json_data = json.dumps(d,indent=4, separators=(',', ': '))
    print('--------------------------- dict -----------------------')
    print(json_data)
