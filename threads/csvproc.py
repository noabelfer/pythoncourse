import csv
import os
import pathlib
from datetime import datetime

class Csvmanage:
    def __init__(self,csvpath:str):        
        self.__exist:bool = os.path.exists(csvpath)
        self.__csvpath = csvpath
        if(not self.__exist):
            raise ValueError(f' file {csvpath} not exist!')
        self._suffix:str = pathlib.Path(csvpath).suffix
        self.__filename = os.path.basename(csvpath) 
        self._dir_path:str = self.__csvpath.replace(self.__filename,'')
        self.__filename = self.__filename.replace(".csv","")
        with open(csvpath, 'r') as f:
            rcsv = csv.DictReader(f)
            self.__csvdict = {}
            self.__years = {}
            curr_year = 0
            n = 0 
            start_year = 0
            for k,v in enumerate(rcsv):
                self.__csvdict[k] = v
                date = datetime.strptime(v['Date'], "%d-%m-%Y")
                if(curr_year == 0):
                    curr_year = date.year
                if(date.year != curr_year):
                    self.__years[curr_year] = (start_year,n)
                    curr_year = date.year
                    start_year = k
                    n = 0
                n += 1
            print(self.__years)
            print(self.__csvdict[0])
            f.close()
                
    def create_year_file(self,year:int):
        path = self._dir_path+ self.__filename + '_' + str(year) + '.csv'
        start_row = self.__years[year][0]
        n_rows = self.__years[year][1]
        print(start_row,n_rows)
        fh = open(path,"w",newline='')      
        keysList = [key for key in self.__csvdict[0].keys()]
        print('keysList ',keysList)
        w = csv.DictWriter(fh,fieldnames=keysList)
        w.writeheader()
        average_line = {}
        for c in range (len(keysList)):
            average_line[keysList[c]] = 0
        average_line[keysList[0]] = self.__csvdict[start_row][keysList[0]]
        for l in range(start_row,start_row+n_rows) :
            w.writerow(self.__csvdict[l])
            for c in range (1,len(keysList)):
                fdst = float(average_line[keysList[c]])
                print('fdst '+str(fdst));
                fsrc = float(self.__csvdict[l][keysList[c]])
                print("fsrc "+str(fsrc))
                average_line[keysList[c]] = fdst + fsrc
        for c in range (1,len(keysList)):
            average_line[keysList[c]] /= n_rows
 #           average_line[keysList[c]] = str(average_line[c])
        print('average_line '+str(average_line))
        w.writerow(average_line)
        fh.close()
        
if __name__ == '__main__':
    a = Csvmanage('data\AAPL.csv')
    a.create_year_file(1983)