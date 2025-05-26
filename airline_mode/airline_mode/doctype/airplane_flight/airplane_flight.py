# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.naming import make_autoname
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from datetime import datetime


class AirplaneFlight(Document):
	def autoname(self):
		created_at = datetime.today().strftime("%m-%y")
		self.name = make_autoname(f"{self.airplane}-{created_at}-")

	def before_save(self):
		if not self.route:
			self.route = f"flights/{self.name}"
	def on_submit(self):
		self.status ="Completed"
