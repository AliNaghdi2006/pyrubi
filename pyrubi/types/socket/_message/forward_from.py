from .chat_types import ChatTypes

class ForwardFrom:
	def __init__(self, forward_data: dict) -> None:
		self.__forward_data = forward_data 
	
	@property
	def type_from(self) -> ChatTypes:
		type = self.__forward_data.get("type_from")
		types = {
        	"User": ChatTypes.User,
            "Group": ChatTypes.Group,
            "Channel": ChatTypes.Channel,
            "Bot": ChatTypes.Bot
        }
		return types.get(
			type, type 
		)
	
	@property
	def message_id(self) -> str:
		return self.__forward_data.get("message_id")
	
	@property
	def object_guid(self) -> str:
		return self.__forward_data.get("object_guid")
	
	def __dict__(self) -> dict:
		return self.__forward_data