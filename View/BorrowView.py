from .BaseView import *

class BorrowView(BaseView):
	"""docstring for BookView"""
	def __init__(self):
		# BookController.__init__(self,parent)
		BaseView.__init__(self)
		# self.controller = BookController()
		for col,label in enumerate(['ID Peminjaman','Judul Buku','Nama Mahasiswa','Petugas','Tanggal Pinjam']):
			self.borrowTable.SetColLabelValue(col, label)
		# self.update_Grid()
		# self.modal = BookModal(self)

	def refresh(self,dataGrid):
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