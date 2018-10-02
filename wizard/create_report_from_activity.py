# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ReportFromActivity(models.TransientModel):

    _name = 'report.from.activity'

    @api.multi
    def create_report(self):
        if self.env.context.get('active_id', False):
            active_id = self.env.context['active_id']
            activity = self.env['project.task'].browse(active_id)
            activity.ensure_one()
            tec_rep_obj = self.env['technical.report']
            partner_id = activity.partner_id
            if not activity.partner_id:
                if activity.project_id:
                    partner_id = activity.project_id.partner_id
            vals = {
                'partner_id': partner_id.id or False,
                'project_id': activity.project_id.id or False,
                'project_activity_id': activity.id,
                'order_type': 'prepaid',
                'intervention_place': partner_id.id
            }
            tec_rep = tec_rep_obj.create(vals)
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'technical.report',
                'res_id': tec_rep.id,
                'view_id': self.env.ref(
                    'technical_reports.view_reports_form').id,
                'target': 'current'
            }
