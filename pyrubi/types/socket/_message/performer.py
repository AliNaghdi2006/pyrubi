from .chat_types import ChatTypes

class Performer:
	def __init__(self, performer_data: dict) -> None:
		self.__performer_data = performer_data 
	
	@property
	def type(self) -> ChatTypes:
		type = self.__performer_data["type"]
		types = {
        	"User": ChatTypes.User,
            "Group": ChatTypes.Group,
            "Channel": ChatTypes.Channel,
            "Bot": ChatTypes.Bot,
        }
		return types.get(
			type , type 
		)
	
	@property 
	def object_guid(self) -> str:
		return self.__performer_data["object_guid"]
	
	def __dict__(self) -> dict:
		return self.__performer_data