from .BorrowView import *
# from . import BookController
# from Controller.BookController import BookController

class Modal(BookModal):
	def __init__(self,parent=None,title=wx.EmptyString, judul=wx.EmptyString,pengarang=wx.EmptyString,penerbit=wx.EmptyString,tahunTerbit=wx.EmptyString,rakBuku=wx.EmptyString):
		BookModal.__init__(self,parent=None,title=title,judul=judul,pengarang=pengarang,penerbit=penerbit,tahunTerbit=tahunTerbit,rakBuku=rakBuku)

	def setTitle(self,title):
		wx.Dialog.title = title
	# def btnSimpanBuku(self,event):
	# 	judul = self.m_textCtrl10.GetValue()
	# 	pengarang = self.m_textCtrl11.GetValue()
	# 	penerbit =self.m_textCtrl12.GetValue()
	# 	tahunterbit = self.m_textCtrl13.GetValue()
	# 	rakbuku = self.m_textCtrl131.GetValue()
		# print(self.anj)
		# self.controller.btnSimpanBuku(judul,pengarang,penerbit,tahunterbit,rakbuku)

# from Controller.BookController import *
class BookView(BorrowView):
	"""docstring for BookView"""
	def __init__(self):
		# BookController.__init__(self,parent)
		BorrowView.__init__(self)
		# self.controller = BookController()
		for col,label in enumerate(['ID Buku','Judul Buku','Pengarang','Penerbit','Tahun Terbit','Rak','Ubah','Hapus']):
			self.bookTable.SetColLabelValue(col, label)
		self.update_Grid()
		self.modal = BookModal(self)
		# self.refresh()

	def refresh(self,dataGrid):
		# print(self.bookTable.SelectAll())
		self.bookTable.ClearGrid()
		row = self.bookTable.GetNumberRows()
		if len(dataGrid)>row:
			self.bookTable.AppendRows(len(dataGrid)-row)
			self.update_Grid()
		for y in range(len(dataGrid)):
			for x in range(6):
				self.bookTable.SetCellValue(y,x,str(dataGrid[y][x]))
		self.bookTable.ForceRefresh()
		
	def refreshB(self,dataGrid):
		# print(self.borrowTable.SelectAll())
		self.borrowTable.ClearGrid()
		row = self.borrowTable.GetNumberRows()
		if len(dataGrid)>row:
			self.borrowTable.AppendRows(len(dataGrid)-row)
			self.update_Grid()
		for y in range(len(dataGrid)):
			for x in range(5):
				self.borrowTable.SetCellValue(y,x,str(dataGrid[y][x]))
		self.borrowTable.ForceRefresh()
	# def modalUpdate(self,title,data):
	# 	BookModal(self,title,data[1],data[2],data[3],data[4],data[5]).ShowModal()

	# def modalAdd(self,title):
	# 	BookModal(self,title=title).ShowModal()

	def modalDelete(self,row):
		if wx.MessageDialog(None,f"Yakin Ingin Menghapus Buku berjudul {self.bookTable.GetCellValue(row,1)}",'Konfirmasi',wx.YES_NO|wx.ICON_INFORMATION).ShowModal() == wx.ID_YES:
			return True

	def update_Grid(self):
		img = wx.Bitmap("../SET.png", wx.BITMAP_TYPE_PNG)
		self.rd = MyImageRenderer(img)
        # Buttons coordinates
		numRows = self.bookTable.GetNumberRows()
		for y in range(numRows):
			self.rd.rend_row = y
			self.rd.rend_col = 6
			self.bookTable.SetCellRenderer(self.rd.rend_row, self.rd.rend_col, self.rd)
			self.bookTable.SetCellRenderer(self.rd.rend_row, self.rd.rend_col+1, self.rd)
			self.bookTable.SetColSize(self.rd.rend_col, img.GetWidth())
			self.bookTable.SetColSize(self.rd.rend_col+1, img.GetWidth())
			self.bookTable.SetRowSize(self.rd.rend_row, img.GetHeight())
			self.bookTable.SetReadOnly(self.rd.rend_row, self.rd.rend_col, True)
			self.bookTable.SetReadOnly(self.rd.rend_row, self.rd.rend_col+1, True)

class MyImageRenderer(wx.grid.GridCellRenderer):
    def __init__(self, img):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = img

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rect.width - 2:
            width = rect.width - 2
        if height > rect.height - 2:
            height = rect.height - 2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)