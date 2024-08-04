class Date:
    def __init__(self,day,month,year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def display(self)->str:
        return f"{self.day}/{self.month}/{self.year}"


