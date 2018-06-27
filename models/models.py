# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Shop(models.Model):
    _name = 'rental.shop'

    number = fields.Integer(string="Numero")
    area = fields.Float(string="Area")
    watermeter = fields.Integer(string="Medidor Agua")
    currentmeter = fields.Integer(string="Medidor Electrico")
    floor_id = fields.Many2one('rental.floor', string="Piso")

class Floor(models.Model):
    _name = 'rental.floor'

    number = fields.Integer(string="Numero")
    shop = fields.One2many('rental.shop', 'floor_id', string="Locales")
