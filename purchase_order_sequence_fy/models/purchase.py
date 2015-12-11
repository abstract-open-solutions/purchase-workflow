# -*- coding: utf-8 -*-
# © 2015 davide.corio@abstract.it
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def create(self, cr, uid, vals, context=None):
        context = context or {}
        fy_model = self.pool['account.fiscalyear']
        fy_id = fy_model.find(cr, uid, vals['date_order'])
        context.update({'fiscalyear_id': fy_id})
        return super(PurchaseOrder, self).create(cr, uid, vals, context)
