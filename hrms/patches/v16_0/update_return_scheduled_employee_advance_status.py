import frappe


def execute():
	advances = frappe.get_all("Employee Advance", pluck="name", filters={"status": "Paid"})
	for advance in advances:
		frappe.get_doc("Employee Advance", advance).set_status(True)
