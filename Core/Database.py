import mysql.connector,os
from datetime import datetime

class Database:
	__host = 'localhost'
	__user = 'root'
	__passwd = ''
	__database = 'perpustakaan'
	def __init__(self):
		self.db = mysql.connector.connect(
			host = Database.__host,
			user = Database.__user,
			passwd = Database.__passwd,
			database = Database.__database
			)
		self.cursor = self.db.cursor()

	def executerule(func):
		def inner(self, query):
			if ('INSERT' in query) or ('DELETE' in query) or ('UPDATE' in query):
				func(self, query)
				return self.commit()
			else:
				return func(self, query)
		return inner

	@executerule
	def execute(self, query):
		return self.cursor.execute(query)

	def commit(self):
		self.db.commit() 
		return self.cursor.rowcount

	def fetchall(self, query):
		self.execute(query)
		return self.cursor.fetchall()

	def fetchrule(func):
		def inner(self, table_head ,query):
			if table_head==None:
				self.execute(query)
				return self.cursor.fetchone()
			else:
				return self.fetchone(table_head, query)
		return inner

	@fetchrule
	def fetchone(self, table_head, query):
		self.execute(query)
		return Database.table(table_head, self.cursor.fetchone())
		