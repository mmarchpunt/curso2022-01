# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk Ticket MMarch",
    "summary": """Helpdesk Ticket""",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "Miquel March, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/mmarchpunt/curso2022-01/",
    "depends": [
        "mail", 
        "portal"
        ],
    "data": [
        "security/ir.model.access.csv",
        "data/helpdesk_ticket_data.xml",
        "views/menus.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "development_status": "Beta",
    "application": False,
    "installable": True,
}
