# create a class computer with max price as a private property . create a method sell to display the selling price and a methos set max price to change the private attribute max price and create an object computre and try changing the max price and use the sell function to display the updated price
class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"THE SELLING PRICE IS {self.__maxprice}")
    def setmaxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(2000)
c.sell()