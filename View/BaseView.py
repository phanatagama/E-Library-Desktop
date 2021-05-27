from .Gui1 import *

class BaseView(MyFrame1):
	"""docstring for BookView"""
	def __init__(self):
		# BookController.__init__(self,parent)
		MyFrame1.__init__(self,parent=None)

		# BookViewTable
		for col,label in enumerate(['ID Buku','Judul Buku','Pengarang','Penerbit','Tahun Terbit','Rak','Ubah','Hapus']):
			self.bookTable.SetColLabelValue(col, label)
		self.update_Grid()

		# BorrowViewTabel
		for col,label in enumerate(['ID Peminjaman','Judul Buku','Nama Mahasiswa','Petugas','Tanggal Pinjam']):
			self.borrowTable.SetColLabelValue(col, label)

		# HistoryViewTabel
		for col,label in enumerate(['ID Peminjaman','Judul Buku','Nama Mahasiswa','Petugas','Tanggal Pinjam','Tanggal Kembali', 'Denda']):
			self.historyTable.SetColLabelValue(col, label)

	# BookView
	def bookTableRefresh(self,dataGrid):
		self.bookTable.ClearGrid()
		row = self.bookTable.GetNumberRows()
		if len(dataGrid)>row:
			self.bookTable.AppendRows(len(dataGrid)-row)
			self.update_Grid()
		for y in range(len(dataGrid)):
			for x in range(6):
				self.bookTable.SetCellValue(y,x,str(dataGrid[y][x]))
		self.bookTable.ForceRefresh()
	
	def bookGetCellValue(self,row,col):
		return self.bookTable.GetCellValue(row,col)

	def modalDelete(self,row):
		if wx.MessageDialog(None,f"Yakin Ingin Menghapus Buku berjudul {self.bookGetCellValue(row,1)}",'Konfirmasi',wx.YES_NO|wx.ICON_INFORMATION).ShowModal() == wx.ID_YES:
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

	# BorrowView			
	def borrowTableRefresh(self,dataGrid):
		self.borrowTable.ClearGrid()
		row = self.borrowTable.GetNumberRows()
		if len(dataGrid)>row:
			self.borrowTable.AppendRows(len(dataGrid)-row)
		for y in range(len(dataGrid)):
			for x in range(5):
				self.borrowTable.SetCellValue(y,x,str(dataGrid[y][x]))
		self.borrowTable.ForceRefresh()

	#HistoryView
	def historyTableRefresh(self,dataGrid):
		self.historyTable.ClearGrid()
		row = self.historyTable.GetNumberRows()
		if len(dataGrid)>row:
			self.historyTable.AppendRows(len(dataGrid)-row)
		for y in range(len(dataGrid)):
			for x in range(7):
				self.historyTable.SetCellValue(y,x,str(dataGrid[y][x]))
		self.historyTable.ForceRefresh()

	# General
	def modalFail(self,msg="Aksi Gagal Dilakukan"):
		return wx.MessageDialog(None,f"{msg}",'Failed',wx.OK|wx.ICON_INFORMATION).ShowModal()

	def modalSuccess(self,msg="Aksi Berhasil Dilakukan"):
		return wx.MessageDialog(None,f"{msg}",'Successfully',wx.OK|wx.ICON_INFORMATION).ShowModal()		

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