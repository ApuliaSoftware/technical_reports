# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api
from datetime import datetime

class TechnicalReportsQweb(models.AbstractModel):
    _name = 'report.technical_reports.technical_reports_qweb'

    @api.multi
    def render_html(self, docids, data=None):
        print self.env.context, docids
        #model = self.env.context.get('active_model')
        #docs = self.env[model].browse(self.env.context.get('active_id'))

        docs = self.env['report.reports'].browse(docids)

        docargs = {
            'timediff':self._timediff,
            'docs': docs,
        }
        return self.env['report'].render(
            'technical_reports.technical_reports_qweb', docargs)

    def _timediff(self, toDate, fromDate):
        if toDate and fromDate:
            date1 = datetime.strptime(toDate, '%Y-%m-%d %H:%M:%S')
            date2 = datetime.strptime(fromDate, '%Y-%m-%d %H:%M:%S')
            return date1 - date2


class ExternalReportsQweb(models.AbstractModel):
    _name = 'report.technical_reports.technical_reports_external_qweb'

    @api.multi
    def render_html(self, docids, data=None):
        print self.env.context, docids
        #model = self.env.context.get('active_model')
        #docs = self.env[model].browse(self.env.context.get('active_id'))

        docs = self.env['report.reports'].browse(docids)

        docargs = {
            'timediff':self._timediff,
            'docs': docs,
        }
        return self.env['report'].render(
            'technical_reports.technical_reports_external_qweb', docargs)

    def _timediff(self, toDate, fromDate):
        if toDate and fromDate:
            date1 = datetime.strptime(toDate, '%Y-%m-%d %H:%M:%S')
            date2 = datetime.strptime(fromDate, '%Y-%m-%d %H:%M:%S')
            return date1 - date2
