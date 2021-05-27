# from .BaseController import *
from View.BaseView import *
from Model.BookModel import *
# from View.BorrowView import *
from Model.BorrowModel import *
from Model.HistoryModel import *
from Model.StaffModel import *
from datetime import datetime

class Controller():
	def __init__(self):
		self.LoginView = Login(parent=None)
		self.LoginView.btnLogin.Bind( wx.EVT_BUTTON, self.onBtnLogin )

		# super(MyFrame1,self).__init__(parent)
		self.BaseView = BaseView()
		self.BaseView.bookTable.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.bookSortData )
		self.BaseView.bookTable.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.bookTableAction )
		self.BaseView.btnTambahBuku.Bind( wx.EVT_BUTTON, self.onBtnTambahBuku )
		# self.BaseView.m_button39211.Bind( wx.EVT_BUTTON, self.addDataPeminjaman )
		self.BaseView.searchBox.Bind( wx.EVT_TEXT, self.onSearchBox )	
		self.BaseView.btnTambahPeminjaman.Bind( wx.EVT_BUTTON, self.onBtnTambahPeminjaman )	
		self.BaseView.btnSubmit.Bind( wx.EVT_BUTTON, self.onBtnSubmit )
		self.BaseView.searchBoxHistory.Bind( wx.EVT_TEXT, self.onSearchBoxHistory )
		self.BaseView.comboBox.Bind( wx.EVT_COMBOBOX, self.onComboBox )
		self.BookModel = BookModel()
		self.BorrowModel = BorrowModel()
		self.HistoryModel = HistoryModel()
		self.StaffModel = StaffModel()
		self.bookData = self.bookGetData()
		self.borrowData = self.borrowGetData()
		self.historyData = self.historyGetData()

	# Login
	def onBtnLogin(self,event):
		usr = self.LoginView.inputUsername.GetValue()
		passwd = self.LoginView.inputPassword.GetValue()
		self.id_staff = self.StaffModel.validStaff(usr,passwd)
		if self.id_staff:
			self.LoginView.Destroy()
			return self.menu()
		else:
			self.BaseView.modalFail("Email/Password Salah!!!")



	# Book Function
	def onComboBox(self,event):
		if event.GetString() != "":
			data = self.BookModel.searchByKeyword(event.GetString())
			return self.BaseView.bookTableRefresh(data)
		return self.BaseView.bookTableRefresh(self.bookGetData())

	def bookGetData(self):
		return self.BookModel.getData()

	def onSearchBox(self,event):
		keyword = self.BaseView.searchBox.GetValue()
		if keyword != '':
			data = self.BookModel.searchByKeyword(keyword)
			return self.BaseView.bookTableRefresh(data)
		return self.BaseView.bookTableRefresh(self.bookGetData())

	def bookSortData(self,event):
		label = event.GetCol()
		self.data = sorted(self.bookData,key=lambda x: x[label])
		self.BaseView.bookTableRefresh(self.data)

	def bookTableAction( self, event ):
		row = event.GetRow()
		col = event.GetCol()
		if col==6:
			data = self.BookModel.getByID(self.BaseView.bookGetCellValue(row,0))[0]
			data = list(map(str, data))
			self.modalCall('Ubah Buku',data)
		elif col==7:
			if self.BaseView.modalDelete(row):
				self.BookModel.deleteByID(self.BaseView.bookGetCellValue(row,0))
				self.BaseView.bookTableRefresh(self.bookGetData())
			# print(row,col)

	def modalCall(self,title,data=wx.EmptyString):
		if "Tambah" in title:
			self.dialog = BookModal(None,title)
		else:
			self.dialog = BookModal(None,title,data[0],data[1],data[2],data[3],data[4],data[5])
		self.dialog.m_button6.Bind( wx.EVT_BUTTON, self.btnSimpanBuku )
		self.dialog.ShowModal()

	def onBtnTambahBuku( self, event ):
		self.modalCall('Tambah Buku')

	# def addDataPeminjaman( self, event ):
	# 	event.Skip()

	def btnSimpanBuku(self,event):
		judul = self.dialog.inputJudul.GetValue()
		pengarang = self.dialog.inputPengarang.GetValue()
		penerbit = self.dialog.inputPenerbit.GetValue()
		tahunterbit = self.dialog.inputTahunTerbit.GetValue()
		rakbuku = self.dialog.inputRak.GetValue()
		if not self.dialog.idData:
			self.BookModel.insert((judul,pengarang,penerbit,tahunterbit,rakbuku))
		else:
			self.BookModel.updateByID(self.dialog.idData,judul,pengarang,penerbit,tahunterbit,rakbuku)
		self.dialog.Destroy()
		self.BaseView.bookTableRefresh(self.bookGetData())
	
	# Borrow Function
	def borrowGetData(self):
		return self.BorrowModel.borrowGetData()	

	def onBtnTambahPeminjaman(self,event):
		id_book = self.BaseView.inputIdBuku.GetValue()
		id_mhs = self.BaseView.inputIdMahasiswa.GetValue()
		id_staff = self.id_staff
		current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		notInBorrow = self.BorrowModel.notInBorrow(id_mhs)
		validStudent = self.BorrowModel.validStudent(id_mhs)
		validBook = self.BorrowModel.validBook(id_book)
		if notInBorrow or not validStudent or not validBook:
			self.BaseView.modalFail("ID Buku/ID Mahasiswa Salah!!!")
		else:
			result = self.BorrowModel.insert((id_book,id_mhs,id_staff,current_date))
			if result:
				name,judul,petugas,tanggal = self.BorrowModel.createNote(id_book,id_mhs,id_staff,current_date)
				self.Nota = Nota(None,name,judul,petugas,current_date[:10])
				self.Nota.btnSelesai.Bind( wx.EVT_BUTTON, self.onBtnSelesai )
				self.Nota.ShowModal()
			else:
				self.BaseView.modalFail()
		self.BaseView.borrowTableRefresh(self.borrowGetData())

	def onBtnSelesai(self,event):
		self.Nota.Destroy()

	# History Function
	def historyGetData(self):
		return self.HistoryModel.historyGetData()	

	def onSearchBoxHistory(self,event):
		keyword = self.BaseView.searchBoxHistory.GetValue()
		if keyword != '':
			data = self.HistoryModel.searchByKeyword(keyword)
			return self.BaseView.historyTableRefresh(data)
		return self.BaseView.historyTableRefresh(self.historyGetData())

	def onBtnSubmit(self,event):
		id_borrow = self.BaseView.inputIdMahasiswa2.GetValue()
		if self.HistoryModel.validBorrow(self.borrowGetData(),id_borrow):
			tanggal_kembali,denda = self.HistoryModel.calculate(self.borrowGetData(),id_borrow)
			self.HistoryModel.insert((id_borrow,tanggal_kembali,denda))
			self.BorrowModel.deleteByID(id_borrow)
			self.BaseView.borrowTableRefresh(self.borrowGetData())
			self.BaseView.modalSuccess()
		else:
			self.BaseView.modalFail("ID Peminjaman Tidak Ditemukan")
		self.BaseView.historyTableRefresh(self.historyGetData())


# =================================================================

	def main(self):
		self.LoginView.Show()

	def menu(self):	
		self.BaseView.Show()
		self.BaseView.historyTableRefresh(self.historyGetData())
		self.BaseView.borrowTableRefresh(self.borrowGetData())
		self.BaseView.bookTableRefresh(self.bookGetData())