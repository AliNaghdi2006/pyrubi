from typing import Optional

class ReplyTo:
	def __init__(self, reply_data: dict) -> None:
		self.__reply_data = reply_data 
	
	@property 
	def message_id(self) -> str:
		return self.__reply_data.get("message_id")
	
	@property
	def text(self) -> Optional[str]:
		return self.__reply_data.get("text")
	
	@property
	def author_guid(self) -> Optional[str]:
		return self.__reply_data.get("author_guid")
	
	def __dict__(self) -> dict:
		return self.__reply_data