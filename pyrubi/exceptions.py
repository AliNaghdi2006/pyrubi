class ClientException(Exception):
    pass

class FiltersException(Exception):
	pass
	
class InvalidAuth(ClientException):

    def __init__(self, message:str="You don't have access to request this method!"):
        super().__init__(message)

class NotRegistered(ClientException):

    def __init__(self, message:str="The account used is invalid or not registered!"):
        super().__init__(message)

class InvalidInput(ClientException):

    def __init__(self, message:str="Some input given to the method is invalid!"):
        super().__init__(message)

class TooRequests(ClientException):

    def __init__(self, message:str="You won't be able to use this method for a while!"):
        super().__init__(message)

class InvalidCommandsType(ClientException):
    def __init__(self, message:str="Commands must be a list of string or a string."):
        super().__init__(message)

class InvalidCommandsPrefixType(ClientException):
    def __init__(self, message:str="prefix must be string."):
        super().__init__(message)
