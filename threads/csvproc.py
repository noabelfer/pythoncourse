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
        self._filename = os.path.basename(csvpath) 
        self._dir_path:str = self.__csvpath.replace(self._filename,'')
        self.filename = self._filename.replace(".csv","")
        with open(csvpath, 'r') as f:
            rcsv = csv.DictReader(f)
            self.__csvdict = {}
            self.__years = {}
            curr_year = 0
            for k,v in enumerate(rcsv):
                self.__csvdict[k] = v
                d = v['Date']
                date = datetime.strptime(v['Date'], "%d-%m-%Y")

                if(date.year != curr_year):
                    self.__years[date.year] = k
                    curr_year = date.year
            print(self.__years)
            f.close()
                

if __name__ == '__main__':
    a = Csvmanage('data\AAPL.csv')