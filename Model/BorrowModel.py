from .BaseModel import *

class BorrowModel(BaseModel):
	"""docstring for BorrowModel"""
	def __init__(self):
		super().__init__()
		self.table_head = ["id_peminjam", "id_buku", "id_students", "id_staff","tanggal_pinjam"]
		self.table_name = 'borrow'

	def borrowGetData(self):
		borrowData = self.getData()
		borrowTableData = []
		for row in borrowData:
			query = f'SELECT borrow.id,books.judul,students.nama,staff.nama,borrow.tanggal_pinjam FROM books JOIN students ON books.id ={row[1]} JOIN staff ON staff.id={row[3]} JOIN borrow ON borrow.id={row[0]} AND students.id ={row[2]};'
			borrowTableData += self.database.fetchall(query)
		return borrowTableData

	def createNote(self,*data):
		query = f"SELECT students.nama,books.judul,staff.nama,borrow.tanggal_pinjam FROM books JOIN students ON books.id ='{data[0]}' JOIN staff ON staff.id='{data[2]}' JOIN borrow ON borrow.tanggal_pinjam='{data[3][:10]}' AND students.id ='{data[1]}';"
		return self.database.fetchall(query)[0]
		
	def validStudent(self, id_students):
		query = f'SELECT * FROM students WHERE id={id_students}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False

	def notInBorrow(self, id_students):
		query = f'SELECT * FROM borrow WHERE id_students={id_students}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False

	def validBook(self, id_book):
		query = f'SELECT * FROM books WHERE id={id_book}'
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False
