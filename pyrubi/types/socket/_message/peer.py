from .chat_types import ChatTypes

class Peer:
	def __init__(self, peer_data: dict) -> None:
		self.__peer_data = peer_data[0]
	
	@property
	def type(self) -> ChatTypes:
		type = self.__peer_data["type"]
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
		return self.__peer_data["object_guid"]
	
	def __dict__(self) -> dict:
		return self.__peer_data