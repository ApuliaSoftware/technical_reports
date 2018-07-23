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
    digital_sign = fields.Binary()
    display_name = fields.Char(compute = '_display_name')
    notes_ids = fields.One2many("report.notes", "report_id", string="Notes")


    @api.multi
    def _display_name(self):

        for n in self:

            n.date_without_time = datetime.strptime(n.start_activity_date, "%Y-%m-%d %H:%M:%S").date()
            n.convert_date=datetime.strftime(n.date_without_time, "%Y-%m-%d")

            if n.project_id.name != False and n.convert_date != False:
                sequence = [n.partner_id.name, n.project_id.name, n.convert_date]
                n.display_name = " - ".join(sequence)

            elif n.project_id.name != False and n.convert_date == False:
                sequence = [n.partner_id.name, n.project_id.name]
                n.display_name = " - ".join(sequence)

            elif n.project_id.name == False and n.convert_date != False:
                sequence = [n.partner_id.name, n.convert_date]
                n.display_name = " - ".join(sequence)

            else:
                n.display_name = n.partner_id.name

