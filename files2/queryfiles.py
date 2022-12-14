import os
import json

    
def search_path(path:str)->dict:
    files_dict = {}
    files_and_dirs = os.listdir(path)
    files_list = []

    for name in files_and_dirs:
        if(os.path.isdir(os.path.join(path, name))):
            if(files_dict == {}):
                files_dict['dirs'] = {}
            files_dict['dirs'][name] = search_path(os.path.join(path, name))
        else:
            files_list.append(name)

    if(files_list != []):
        files_dict['files'] = files_list
 
    return files_dict

def store_path(path:str,json_path=None)->dict:
    dict = search_path(path)
    if((json_path != None) and os.path.exists(json_path)):
        path = os.path.join(json_path, "files.json")
        json_data = json.dumps(dict,indent=4, separators=(',', ': '))
        with open(path, 'w') as f:
            f.write(json_data)
            f.close()
    return dict
    
if __name__ == '__main__':
    d = store_path('.',"c:\\temp")
    json_data = json.dumps(d,indent=4, separators=(',', ': '))
    print('--------------------------- dict -----------------------')
    print(json_data)
