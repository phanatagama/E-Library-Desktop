# from View.BookView import *
from Controller.Controller import *

class App(wx.App):
	"""docstring for App"""
	def OnInit(self):
		self.frame = Controller()
		self.frame.main()
		return True
