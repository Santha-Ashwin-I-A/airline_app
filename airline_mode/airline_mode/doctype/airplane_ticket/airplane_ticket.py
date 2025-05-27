# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
	def before_insert(self):
		ran_no = random.randint(10,99)
		ran_let = random.choice(["A","B","C","D","E","F"])
		self.seat = f"{ran_no}{ran_let}"

	def validate(self):
		total=0
		for i in self.table_asdg:
			total+= i.amount
		self.total_amount = self.flight_price + total
	def before_save(self):
		a = frappe.db.get_list("Airplane",fields=["name","capacity"])
		b = frappe.db.get_list("Airplane Flight",fields=["name","airplane"],filters={"name":f"{self.flight}"})
		c=[]
		for i in b:
			for j in a:
				if i.airplane == j.name:
					c.append(j)
		for i in c:
			d= i.capacity
		if d >= len(b):
				pass
		else:
			frappe.throw("Maxium Tickets Applied for this Flight")
