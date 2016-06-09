# NAME pcarsListener.py
# DESC helper to read packets from udp stream and pass data to web app
# AUTH tom snelling
# YEAR 2016

from pcars.enums import GameState, SessionState, RaceState, TyreFlags, FlagColour, Sector, PitMode, PitSchedule
from pcars.packet import Packet, TelemetryPacket
from StringIO import StringIO
import socket, threading

addr = ''
port = 5606

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpSocket.bind((addr, port))

udp_isopen = True
currentPacket = None

def getChannel(channel):
	if currentPacket != None:
		return currentPacket.getValue(channel)

def getTyre(number, channel):
	if currentPacket != None:
		return currentPacket.tyres[number][channel]

def getParticipant(channel):
	if currentPacket != None:
		p = currentPacket.participants[0]
		return p[channel]


def terminate():
	udp_isopen = False
	udpSocket.close()

def mainloop():
	global currentPacket, udp_isopen
	while udp_isopen:
		data = udpSocket.recv(1400)
		try:
			currentPacket = Packet.readFrom(StringIO(data))
		except:
			pass

thread = threading.Thread(target=mainloop)
thread.start()