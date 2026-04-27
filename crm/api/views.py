import frappe
from pypika import Criterion


@frappe.whitelist()
def get_views(doctype: str):
	View = frappe.qb.DocType("CRM View Settings")
	query = (
		frappe.qb.from_(View)
		.select("*")
		.where(Criterion.any([View.user == "", View.user == frappe.session.user]))
		.orderby(View.position)
		.orderby(View.label)
	)
	if doctype:
		query = query.where(View.dt == doctype)
	views = query.run(as_dict=True)
	return views
