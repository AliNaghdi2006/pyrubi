
class LiveStatus:
	def __init__(self, live_status_data: dict) -> None:
		self.__live_status_data = live_status_data 
	
	@property
	def status(self) -> str:
		return self.__live_status_data["status"]
	
	@property
	def play_count(self) -> int:
		return self.__live_status_data["play_count"]
	
	@property
	def allow_comment(self) -> bool:
		return self.__live_status_data["allow_comment"]
	
	@property
	def can_play(self) -> bool:
		return self.__live_status_data["can_play"]
	
	@property
	def timestamp(self) -> str:
		return self.__live_status_data["timestamp"]
	
	def __dict__(self) -> dict:
		return self.__live_status_data

class Live:
	def __init__(self, live_data: dict) -> None:
		self.__live_data = live_data 
	
	@property
	def live_id(self) -> str:
		return self.__live_data["live_id"]
	
	@property
	def thumb_inline(self) -> str:
		return self.__live_data["thumb_inline"]
	
	@property
	def access_token(self) -> str:
		return self.__live_data["access_token"]
	
	@property
	def live_status(self) -> LiveStatus:
		return LiveStatus(self.__live_data["live_status"])
	
	def __dict__(self) -> dict:
		return self.__live_data