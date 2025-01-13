from typing import Optional
from .event_types import EventTypes
from .performer import Performer
from .peer import Peer

class Event:
	def __init__(self, event_data: dict) -> None:
		self.__event_data = event_data 
	
	@property
	def type(self) -> EventTypes:
		types = {
			"AddedGroupMembers": EventTypes.AddedGroupMembers,
			"RemoveGroupMembers": EventTypes.RemoveGroupMembers,
			"PinnedMessageUpdated": EventTypes.PinnedMessageUpdated,
			"CreateGroupVoiceChat": EventTypes.CreateGroupVoiceChat,
			"StopGroupVoiceChat": EventTypes.StopGroupVoiceChat,
			"JoinedGroupByLink": EventTypes.JoinedGroupByLink,
			"LeaveGroup": EventTypes.LeaveGroup
		}
		type = self.__event_data["type"]
		return types.get(type, type)
	
	@property
	def performer(self) -> Optional[Performer]:
		if self.type == EventTypes.StopGroupVoiceChat:
			return 
		return Performer(self.__event_data["performer_object"])
	
	@property
	def peer(self) -> Optional[Peer]:
		if not self.__event_data.get("peer_objects"):
			return 
		return Peer(self.__event_data["peer_objects"])
	
	@property
	def pinned_message_id(self) -> Optional[str]:
		if not self.type == EventTypes.PinnedMessageUpdated:
			return 
		return self.__event_data["pinned_message_id"]
	
	@property
	def group_voice_chat_duration(self) -> Optional[int]:
		if not self.type == EventTypes.StopGroupVoiceChat:
			return 
		return self.__event_data["group_voice_chat_duration"]
	
	def __dict__(self) -> dict:
		return self.__event_data