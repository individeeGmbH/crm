import frappe


def execute():
    frappe.db.sql("""
        UPDATE `tabCRM Lead` l
        JOIN (
            SELECT
                dl.link_name AS lead_name,
                MAX(cl.creation) AS last_call_date
            FROM `tabCRM Call Log` cl
            JOIN `tabDynamic Link` dl
                ON  dl.parent       = cl.name
                AND dl.parenttype   = 'CRM Call Log'
                AND dl.link_doctype = 'CRM Lead'
            WHERE cl.status = 'Completed'
            GROUP BY dl.link_name
        ) stats ON stats.lead_name = l.name
        SET l.last_contact_on = stats.last_call_date,
            l.next_action_on = DATE_ADD(stats.last_call_date, INTERVAL 3 DAY)
        WHERE l.status IN ('Contacted', 'Reached')
          AND (l.last_contact_on IS NULL)
    """)
    frappe.db.commit()
