from enum import Enum

class EventTypes(Enum):
	AddedGroupMembers = "AddedGroupMembers"
	RemoveGroupMembers = "RemoveGroupMembers"
	PinnedMessageUpdated = "PinnedMessageUpdated"
	CreateGroupVoiceChat = "CreateGroupVoiceChat"
	StopGroupVoiceChat = "StopGroupVoiceChat"
	JoinedGroupByLink = "JoinedGroupByLink"
	LeaveGroup = "LeaveGroup"