from enum import Enum

class MessageTypes(Enum):
	ContactMessage = "ContactMessage"
	Text = "Text"
	Sticker = "Sticker"
	FileInline = "FileInline"
	Live = "Live"
	Location = "Location"