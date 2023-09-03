# Importing the MikrotikRouter class from the MikrotikRouter module
from MikrotikRouter import MikrotikRouter

# Defining a new class named CentralRouter which is a subclass of MikrotikRouter
class CentralRouter(MikrotikRouter):
    """
    This class represents a Central Router that inherits properties and methods from the MikrotikRouter class.
    """
    
    # The constructor method for the CentralRouter class
    def __init__(self, ipAddr: str, user: str, passwd: str) -> None:
        """
        Initializes a new instance of the CentralRouter class.
        
        Parameters:
        ipAddr (str): The IP address of the router.
        user (str): The username used for authentication.
        passwd (str): The password used for authentication.
        
        Returns:
        None
        """
        
        # Calling the constructor of the parent class
        super().__init__(ipAddr, user, passwd)
