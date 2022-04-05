from odoo import _, api, fields, models, tools


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _order = "id desc"

    name = fields.Char(string="Title", required=True)
    description = fields.Char(required=True)

    partner_id = fields.Many2one(comodel_name="res.partner", string="Contact")
    partner_name = fields.Char(string="Partner Name", related='partner_id.name')
    partner_email = fields.Char(string="Partner Email", related='partner_id.email')

    assigned_date = fields.Date()
    closed_date = fields.Datetime()

    is_assigned = fields.Boolean(string="Assigned")
    actions_to_be_made = fields.Html(string="Actions")
    
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )
    priority = fields.Selection(
        selection=[
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
            ("3", "Very High"),
        ],
        default="1",
    )
    active = fields.Boolean(default=True)

    # ---------------------------------------------------
    # CRUD
    # ---------------------------------------------------

    @api.model
    def create(self, vals):
        res = super().create(vals)
        return res

    def copy(self, default=None):
        res = super().copy(default)
        return res

    def write(self, vals):
        res = super().write(vals)
        return res



