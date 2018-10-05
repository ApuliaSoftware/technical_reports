# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class AccountInvoice (models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def unlink(self):
        for invoice in self:
            report_id = invoice.env['technical.report'].search(
                [('invoice_id', '=', invoice.id)])
            result = super(AccountInvoice, self).unlink()
            if result:
                report_id.state = 'to invoice'
            return result
