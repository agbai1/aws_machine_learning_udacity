class Shirt:
    """The Shirt class represents an article of shirts sold in a store
    """
    def __init__(self,color, size, style, price):
        """Method for initializing a Shirt object

        Args:
            color (str)
            size (int)
            style (str)
            price (float)

        Attributes:
            color (str): color of a shirt object
            size (str):  size of a shirt object
            style (str): style of a shirt object
            price (float): price of a shirt object
        """
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def set_price(self, new_price):
        """The set_price method changes the price attribute of a shirt object

        Args:
            new_price (float): the new price of the shirt object

        Returns: None

        """
        self.price = new_price

    def set_color(self, new_color):
        """The set_color method changes the color attribute of a shirt object

        Args:
            new_color (float): the new color of the shirt object

        Returns: None

        """
        self.color = new_color

    def set_style(self, new_style):
        """The set_style method changes the style attribute of a shirt object

        Args:
            new_style (float): the new style of the shirt object

        Returns: None

        """
        self.style = new_style

    def set_size(self, new_size):
        """The set_size method changes the size attribute of a shirt object

        Args:
            new_size (float): the new size of the shirt object

        Returns: None

        """
        self.size = new_size

    def get_price(self):
        """The get_price method returns the price attribute of a shirt object

        Args:
            None

        Returns:
            float: the price of shirt object

        """
        return self.price

    def discount(self, discount):
        """The discount method outputs a discounted price of a shirt object

        Args:
            discount (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - discount)

    def get_color(self):
        """The get_color method returns the color attribute of a shirt object

        Args:
            None

        Returns:
            float: the color of shirt object

        """
        return self.color

    def get_style(self):
        """The get_style method returns the style attribute of a shirt object

        Args:
            None

        Returns:
            float: the style of shirt object

        """
        return self.style

    def get_size(self):
        """The get_size method returns the size attribute of a shirt object

        Args:
            None

        Returns:
            float: the size of shirt object

        """
        return self.size
