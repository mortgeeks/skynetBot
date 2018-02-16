#!/usr/bin/python3
import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "#ctfteamv1" # Channel
channelPass = "welevelup"
skynet = "skynetBot" # bot nick
adminname = "thehappybit" # admin nickname.
exitcode = "bye " + skynet

def conn():
	ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
	ircsock.send(bytes("USER "+ skynet +" "+ skynet +" "+ skynet + " " + skynet + "\n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
	ircsock.send(bytes("NICK "+ skynet +"\n", "UTF-8")) # assign the nick to the bot

def joinchan(chan,chanPass): # join channel(s).
	ircsock.send(bytes("JOIN "+ chan +" "+ chanPass +"\n", "UTF-8")) 
	ircmsg = ""
	while ircmsg.find("End of /NAMES list.") == -1:  
		ircmsg = ircsock.recv(2048).decode("UTF-8")
		ircmsg = ircmsg.strip('\n\r')
		print(ircmsg)

def ping(): # respond to server Pings.
	ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

def sendmsg(msg): # sends messages to the channel.
	ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n") 

if __name__ == '__main__':
	conn()
	joinchan(channel,channelPass)
	while 1:
		ircmsg = "" #receive information 
		ircmsg = ircsock.recv(2048).decode("UTF-8")
		ircmsg = ircmsg.strip('\n\r')
		print(ircmsg) #print received msgs
		# repsond to pings so server doesn't think we've disconnected
		if ircmsg.find("PING :") != -1: 
			ping()
		if ircmsg.find("PRIVMSG") != -1:
		# save user name into name variable
			name = ircmsg.split('!',1)[0][1:]
			print('name: ' + name)
		# get the message to look for commands
			message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
			print(message)
