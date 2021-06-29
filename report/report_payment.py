# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.addons.l10n_gt_extra import a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'onyx.abstract.reporte_account_payment'

    def fecha_a_letras(self,fecha):
        fecha_letras = ""
        dia = fecha.strftime('%d')
        mes = int(fecha.strftime('%m'))
        mes_letras = a_letras.mes_a_letras(mes-1)
        anio = fecha.strftime('%Y')
        fecha_letras = dia + " de " + mes_letras.capitalize() + " del " + anio
        return fecha_letras

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_id.line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    def _get_report_values(self, docids, data=None):
        model = 'account.payment'
        docs = self.env['account.payment'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'a_letras': a_letras.num_a_letras,
            'fecha_a_letras': self.fecha_a_letras,
            'totales': self.totales,
        }

class ReportPayment1(models.AbstractModel):
    _name = 'report.onyx.reporte_account_payment1'
    _inherit = 'onyx.abstract.reporte_account_payment'
