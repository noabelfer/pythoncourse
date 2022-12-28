from valeria_ebook import EBook


class MyeBook(EBook):
    def __init__(self, book_path: str, words_num: int,start_page=0):
        super().__init__(book_path,words_num)
        self.__page_number = start_page 
        if(start_page >= self.get_total_pages()):
            raise ValueError(f'Page {start_page} is out of range of <{self.get_total_pages()}>')
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if(self.__page_number >= self.get_total_pages()):
            raise StopIteration
        self.__page_number += 1
        return self
        
   #     return self
    
    def __str__(self):
        return self.get_page_content(self.__page_number)
        
        
if __name__ == '__main__':
    book = MyeBook('data/alice_in_wonderland.txt', 1000,25)
    i = 0
    for page in book:
        print('======================='+str(i)+'====================================')
        print(page)
        i += 1
 
