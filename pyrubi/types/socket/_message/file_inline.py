from typing import Optional
from .file_types import FileTypes

class FileInline:
	def __init__(self, file_inline_data: dict) -> None:
		self.__file_inline_data = file_inline_data
		
	@property
	def file_id(self) -> int:
		return self.__file_inline_data["file_id"]
	
	@property
	def mime(self) -> str:
		return self.__file_inline_data["mime"]
	
	@property
	def dc_id(self) -> int:
		return self.__file_inline_data["dc_id"]
	
	@property
	def access_hash_rec(self) -> str:
		return self.__file_inline_data["access_hash_rec"]
	
	@property
	def file_name(self) -> str:
		return self.__file_inline_data["file_name"]
	
	@property
	def width(self) -> int:
		return self.__file_inline_data["width"]
	
	@property
	def height(self) -> int:
		return self.__file_inline_data["height"]
	
	@property
	def time(self) -> int:
		return self.__file_inline_data["time"]
	
	@property
	def size(self) -> int:
		return self.__file_inline_data["size"]
	
	@property
	def type(self) -> FileTypes:
		types = {
			"Video": FileTypes.Video,
			"Image": FileTypes.Image,
			"Voice": FileTypes.Voice,
			"File": FileTypes.File,
			"Gif": FileTypes.Gif
		}
		type = self.__file_inline_data["type"]
		return types.get(type, type)
	
	@property
	def is_round(self) -> bool:
		return self.__file_inline_data["is_round"]
	
	@property
	def is_spoil(self) -> bool:
		return self.__file_inline_data["is_spoil"]
	
	def __dict__(self) -> dict:
		return self.__file_inline_data