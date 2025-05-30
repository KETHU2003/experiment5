class Book:
     def __init__(self,title):
           self.title=title
def create_book_list():
    return[Book("python 101"),Book("ai basics"),Book("datascience")]
books=create_book_list()
for b in books:
      print("Book title:",b.title)
                        
                       
            
