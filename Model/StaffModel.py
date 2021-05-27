
from .BaseModel import *

class StaffModel(BaseModel):
	def __init__(self):
		super().__init__()

	def validStaff(self,usr,passwd):
		query = f"SELECT * FROM staff WHERE email='{usr}' AND pass='{passwd}'"
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False