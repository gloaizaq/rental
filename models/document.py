# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Document(models.Model):
    _name = 'rental.document'

    client_id = fields.Many2one('res.partner', string="Cliente")
    contract_number = fields.Integer(string="Numero de contrato")
    shops = fields.One2many('rental.shop', 'document_id' , string="Locales")
    montly_rent_fee = fields.Float(string="Monto mensual")
    montly_manteinance_fee = fields.Float(string="Monto mantenimiento")
    #issued_invoices = Many2one('account.invoice', string="Facturas emitidas")
    start_date = fields.Date(string="Fecha Inicio")
    end_date = fields.Date(string="Fecha Final")
    annual_increase_percentage = fields.Float(string="Porcentaje de incremento Anual")
