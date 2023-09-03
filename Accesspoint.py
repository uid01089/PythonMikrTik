# Importing the MikrotikRouter class from the MikrotikRouter module
from MikrotikRouter import MikrotikRouter

# Defining a new class named Accesspoint which is a subclass of MikrotikRouter
class Accesspoint(MikrotikRouter):
    """
    This class represents an Access Point that inherits properties and methods from the MikrotikRouter class.
    """
    
    # The constructor method for the Accesspoint class
    def __init__(self, ipAddr: str, user: str, passwd: str) -> None:
        """
        Initializes a new instance of the Accesspoint class.
        
        Parameters:
        ipAddr (str): The IP address of the router.
        user (str): The username used for authentication.
        passwd (str): The password used for authentication.
        
        Returns:
        None
        """
        
        # Calling the constructor of the parent class
        super().__init__(ipAddr, user, passwd)
