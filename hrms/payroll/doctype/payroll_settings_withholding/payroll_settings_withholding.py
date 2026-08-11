from frappe.model.document import Document


class PayrollSettingsWithholding(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		currency: DF.Link
		maximum_withholding_balance: DF.Currency
		minimum_amount: DF.Currency
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		round_salary: DF.Currency
	# end: auto-generated types

	pass
