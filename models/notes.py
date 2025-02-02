# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class TechnicalReportNotes(models.Model):

    _name = 'technical.report.notes'
    _rec_name = "display_name"

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    summary = fields.Char(size=50)
    date_and_hour = fields.Datetime(required=True, default=fields.Datetime.now)
    notes = fields.Html(required=True)
    worked = fields.Boolean()
    report_id = fields.Many2one("technical.report", string="Technical report")
    display_name = fields.Char(compute='_display_name')

    @api.multi
    def _display_name(self):
        for n in self:
            n.display_name = n.partner_id.name
