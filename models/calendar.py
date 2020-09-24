# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    presenter_ids = fields.One2many('res.partner', 'calendar_id')
    note_tracker = fields.Many2one('res.partner')
    agenda_topics = fields.Text()
    action_items = fields.Text()
    conclusion = fields.Text()
