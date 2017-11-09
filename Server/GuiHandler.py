#importerar tkinter library smamt message Box.

#Definiton for GUI handler class, which allows the creation of the actual interface fo the chat server.
#It also calls the main.py server function.
class GuiHandler:
    def __init__(self,socketHandler_):
        self.socketHandler = socketHandler_

    #creates a interface with label and an entry field.

    def getPort(self):
        port = input("Port: ")

    #returns the inputed port number as blank from the start.
        self.portToReturn = port

        # creates a verification point with a button functionality.
        # it also calls the main.py server function.

        #closes the main port input window by calling destroy() function.

        #returns port to compare with client/user port input.
        return self.portToReturn

#main server GUI root Interface is created with tkinter settings.
    def startMainGui(self):
        from Users import CollectionOfUsers
        loop = True
        while loop:
            command = input("")
            if command[0] == "#":
                text = command[1:]
                self.sendMsgBySocketHandler(text)
            elif command[0] == "/":
                if command[1] == "c":
                    loop = False
                elif command[1] == "k":
                    username = command.split(" ")
                    self.socketHandler.kickKnownClient(str(username[1]))




    #call sockethandler instrutor function above and send admi messages to each connected client/chat member.
    def sendMsgBySocketHandler(self,text):
        self.socketHandler.sendAndShowMsg("Admin: " + text)

    #Calls sockethandler instrutor, closes the server.
    def closeConnection(self):
        self.socketHandler.closeEveryThing()

    #Starts main server GUI interface.
    def startGui(self):
        self.startMainGui()

    #displays messages from sever.
    def showMessage(self,text):
        #gör chattrutan writeable
        print(text+"\n")

    #shows warning messages upton incorrect port binding.
        #gör den read-only
        #rensar entryOfUser
    def showWarningMsg(self):
        print("could not bind port")
