#!/usr/bin/env python

import os
import pathlib
from textfile import TextFile

class TxtFile(TextFile):
    def __init__(self,path:str):
        super().__init__(path)
        if not self._exist:
            raise Exception(f"File {path} does not exist!")
        if self._suffix != ".txt":
            raise Exception(f"File {path} is not a text file!")
            
    def __repr__(self):
        return f'TxtFile({self._path})'
        
    def get_content(self)->str:
        self._open()
        st = self._file_handle.read()
        self._file_handle.close()
        return st
        
    def __add__(self,path:str):
        toadd = TxtFile(path)
        st = self.get_content() + toadd.get_content()
        fname = self._dir_path + self.filename + '_' + toadd.filename + '.txt'
        fh = open(fname,"wt")
        fh.write(st)
        fh.close()
        added = TextFile(fname)
        return added
        

abc = TxtFile('c:\\temp\\noa\\pythoncourse\\files\\aaa.txt')
print(abc)   
print(repr(abc))  
print('file size: ',abc.get_file_size()) 
# print(abc.get_content())
ddd = abc.__add__('c:\\temp\\noa\\pythoncourse\\files\\bbb.txt')
print('file size: ',ddd.get_file_size()) 
