# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

def timediff(toDate, fromDate):
    if toDate and fromDate:
        date1 = datetime.strptime(toDate, '%Y-%m-%d %H:%M:%S')
        date2 = datetime.strptime(fromDate, '%Y-%m-%d %H:%M:%S')
        result = date1 - date2
        days = result.days*24
        hours, remainder = divmod(result.seconds, 3600.0)
        minutes, seconds = divmod(remainder, 60.0)
        return days + hours + (minutes / 60.0)


class TechnicalReportsAdvancePaymentInv(models.TransientModel):

    _name = "technical.reports.advance.payment.inv"
    _description = "Technical Report Advance Payment Invoice"

    @api.model
    def _default_product_id(self):
        product_id = self.env.user.company_id.labor_service_id
        return product_id

    @api.model
    def _default_travel_product_id(self):
        travel_product_id = self.env.user.company_id.travel_product
        return travel_product_id

    @api.model
    def travel_cost(self, distance):
        cost_rules = self.env['technical.report.travel.costs'].search([
                ('from_km', '<=', distance),
                ('to_km', '>=', distance)
            ])
        if not cost_rules:
            raise UserError(
                _(
                    'A rule has not been defined for this kilometric value.'
                    ' You may have set it in a configuration menu. ')
                )
        elif len(cost_rules)>1:
            raise UserError(
                _(
                    'More rules has been defined for this kilometric value. '
                    'You may have modify them in a configuration menu. ')
            )
        else:
            travel_cost = cost_rules.fixed_cost + (
                    cost_rules.variable_cost * distance)
            return travel_cost

    product_id = fields.Many2one('product.product',
                                 default=_default_product_id)
    travel_product_id = fields.Many2one('product.product',
                                 default=_default_travel_product_id)

    @api.multi
    def _create_invoice(self, report):
        inv_obj = self.env['account.invoice']
        if self.product_id.id:
            account_id = \
                self.product_id.property_account_income_id.id or \
                self.product_id.categ_id.property_account_income_categ_id.id
            if self.product_id.taxes_id.id:
                taxes_ids = [(6, 0, [self.product_id.taxes_id.id])]
            else:
                taxes_ids = False
        else:
            raise UserError(
                _(
                    'A labor service has not been defined. '
                    'You may have set it in a configuration menu.')
                )
        if not report.end_activity_date or not report.start_activity_date:
            raise UserError(
                _('Insert the start activity date and the end activity '
                  'to generate the invoice')
            )
        else:
            invoice_lines = [(0, 0, {
                'name': self.product_id.name +
                        ' from ' +
                        report.start_activity_date +
                        ' to ' +
                        report.end_activity_date,
                'origin': report.name,
                'account_id': account_id,
                'price_unit': self.product_id.list_price,
                'quantity': timediff(
                    report.end_activity_date, report.start_activity_date),
                'discount': 0.0,
                'uom_id': self.product_id.uom_id.id,
                'product_id': self.product_id.id,
                'invoice_line_tax_ids': taxes_ids,
            })]
            if report.end_journey_date and report.start_journey_date and \
                    report.intervention_place.distance > 0 :
                if not self.travel_product_id:
                    raise UserError(
                        _(
                            'A travel product has not been defined.'
                            ' You may have set it in a configuration menu.')
                         )
                else:
                    if self.travel_product_id.taxes_id.id:
                        travel_taxes_ids = [(6, 0, [
                            self.travel_product_id.taxes_id.id])]
                    else:
                        travel_taxes_ids = False
                    invoice_lines.append((0, 0, {
                    'name': self.travel_product_id.name +
                            ' of ' +
                            report.name + ' ('
                            + str(report.intervention_place.distance) + ' km)',
                    'origin': report.name,
                    'account_id': account_id,
                    'price_unit': self.travel_cost(
                        report.intervention_place.distance),
                    'quantity': 1.0,
                    'discount': 0.0,
                    'uom_id': self.travel_product_id.uom_id.id,
                    'product_id': self.travel_product_id.id,
                    'invoice_line_tax_ids': travel_taxes_ids,
                }))
            invoice = inv_obj.create({
                'name': report.name,
                'origin': report.name,
                'type': 'out_invoice',
                'reference': False,
                'account_id':
                    report.partner_id.property_account_receivable_id.id,
                'partner_id': report.partner_id.id,
                'partner_shipping_id': report.intervention_place.id,
                'invoice_line_ids': invoice_lines,
            })
            report.invoice_id = invoice.id
            report.state = 'done'
            return invoice

    @api.multi
    def create_invoices(self):
        technical_reports = self.env['technical.report'].browse(
            self._context.get('active_ids', []))
        for report in technical_reports:
            self._create_invoice(report)
        if self._context.get('open_invoices', False):
            return technical_reports.action_view_invoice()
        return {'type': 'ir.actions.act_window_close'}
