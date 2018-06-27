# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Shop(models.Model):
    _name = 'rental.shop'

    number = fields.Integer(string="Numero")
    area = fields.Float(string="Area")
    watermeter = fields.Integer(string="Medidor Agua")
    currentmeter = fields.Integer(string="Medidor Electrico")
    floor_id = fields.Many2one('rental.floor', string="Piso")
    document_id = fields.Many2one('rental.document', string="Documento")

    _sql_constraints = [
        ('number_unique',
         'UNIQUE(number)',
         "Ya existe un local con ese numero")
    ]

class Floor(models.Model):
    _name = 'rental.floor'

    number = fields.Integer(string="Numero")
    shop = fields.One2many('rental.shop', 'floor_id', string="Locales")
    building_id = fields.Many2one('rental.building', string="Edificio")

    _sql_constraints = [
        ('number_unique',
         'UNIQUE(number)',
         "Ya existe un piso con ese numero")
    ]

class Building(models.Model):
    _name = 'rental.building'

    name = fields.Char(string="Nombre")
    address = fields.Text(string="Direccion")
    total_area = fields.Float(string="Area de terreno")
    built_area = fields.Float(string="Area construida")
    floors = fields.One2many('rental.floor', 'building_id', string="Pisos")
    real_value = fields.Float(string="Valor Real")
    fiscal_value = fields.Float(string="Valor Fiscal")

    _sql_constraints = [
        ('mane_unique',
         'UNIQUE(name)',
         "Ya existe un edificio con ese nombre")
    ]

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
