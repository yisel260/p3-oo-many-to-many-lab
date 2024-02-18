

class Author:
    all_authors = []


    def __init__(self, name):
        self.name = name
        self.books_list = []
        self.contract_list = []
        Author.all_authors.append(self)

    def contracts(self):
        print(Contract.all)
        return [contract for contract in Contract.all if contract.author == self ]
    

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self ]
    

       
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contract_list.append(contract)
        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
           total += contract.royalties
        return total



class Book:
   
    all_books=[]
    
    def __init__(self, title ):
        self.title = title 
        Book.all_books.append(self)

    def contracts(self):
      return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
       return [contract.author for contract in Contract.all if contract.book == self]
    
class Contract:
      
      all=[]

      def __init__(self, author, book, date, royalties ):
        if isinstance( book, Book ):
           self.book = book
        else:
           raise ValueError("Book must be and instance of Book")
        if isinstance( author, Author ):
           self.author = author
        else:
           raise ValueError("Author must be and instance of Author") 
        if isinstance( date, str ):
           self.date = date 
        else:
           raise ValueError("Date must be a string")
        if isinstance( royalties, int ):
           self.royalties = royalties
        else:
           raise ValueError("Royalties must be an integer")

        Contract.all.append(self)
        
      @classmethod
      def contracts_by_date(cls, date):
         return [contract for contract in cls.all if contract.date == date]
      