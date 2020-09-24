# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api


class TechnicalReportsQweb(models.AbstractModel):

    _name = 'report.technical_reports.technical_reports_qweb'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name(
            'technical_reports.technical_reports_qweb')

        docs = self.env['technical.report'].browse(docids)
        docargs = {
            'timediff': self._timediff,
            'docs': docs,
            'doc_ids': docids,
            'doc_model': report.model
        }
        return docargs

    def _timediff(self, toDate, fromDate):
        if toDate and fromDate:
            return toDate - fromDate


class ExternalReportsQweb(models.AbstractModel):
    _name = 'report.technical_reports.technical_reports_external_qweb'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name(
            'technical_reports.technical_reports_external_qweb')

        docs = self.env['technical.report'].browse(docids)
        docargs = {
            'timediff': self._timediff,
            'docs': docs,
            'doc_ids': docids,
            'doc_model': report.model
        }
        return docargs

    def _timediff(self, toDate, fromDate):
        if toDate and fromDate:
            if toDate and fromDate:
                return toDate - fromDate


class CalendarReportsQweb(models.AbstractModel):
    _name = 'report.technical_reports.calendar_reports_qweb'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name(
            'technical_reports.calendar_reports_qweb')

        docs = self.env['calendar.event'].browse(docids)
        docargs = {
            'docs': docs,
            'doc_ids': docids,
            'doc_model': report.model
        }
        return docargs
