import csv
import os
import pathlib
from datetime import datetime
import concurrent.futures

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
            self.__years = {}
            curr_year = 0
            # loop of constructing self.__years dictinary 
            #   self.__years dictinary = {
            #                              1980: [list of rows belong to 1980],
            #                              1981: [list of rows belong to 1981]
            #                              ........
            #                              2020:  [list of rows belong to 2020]
            #
            for csvrecord in rcsv:
                # get the date in order to extract date.year
                date = datetime.strptime(csvrecord['Date'], "%d-%m-%Y")
                # here we detect year change
                if(date.year != curr_year):
                    #create new entry in self.__years for date.year
                    self.__years[date.year] = []
                    curr_year = date.year
                self.__years[curr_year].append(csvrecord)
            print(self.__years.keys())
            print(self.__years[curr_year][0])
            f.close()
                
    def create_year_file(self,year:int)->int:
        # prepare file name full path
        path = self._dir_path+ self.__filename + '_' + str(year) + '.csv'
        print("started "+str(year) + " create file: "+path)
        # Prepare output file
        fh = open(path,"w",newline='')      
        keysList = [key for key in self.__years[year][0].keys()]
        w = csv.DictWriter(fh,fieldnames=keysList)
        w.writeheader()
        #prepare average line to be written at end of file 
        average_line = {}
        for c in range (len(keysList)):
            average_line[keysList[c]] = float(0)
        average_line[keysList[0]] = 'Average' 
        # loop of writing all rows belong to year
        for v in self.__years[year]:
            w.writerow(v)
            #sum average line columns
            for c in range (1,len(keysList)):
                average_line[keysList[c]] += float(v[keysList[c]])
        #now the average line is divided by length to get average values 
        for c in range (1,len(keysList)):
            average_line[keysList[c]] /= len(self.__years[year])
        #write the average line 
        w.writerow(average_line)
        fh.close()
        print("ended "+str(year) +" create file: "+path)
        return year

    def run_as_threads(self):
        first_year = list(self.__years.keys())[0]
        last_year = list(self.__years.keys())[-1]
        print('first_year '+str(first_year)+' last_year '+str(last_year))
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            results = [executor.submit(self.create_year_file, i) for i in range(first_year,last_year+1)]
        
        executor.shutdown()
        for f in concurrent.futures.as_completed(results):
            print(f.result())
if __name__ == '__main__':
    a = Csvmanage('data\AAPL.csv')
    a.run_as_threads()