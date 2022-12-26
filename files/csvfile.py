#!/usr/bin/env python

import os
import pathlib
import csv
from textfile import TextFile

class CsvFile(TextFile):
    def __init__(self,path:str):
        super().__init__(path)
        if not self._exist:
            raise Exception(f"File {path} does not exist!")
        if self._suffix != ".csv":
            raise Exception(f"File {path} is not a csv file!")
            
    def __repr__(self):
        return f'CsvFile({self._path})'
        
    def get_content(self)->dict:
        self._open()
        d = {}
        # rcsv = csv.reader(self._file_handle, delimiter=',', quotechar='|')
        rcsv = csv.DictReader(self._file_handle)
        for k,v in enumerate(rcsv):
            d[k] = v
        self._file_handle.close()
        return d
    
    def  get_rows_num(self)->int:
        d = self.get_content()
        return len(d)
        
    def  get_columns_num(self)->int:
        d = self.get_content()
        return len(d[0])
      
    def get_row(self,rownum:int)->dict:
        d = self.get_content()
        if(rownum >= len(d)):
            raise 'Row is out of range!'
        row = d[rownum]
        rd = {}
        for r,v in enumerate(row):
            rd[r] = v
        return rd
        
    def get_column(self,colnum:int)->list:
        if(colnum > self.get_columns_num()):
             raise 'Col is out of range!'
        d = self.get_content()
        collist = []
        for row in d:
            a = list(d[row])
            b = d[row][a[colnum]]
            collist.append(b)
        return collist

        
    def __add__(self,toadd):
        src_dict = self.get_content() 
        added_dict = toadd.get_content()
        fname = self._dir_path+ self.filename + '_' + toadd.filename + '.csv'
        # if os.path.exists(fname):
            # raise Exception(f'File {fname} exists!')
        last_key = list(src_dict.keys())[-1]
        print('last_key ',last_key)
        start = last_key + 1
        
        for item in added_dict:
            src_dict[start] = added_dict[item]
            start += 1 
        fh = open(fname,"w",newline='')      
        keysList = [key for key in src_dict[last_key].keys()]
        print('keysList ',keysList)
        w = csv.DictWriter(fh,fieldnames=keysList)
        w.writeheader()
        for l in src_dict:
            w.writerow(src_dict[l])
        fh.close()
        c = CsvFile(fname)
        return c

        
  
            
# aaa = CsvFile('c:\\temp\\noa\\pythoncourse\\files\\apl1.csv')
# bbb = CsvFile('c:\\temp\\noa\\pythoncourse\\files\\apl2.csv')
# ccc = aaa +bbb 
# print(ccc.get_content())
# exit()
# # print(aaa.get_content())
# print('get_rows_num ',aaa.get_rows_num())
# print('get_columns_num ',aaa.get_columns_num())
# print(' row 20 ',aaa.get_row(20))
# print(' col 5 ',aaa.get_column(5))
# # print(abc.get_content())
# ddd = abc.__add__('c:\\temp\\noa\\pythoncourse\\files\\bbb.txt')
# print('file size: ',ddd.get_file_size()) 
