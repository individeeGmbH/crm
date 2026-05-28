import frappe


def execute():
    frappe.db.sql("""
        UPDATE `tabCRM Lead` l
        JOIN (
            SELECT
                dl.link_name AS lead_name,
                COUNT(*) AS total_calls,
                MAX(cl.creation) AS last_call_date
            FROM `tabCRM Call Log` cl
            JOIN `tabDynamic Link` dl
                ON  dl.parent       = cl.name
                AND dl.parenttype   = 'CRM Call Log'
                AND dl.link_doctype = 'CRM Lead'
            GROUP BY dl.link_name
        ) stats ON stats.lead_name = l.name
        SET l.dial_count = stats.total_calls,
            l.last_dial_on = stats.last_call_date
    """)
    frappe.db.commit()
