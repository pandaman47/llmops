class Calculator:
    @staticmethod
    def multiply(a:int, b:int) -> int:
        """
        Multiply two integers
        
        Args:
            a(int): the first integer
            b(int): the second integer

        Returns:
            int: product of a and b
        """
        return a*b
    
    @staticmethod
    def calculate_total(*x:float) -> float:
        """
        calculate the sum of given list of numbers
        
        Args:
            x (float) : variable number of floating-point numbers

        Returns:
            float: sum of the list of numbers in x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float, days:int) -> float:
        """
        Calculate the daily budget given the total amount and duration

        args:
            total (float) : Total cost
            days (int) : Number of days

        Returns:
            float : Daily budget amount
        """
        return total/days if days > 0 else 0