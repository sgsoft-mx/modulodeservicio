# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

import time
from openerp.report import report_sxw

class PrintOrder(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(PrintOrder, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'total': self.total,
        })

    def total(self, servicemc):
        total = 0.0
        for operation in servicemc.operations:
           total += operation.price_subtotal
        for fee in servicemc.fees_lines:
           total += fee.price_subtotal
        total = total + servicemc.amount_tax
        return total

report_sxw.report_sxw('report.servicemc.order','mrp.servicemc','addons/mrp_servicemc/report/print_order.rml',parser=PrintOrder)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

