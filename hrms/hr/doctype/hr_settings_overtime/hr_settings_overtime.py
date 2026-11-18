from frappe.model.document import Document


class HRSettingsOvertime(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		branch: DF.Link
		max_auto_overtime: DF.Float
		min_auto_overtime: DF.Float
		overtime_deduction: DF.Float
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
