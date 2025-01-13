from pyrubi import Client
from pyrubi.types import Message
from pyrubi.enums import (
	MessageTypes, EventTypes, ChatTypes
)
from pyrubi.exceptions import (
	InvalidCommandsPrefixType,
	InvalidCommandsType
)
from typing import Optional, Union, List
from re import search, match

__all__ = (
	"commands",
	"text",
	"private",
	"group",
	"channel",
	"bot",
	"chat",
	"user",
	"ads",
	"forward",
	"new_chat_member",
	"left_chat_member"
)

class Filter:
	def __call__(self, message: Message):
		raise NotImplementedError 
	
	def __and__(self, other):
		return AndFilter(self, other)
	
	def __or__(self, other):
		return OrFilter(self, other)
	
	def __invert__(self):
		return NotFilter(self)
	
class AndFilter(Filter):
	def __init__(self, *filters: Filter):
		self.filters = filters 
	
	def __call__(self, message: Message) -> bool:
		return all(filter(message) for filter in self.filters)

class OrFilter(Filter):
	def __init__(self, *filters: Filter):
		self.filters = filters 
	
	def __call__(self, message: Message) -> bool:
		return any(filter(message) for filter in self.filters)

class NotFilter(Filter):
	def __init__(self, filter: Filter):
		self.filter = filter 
	
	def __call__(self, message: Message) -> bool:
		return not self.filter(message)

class CommandsFilter(Filter):
	def __init__(
		self,
		commands: Optional[Union[str,List[str]]] = None,
		prefix: Optional[str] = None
	) -> None:
		self.commands = commands
		self.prefix = prefix or "/"
		
		if not isinstance(self.commands, list) and not isinstance(self.commands, str):
			raise InvalidCommandsType()
		if not isinstance(self.prefix, str):
			raise InvalidCommandsPrefixType()
	
	def __call__(self, message: Message) -> bool:
		if not self.commands:
			return message.text.startswith(self.prefix)
		
		try:
			command = message.text.split(self.prefix)[1]
		except Exception: 
			return False 
		
		if isinstance(self.commands, str):
			return command == self.commands
			
		return bool(
			command in self.commands
		)

commands = CommandsFilter

class TextFilter(Filter):
	def __init__(self, texts: Optional[Union[str, List[str]]] = None):
		self.texts = texts 
		
	def __call__(self, message: Message) -> bool:
		if not self.texts:
			return False if message.text == "None" else True 
		
		if isinstance(self.texts, str):
			return bool(
				message.text  and 
				message.text == self.texts
			)
		if isinstance(self.texts, list):
			return bool(
				message.text  and 
				message.text in self.texts
			)
		return False
	
text = TextFilter

class PrivateFilter(Filter):
	def __call__(self, message: Message) -> bool:
		return message.chat.type == ChatTypes.User

private = PrivateFilter()

class GroupFilter(Filter):
	def __call__(self, message: Message) -> bool:
		return message.chat.type == ChatTypes.Group

group = GroupFilter()

class ChannelFilter(Filter):
	def __call__(self, message: Message) -> bool:
		return message.chat.type == ChatTypes.Channel

channel = ChannelFilter()

class BotFilter(Filter):
	def __call__(self, message: Message) -> bool:
		return message.chat.type == ChatTypes.Bot

bot = BotFilter()

class ChatFilter(Filter):
	def __init__(self, guids: Union[str, List[str]]):
		self.guids = guids 
	
	def  __call__(self, message: Message) -> bool:
		if isinstance(self.guids, str):
			return message.chat.object_guid == self.guids
		return message.chat.object_guid in self.guids

chat = ChatFilter

class UserFilter(Filter):
	def __init__(self, guids: Union[str, List[str]]):
		self.guids = guids 
	
	def __call__(self, message: Message) -> bool:
		if isinstance(self.guids, str):
			return message.chat.author_guid == self.guids 
		if isinstance(self.guids, list):
			return message.chat.author_guid in self.guids
		return False

user = UserFilter

class AdsFilter(Filter):
	def __call__(self, message: Message):
		url_pattern = r"(https?://[^\s]+)"
		username_patern = r"@\w+"
		
		return bool(
			search(url_pattern, message.text) or 
			search(username_patern, message.text)
		)

ads = AdsFilter()

class NewChatMemberFilter(Filter):
	def __call__(self, message: Message) -> bool:
		if not message.event:
			return False
		if message.event.type in [
			EventTypes.AddedGroupMembers,
			EventTypes.JoinedGroupByLink
		]:
			return True 
		return False

new_chat_member = NewChatMemberFilter()

class LeftChatMemberFilter(Filter):
	def __call__(self, message: Message) -> bool:
		if not message.event:
			return False 
		if message.event.type in [
			EventTypes.RemoveGroupMembers,
			EventTypes.LeaveGroup
		]:
			return True 
		return False

left_chat_member = LeftChatMemberFilter()

class ForwardFilter:
	def __call__(self, message: Message) -> bool:
		True if message.forward else False

forward = ForwardFilter()