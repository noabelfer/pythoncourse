import os

def fill_space(count):
    st = ""
    for i in range(count):
        st +=' '
    return st
    
def dict_2_str(mydic:dict,offset:int)->str:
    st:str = "" 
    for key,values in mydic.items():
        st += fill_space(offset)
        # for i in range(offset):
            # st +=' '

        st += key+' : '
        if isinstance(values,dict):
            st += "{\n"
            st += dict_2_str(values,offset+4)
            st += fill_space(offset)
            st += "}\n"
        elif isinstance(values,list):
            st += "[\n"
            for l in values:
                st += fill_space(offset+4)
                st += l
                st += ",\n"
            st += fill_space(offset+4)
            st += "]\n"
        else:
            st += str(values)
            st += "\n"
    return st
    
def search_path(path:str):
    files_dict = {}
    files_and_dirs = os.listdir(path)
    files_list = []
    dir_list = []
    

    for name in files_and_dirs:
        if(os.path.isdir(os.path.join(path, name))):
            if(files_dict == {}):
                files_dict['dirs'] = {}
            d = search_path(os.path.join(path, name))
            if(d != {}):
                files_dict['dirs'][name] = d
            else:
                files_dict['dirs'][name] = {}
            dir_list.append(name)
        else:
            files_list.append(name)

    if(files_list != []):
        files_dict['files'] = files_list
    if(files_list == [] and dir_list == []):
        return {}
    return files_dict
        
if __name__ == '__main__':
    d = search_path('..')
    print('--------------------------- dict -----------------------')
    print(dict_2_str(d,4))
