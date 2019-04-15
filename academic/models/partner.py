from odoo import api, fields, models, _

class Partner(models.Model):

    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string="Is Instructor", default=False )