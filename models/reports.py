# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from datetime import datetime
from openerp.exceptions import UserError


class Reports(models.Model):

    _name = 'report.reports'

    _rec_name = "display_name"

    name = fields.Char(string='Number', required=True,
                       copy=False, readonly=True, default=lambda self: _('New'))
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    project_id = fields.Many2one("project.project", string="Project")
    project_activity_id = fields.Many2one("project.task",
                                          string="Project activity")
    users_ids = fields.Many2many("res.users", string="Formation users list")
    partecipants_customer_description = fields.Text()
    start_journey_date = fields.Datetime()
    end_journey_date = fields.Datetime()
    start_activity_date = fields.Datetime()
    end_activity_date = fields.Datetime()
    activity_description = fields.Html()
    order_type = fields.Selection([('prepaid', 'Prepaid'),
                                   ('consumptive', 'Consumptive')],
                                  string="Order type", required=True)
    to_invoice = fields.Boolean()
    customer_note = fields.Text()
    digital_sign = fields.Binary()
    display_name = fields.Char(compute='_display_name')
    notes_ids = fields.One2many("report.notes", "report_id", string="Notes")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to invoice', 'To invoice'),
        ('done', 'Done')],
        string="state", default="draft")
    invoice_id = fields.Many2one ("account.invoice", string="Invoice",
                                  readonly=True)
    intervention_place = fields.Many2one("res.partner", string="Partner")
    city = fields.Char(related="intervention_place.city", string="City",
                       store=True, readonly=True)

    @api.multi
    def _display_name(self):
        for n in self:
            sequence = [n.partner_id.name]
            if n.project_id.name:
                sequence.append(n.project_id.name)
            if n.start_activity_date:
                n.date_without_time = datetime.strptime(
                    n.start_activity_date, "%Y-%m-%d %H:%M:%S").date()
                n.convert_date = datetime.strftime(n.date_without_time,
                                                   "%Y-%m-%d")
                sequence.append(n.convert_date)

            n.display_name = " - ".join(sequence)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'technical.reports') or _('New')
        result = super(Reports, self).create(vals)
        return result

    @api.multi
    def action_done(self):
        for o in self:
            o.state = 'done'

    @api.multi
    def action_to_confirm(self):
        for o in self:
            if o.to_invoice == False and o.order_type == 'prepaid':
                o.state = 'done'
            else:
                o.state = 'to invoice'

    @api.multi
    def action_draft(self):
        for o in self:
            o.state = 'draft'

    @api.onchange("partner_id")
    def change_partner(self):
        self.project_id = False
        self.intervention_place = False
        self.project_activity_id = False


    @api.multi
    @api.constrains('start_journey_date', 'end_journey_date',
                  'start_activity_date', 'end_activity_date')
    def check_date(self):
        for report in self:
            if not (report.start_journey_date and report.start_activity_date):
                continue

            if (report.start_activity_date < report.start_journey_date):
                raise UserError(
                    _(
                        'Error'
                        '! '
                        'Activity starting date must be bigger than journey starting date.'
                    ))

            if not (report.start_activity_date and report.end_activity_date):
                continue

            if(report.start_activity_date > report.end_activity_date):
                raise UserError(
                    _(
                        'Error'
                        '! '
                        'Activity starting date must be lower than its ending date.'
                    ))

            if not (report.end_activity_date and report.end_journey_date):
                continue

            if (report.end_activity_date > report.end_journey_date):
                raise UserError(
                    _(
                        'Error'
                        '! '
                        'Activity ending date must be lower than journey ending date.'
                    ))

            if not (report.start_journey_date and report.end_journey_date):
                continue

            if(report.start_journey_date > report.end_journey_date):
                raise UserError(
                    _(
                        'Error'
                        '! '
                        'Journey starting date must be lower than its ending date.'
                    ))


