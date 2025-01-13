from websocket import WebSocketApp
from .helper import Helper
from json import dumps, loads
from threading import Thread
from ..types import Message
from ..exceptions import NotRegistered, TooRequests
from ..utils import Utils
from re import match
from time import sleep

class Socket:
    def __init__(self, methods) -> None:
        self.methods = methods
        self.handlers = {}

    def connect(self) -> None:
        print("Connecting to the webSocket...")
        ws = WebSocketApp(
            Helper.getSocketServer(),
            on_open=self.onOpen,
            on_message=self.onMessage
        )
        ws.run_forever()

    def handShake(self, ws, data=None) -> None:
        ws.send(
            data or dumps(
                {
                    "auth": self.methods.sessionData["auth"],
                    "api_version": self.methods.apiVersion,
                    "method": "handShake"
                }
            )
        )

    def keepAlive(self, ws) -> None:
        while True:
            try:
                self.methods.getChatsUpdates()
                self.handShake(ws, "{}")
                sleep(30)
            except NotRegistered:
                raise
            except TooRequests:
                break
            except:
                continue

    def onOpen(self, ws) -> None:
        Thread(target=self.keepAlive, args=[ws]).start()
        self.handShake(ws)
        print("Connected.")
    
    def onMessage(self, _, message:str) -> None:
        if not message:
            return
        
        message:dict = loads(message)

        if not message.get("type") == "messenger":
            return
        
        message:dict = loads(self.methods.crypto.decrypt(message["data_enc"]))
        
        if not message.get("message_updates"):
            return
        
        message: Message = Message(
        	message,
        	self.methods
        )
        for handler in self.handlers:
        	filters = self.handlers[handler]
        	Thread(
        		target= self.handleMessages,
        		args=(handler, filters, message)
        	).start()
        
    def handleMessages(self, func: callable, filters, message: Message) -> None:
    	if not filters:
    		Thread(target= func, args= (message,)).start()
    		return 
    	if not filters(message):
    	    return 
    	Thread(target= func, args= (message,)).start()
    
    def addHandler(self, func, filters: list) -> None:
        self.handlers[func] = filters
        return func

    
