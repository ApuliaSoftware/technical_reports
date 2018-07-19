# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime

class Reports(models.Model):

    _name = 'report.reports'

    _rec_name = "display_name"

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    project_id = fields.Many2one("project.project", string="Project")
    project_activity_id = fields.Many2one("project.task", string="Project activity")
    users_ids = fields.Many2many("res.users", string="Formation users list")
    partecipants_customer_description = fields.Text()
    start_journey_date = fields.Datetime()
    end_journey_date = fields.Datetime()
    start_activity_date = fields.Datetime()
    end_activity_date = fields.Datetime()
    activity_description = fields.Html()
    order_type = fields.Selection([('prepaid','Prepaid'),('consumptive','Consumptive')], string="Order type")
    debit = fields.Boolean()
    customer_note = fields.Text()
    #notes_list_ids = fields.One2many('nuova classe')
    digital_sign = fields.Binary()
    display_name = fields.Char(compute = '_display_name')

    @api.multi
    def _display_name(self):

        for n in self:

            format_data = "%Y-%m-%d"
            date_without_time = (n.start_activity_date.datetime, format_data)
            sequence = [n.partner_id.name, n.project_id.name, date_without_time]
            n.display_name = " - ".join(sequence)