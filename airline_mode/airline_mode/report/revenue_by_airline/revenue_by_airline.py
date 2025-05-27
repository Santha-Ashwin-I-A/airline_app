# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	airlines = frappe.get_all("Airline", fields=["name"])
	data = frappe.db.get_list("Airplane Ticket",fields=["flight.airplane","total_amount"])
	columns = [
		{"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline"},
		{"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency","fieldvalue":"Data"}
	]
	
	
	return columns,data,None,None,None

