from typing import Optional, Union, BinaryIO
from .message_types import MessageTypes
from .forward_from import ForwardFrom
from .file_inline import FileInline
from .file_types import FileTypes
from .location import Location
from .reply_to import ReplyTo
from .contact import Contact
from .event import Event
from .chat import Chat
from .live import Live

class Message:
	def __init__(self, data: dict, methods) -> None:
		self.__data = data
		self.__message_updates = data["message_updates"][0]
		self.__chat_updates = data["chat_updates"][0]
		self.__methods = methods 
	
	@property 
	def id(self) -> str:
		return self.__message_updates["message"].get("message_id")
	
	@property 
	def message_id(self) -> str:
		return self.__message_updates["message"].get("message_id")
	
	@property
	def text(self) -> Optional[str]:
		return self.__message_updates["message"].get("text")
	
	@property
	def time(self) -> str:
		return self.__message_updates["message"].get("time")
	
	@property
	def type(self) -> MessageTypes:
		types = {
        	"Text": MessageTypes.Text,
            "Sticker": MessageTypes.Sticker,
            "FileInline": MessageTypes.FileInline,
            "Location": MessageTypes.Location,
            "ContactMessage": MessageTypes.ContactMessage,
            "Live": MessageTypes.Live
        }
		return types.get(
			self.__message_updates["message"]["type"], type 
		)
	
	@property 
	def is_edited(self) -> bool:
		return self.__message_updates["message"].get("is_edited")
	
	@property
	def is_mine(self) -> bool:
		return self.__chat_updates["chat"].get("last_message").get("is_mine")
	
	@property
	def prev_message_id(self) -> str:
		return self.__message_updates.get("prev_message_id")
	
	@property
	def state(self) -> str:
		return self.__message_updates.get("state")
	
	@property
	def chat(self) -> Chat:
		return Chat(self.__chat_updates)
	
	@property
	def reply_to_message_id(self) -> Optional[str]:
		return self.__message_updates["message"].get("reply_to_message_id")
	
	@property
	def reply_to(self) -> Optional[ReplyTo]:
		if not self.reply_to_message_id:
			return 
		reply_info = self.__methods.getMessagesById(self.chat.object_guid, [self.reply_to_message_id])["messages"][0]
		reply_data = {
			"message_id": self.reply_to_message_id,
			"text": reply_info["text"],
			"author_guid": reply_info["author_object_guid"]
		}
		return ReplyTo(reply_data)
	
	@property
	def is_forwarded(self) -> bool:
		return "forwarded_from" in self.__message_updates["message"].keys()
	
	@property 
	def forward_from(self) -> Optional[ForwardFrom]:
		if not self.is_forwarded:
			return 
		forward_info = self.__message_updates["message"]["forwarded_from"]
		return ForwardFrom(forward_info)
	
	@property
	def is_event(self) -> bool:
		return "event_data" in self.__message_updates["message"].keys()
	
	@property
	def event(self) -> Event:
		if not self.is_event:
			return 
		return Event(self.__message_updates["message"]["event_data"])
	
	@property
	def file_inline(self) -> Optional[FileInline]:
		if not self.__message_updates["message"].get("file_inline"):
			return 
		return FileInline(self.__message_updates["message"]["file_inline"])
	
	@property
	def contact(self) -> Optional[Contact]:
		if not self.__message_updates["message"].get("contact_message"):
			return 
		return Contact(self.__message_updates["message"]["contact_message"])
	
	@property
	def location(self) -> Optional[Location]:
		if not self.__message_updates["message"].get("location"):
			return 
		return Location(self.__message_updates["message"]["location"])
		
	@property
	def live(self) -> Optional[Live]:
		if not self.__message_updates["message"].get("live_data"):
			return 
		return Live(self.__message_updates["message"]["live_data"])
	
	def reply_text(self, text: str, quote: bool = False):
		if not quote:
			quote = None 
		else:
			quote = self.message_id
		return self.__methods.sendText(objectGuid= self.chat.object_guid, text= text, messageId= self.message_id)
	
	def seen(self):
		return self.__methods.seenChats(seenList= {self.chat.object_guid: self.message_id})
	
	def react(self, reaction_id: int):
		return self.__methods.actionOnMessageReaction(objectGuid= self.chat.object_guid, messageId= self.message_id, reactionId= reaction_id, action="Add")
	
	def unreact(self, reaction_id: int):
		return self.__methods.actionOnMessageReaction(objectGuid= self.chat.object_guid, reactionId= reaction_id, messageId= self.message_id, action="Remove")
	
	def delete(self, delete_for_all: bool = True):
	    return self.__methods.deleteMessages(objectGuid= self.chat.object_guid, messageIds= [self.message_id], deleteForAll= delete_for_all)
	
	def pin(self):
	    return self.__methods.setPinMessage(objectGuid= self.chat.object_guid, messageId= self.message_id, action= "Pin")
	
	def unpin(self):
	    return self.__methods.setPinMessage(objectGuid= self.chat.object_guid, messageId= self.message_id, action="Unpin")
		
	def forward(self, to_object_guid: str):
		return self.__methods.forwardMessages(objectGuid= self.chat.object_guid, messageIds= [self.message_id], toObjectGuid= to_object_guid)
	
	def download(self, save: bool= False, save_as: Optional[str] = None) -> dict:
		return self.__methods.download(objectGuid= self.chat.object_guid, messageId= self.message_id, save= save, saveAs= save_as, fileInline= self.file_inline.__dict__())
	
	def __dict__(self) -> dict:
		return self.__data