from .BaseModel import *

class BookModel(BaseModel):
	def __init__(self):
		super().__init__()
		self.table_head = ["id_buku", "judul", "pengarang", "penerbit", "tahun","rak"]
		self.table_name = 'books'

	def updateByID(self, *data):
		query = f"UPDATE {self.table_name} SET {self.table_head[1]}='{data[1]}',{self.table_head[2]}='{data[2]}',{self.table_head[3]}='{data[3]}',{self.table_head[4]}='{data[4]}',{self.table_head[5]}='{data[5]}' WHERE id = {data[0]}"
		return self.database.execute(query)

	def searchByKeyword(self,keyword):
		query = f"SELECT * FROM {self.table_name} WHERE {self.table_head[1]} LIKE '%{keyword}%' OR {self.table_head[2]} LIKE '%{keyword}%' OR {self.table_head[3]} LIKE '%{keyword}%' OR {self.table_head[4]} LIKE '%{keyword}%' OR {self.table_head[5]} LIKE '%{keyword}%'"
		return self.database.fetchall(query)

	def getByID(self,idBuku):
		query = f"SELECT * FROM {self.table_name} WHERE id='{idBuku}'"
		return self.database.fetchall(query)

	def getCount(self):
		query = f'SELECT * FROM {self.table_name}'
		#query = f"SELECT COUNT(*) FROM {self.table_name}"
		a = self.database.fetchall(query)
		return len(a)
