# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Reports(models.Model):
    _name = 'report.reports'

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
    #firma
