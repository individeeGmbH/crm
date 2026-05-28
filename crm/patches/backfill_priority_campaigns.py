import frappe


def execute():
    frappe.db.sql("""
        UPDATE `tabCRM Lead`
        SET priority_campaign = CASE
            WHEN custom_campaign LIKE '%NGO%' THEN 1
            WHEN custom_source_type  = 'paid' THEN 1
            WHEN COALESCE(custom_visit_duration, 0) >= 30 THEN 1
            ELSE 0
        END
    """)
    frappe.db.commit()
