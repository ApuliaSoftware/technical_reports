# -*- coding: utf-8 -*-
# © 2018 Andrea Cometa (<http://www.andreacometa.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api

class AccountInvoice (models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def unlink(self):
        report_id = self.env['technical.report'].search(
            [('invoice_id', '=', self.id)])
        result = super(AccountInvoice, self).unlink()
        if result:
            report_id.state = 'to invoice'
        return result
