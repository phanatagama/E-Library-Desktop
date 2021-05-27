from .BaseModel import *
from datetime import datetime

class HistoryModel(BaseModel):
	"""docstring for ReturnBookModel"""
	def __init__(self):
		super().__init__()
		self.table_head = ["id_kembali", "id_borrow", "tanggal_kembali", "denda"]
		self.table_name = 'pengembalian'

	def calculate(self,data,id_borrow):
		for row in data:
			if str(row[0]) == id_borrow:
				tanggal_pinjam = row[-1]
				break
		denda = 0
		keterlambatan = self.today() - tanggal_pinjam
		if keterlambatan.days > 3:
			denda = 2000*(keterlambatan.days-3)
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S"), denda

	def historyGetData(self):
		query = f'SELECT pengembalian.id_borrow,books.judul,students.nama,staff.nama,riwayatpeminjaman.tanggal_pinjam,pengembalian.tanggal_kembali,pengembalian.denda FROM pengembalian JOIN riwayatpeminjaman ON pengembalian.id_borrow=riwayatpeminjaman.id_borrow JOIN books ON books.id=riwayatpeminjaman.id_buku JOIN students ON students.id=riwayatpeminjaman.id_students JOIN staff ON staff.id=riwayatpeminjaman.id_staff;'
		return self.database.fetchall(query)
		# historyTableData = []
		# for row in historyData:
		# 	query = f'SELECT pengembalian.id_borrow,returnbook.tanggal_kembali,returnbook.denda,staff.nama,borrow.tanggal_pinjam FROM returnbook JOIN students ON returnbook.id ={row[1]} JOIN staff ON staff.id={row[3]} JOIN borrow ON borrow.id={row[0]} AND students.id ={row[2]};'
		# 	historyTableData += self.database.fetchall(query)
		# return historyTableData

	def searchByKeyword(self,keyword):
		historyData = self.historyGetData()
		historyTableData = []
		for row in historyData:
			for value in row:
				if str(keyword).lower() in str(value).lower():
					historyTableData += [row]
					break
		return historyTableData

	def today(self):
		return datetime.now().date()

	def validBorrow(self, data, id_borrow):
		for row in data:
			if str(id_borrow) in str(row[0]):
				return True
		return False

		# query = f'SELECT * FROM borrow WHERE id={id_borrow}'
		# try:
		# 	return self.database.fetchall(query)[0][0]
		# except Exception as e:
		# 	return False