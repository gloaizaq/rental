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
    building_id = fields.Many2one('rental.building', string="Edificio")

class Building(models.Model):
    _name = 'rental.building'

    name = fields.Char(string="Nombre")
    address = fields.Text(string="Direccion")
    total_area = fields.Float(string="Area de terreno")
    built_area = fields.Float(string="Area construida")
    floors = fields.One2many('rental.floor', 'building_id', string="Pisos")
    real_value = fields.Float()
    fiscal_value = fields.Float()
