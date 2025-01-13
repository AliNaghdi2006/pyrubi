from typing import Optional
from .chat_types import ChatTypes

class Chat:
	def __init__(self, chat_data: dict) -> None:
		self.__chat_data = chat_data 
	
	@property
	def count_unseen(self) -> int:
		return self.__chat_data["chat"]["count_unseen"]
	
	@property
	def author_type(self) -> str:
		return self.__chat_data["chat"]["last_message"]["author_type"]
	
	@property 
	def author_guid(self) -> str:
		return self.__chat_data["chat"]["last_message"]["author_object_guid"]

	@property
	def author_title(self) -> Optional[str]:
		return self.__chat_data["chat"]["last_message"].get("author_title")
	
	@property
	def time_string(self) -> str:
		return self.__chat_data["chat"]["time_string"]
	
	@property
	def type(self) -> ChatTypes:
		type = self.__chat_data["type"]
		types = {
        	"User": ChatTypes.User,
            "Group": ChatTypes.Group,
            "Channel": ChatTypes.Channel,
            "Bot": ChatTypes.Bot,
        }
		return types.get(
			type, type 
		)
	
	@property
	def last_seen_peer_mid(self) -> str:
		return self.__chat_data["chat"]["last_seen_peer_mid"]
	
	@property
	def status(self) -> str:
		return self.__chat_data["chat"]["status"]
	
	@property
	def object_guid(self) -> str:
		return self.__chat_data["object_guid"]	
	
	def __dict__(self) -> dict:
		return self.__chat_data