# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RawRockType(models.Model):

    _name = "raw.rock.type"
    _description = "Raw Rock Types"

    name = fields.Char('Name')

class BlockSize(models.Model):

    _name = "block.size"
    _description = "Address Block Size"

    name = fields.Char('Size')

class Product(models.Model):
    _inherit = "product.template"

    sale_partner_id = fields.Many2one('res.partner','Customer')
    product_type = fields.Selection([
        ('cast','Cast Stone'),
        ('tv','TV'),
        ('arches','Arches'),
        ('slabs','Slabs'),
        ('address','Address Blocks')],'Type')
    uas = fields.Char('UAS #')
    
    cast_color = fields.Char('Color')
    cast_pieces = fields.Integer('Pieces')

    raw_type = fields.Selection([
        ('arkansas','Arkansas Moss'),
        ('texas','Texas Moss'),
        ('austin','Austin Chalk'),
        ('chocolate','Chocolate'),
        ('ciniman','Ciniman Stripes'),
        ('dubois','Dubois'),
        ('grandbury','Grandbury'),
        ('brand_blueline','Grandbury Blueline')], 'Raw Rock Type')
    raw_type_id = fields.Many2one('raw.rock.type','Raw Rock Type')
    raw_cut = fields.Selection([
        ('chopped','Chopped'),
        ('flagstone','FlagStone'),
        ('random','Random'),
        ('river','River'),
        ('slab','Slab'),
        ('ruders','Ruders')], 'Cut')
    raw_size = fields.Integer('Size (tons)')

    tv_height1 = fields.Integer('Height #1')
    tv_height2 = fields.Integer('Height #2')
    tv_height3 = fields.Integer('Height #3')
    tv_height4 = fields.Integer('Height #4')
    tv_size = fields.Integer('TV Size (feet)')

    arches_radius = fields.Float('Radius')
    arches_rise = fields.Char('Rise')
    arches_plate = fields.Char('Plate')

    polish_level = fields.Selection([('natural','Natural'),
        ('sanded','Sanded'), ('leathered','Leathered'), ('honed','Honed'), ('polished','Polished')], 'Polish Level')
    slabs_template = fields.Char('Template')

    address_blocks_type = fields.Char('Address Block Type')
    address_blocks_size = fields.Many2one('block.size','Size')
    address_blocks_color = fields.Char('Color')
