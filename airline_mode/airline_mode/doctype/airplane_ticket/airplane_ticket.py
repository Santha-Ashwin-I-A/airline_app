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
		# if self.status != "Boarded":
		# 	frappe.throw("You only submit the Airplane Ticket if the status is Boarded")
