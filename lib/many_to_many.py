class Author:
    all_authors = []


    def __init__(self, name):
        self.name = name
        self.books_list = []
        self.contract_list = []
        Author.all_authors.append(self)

    def contracts(self):
        print(self.contract_list)  # Add this line to check the contract_list
        return self.contract_list

    def books(self):
        pass

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contract_list.append(contract)
        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contract_list:
            total += contract.royalties
        return total





class Book:
   
    all_books=[]
    
    def __init__(self, title ):
        self.title = title 
        Book.all_books.append(self)

    def set_title(self, new_title):
        if isinstance(new_title, str):
            self.title = new_title
        else:
            raise ValueError('Invalid title format. Please provide a string.')



class Contract:
      
      all_contracts=[]

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

        Contract.all_contracts.append(self)


      def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
 
