import UDPkit

class Packet(object):

	def __init__(self, opCode, Filename, BlockNumber, Data, ErrorCode, ErrMsg = "ERROR", Mode = "octet"):
		self.opCode = opCode
		self.Filename = Filename
		self.BlockNumber = BlockNumber
		self.Data = Data
		self.ErrorCode = ErrorCode
		self.ErrMsg = ErrMsg
		self.Mode = Mode

		if (self.opCode == 0x0001):
			self.gopCode = "0000000000000001"
		if (self.opCode == 0x0002):
			self.gopCode = "0000000000000010"
		if (self.opCode == 0x0003):
			self.gopCode = "0000000000000011"
		if (self.opCode == 0x0004):
			self.gopCode = "0000000000000100"
		if (self.opCode == 0x0005):
			self.gopCode = "0000000000000101"
		


		if(self.opCode == 0x0001 or self.opCode == 0x0002):
			self.tftpHeader = self.gopCode + self.Filename + '0' + self.Mode + '0'
			print self.tftpHeader
		if(self.opCode == 0x0003):
			self.tftpHeader = self.gopCode + self.BlockNumber + self.Data
		if(self.opCode == 0x0004):
			self.tftpHeader = self.gopCode + self.BlockNumber
		if(self.opCode == 0x0005):
			self.tftpHeader = self.gopCode + self.ErrorCode + self.ErrMSG + '0'
	
	
