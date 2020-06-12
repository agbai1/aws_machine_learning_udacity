import pants from Pants

class SalesPerson:
    """
    The SalesPerson class represents a store employee

    """

    def __init__(self, first_name, last_name, employee_id, salary):
        """Method for initializing a SalesPerson object

        Args:
            first_name (str)
            last_name (str)
            employee_id (int)
            salary (float)

        Attributes:
            first_name (str): first name of the employee
            last_name (str): last name of the employee
            employee_id (int): identification number of the employee
            salary (float): annual salary of the employee
            pants_sold (list): a list of pants objects sold by the employee
            total_sales (float): sum of all sales made by the employee

        """

        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        """
        The sell_pants method appends a pants object to the pants_sold attribute

        Args:
            pants_object (obj): a pants object that was sold

        Returns: None

        """

        self.pants_sold.append(pants_object)

    def calculate_sales(self):
        """
        The calculate_sales method loops through a list of pants object and calculates the total sales on pants sold

        Args: None

        Returns: None

        """

        for pant in self.pants_sold:
            self.total_sales += pant.price
        return self.total_sales

    def display_sales(self):
        """
        The display_sales method prints out all the pants sold

        Args: None

        Returns: None

        """

        for pant in self.pants_sold:
            print("color: {}, waist_size: {}, length: {}, price: {}".format(pant.color, pant.waist_size, pant.length, pant.price))


    def calculate_commission(self, percentage):
        """
        The calculate_commission method returns commission based on sales made

        Args:
            percentage (float): the commission percentage as a decimal

        Returns:
            float: the commission due
        """
        return self.calculate_sales() * percentage
