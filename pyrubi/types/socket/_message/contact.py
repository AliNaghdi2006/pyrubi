from typing import Optional

class Contact:
	def __init__(self, contact_data: dict) -> None:
		self.__contact_data = contact_data 
	
	@property
	def phone_number(self) -> str:
		phone_number: str = self.__contact_data["phone_number"]
		return phone_number.replace("-", "")
	
	@property
	def first_name(self) -> Optional[str]:
		first_name = self.__contact_data["first_name"]
		return first_name if first_name else None
	
	@property
	def last_name(self) -> Optional[str]:
		last_name = self.__contact_data["first_name"]
		return last_name if last_name else None 
	
	@property
	def vcard(self) -> str:
		return self.__contact_data["vcard"]
	
	def __dict__(self) -> dict:
		return self.__contact_data