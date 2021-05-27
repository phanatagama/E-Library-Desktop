from Core.Database import *

class BaseModel:
	"""docstring for BaseModel"""
	def __init__(self):
		self.database = Database()

	def insert(self, data):
		query = f"""INSERT INTO {self.table_name} {str(tuple(self.table_head[1:])).replace("'","")} VALUES {data};"""
		return self.database.execute(query)
		
	def deleteByID(self, id_item):
		query = f"DELETE FROM {self.table_name} WHERE id={id_item}"
		return self.database.execute(query)

	def getData(self):
		query = f'SELECT * FROM {self.table_name}'
		return self.database.fetchall(query)