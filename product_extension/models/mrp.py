from odoo import api, fields, models, _

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    sale_partner_id = fields.Many2one('res.partner','Customer')
    product_type = fields.Selection([
        ('cast','Cast Stone'),
        ('raw','Rock Raw'),
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

    slabs_template = fields.Char('Template')

    address_blocks_type = fields.Char('Address Block Type')
    address_blocks_color = fields.Char('Color')

    @api.onchange('product_id')
    def product_attribute_change(self):
        self.sale_partner_id = self.product_id.sale_partner_id
        self.product_type = self.product_id.product_type
        self.uas = self.product_id.uas
        self.cast_color = self.product_id.cast_color
        self.cast_pieces = self.product_id.cast_pieces
        self.raw_type = self.product_id.raw_type
        self.raw_cut = self.product_id.raw_cut
        self.raw_size = self.product_id.raw_size
        self.tv_height1 = self.product_id.tv_height1
        self.tv_height2 = self.product_id.tv_height2
        self.tv_height3 = self.product_id.tv_height3
        self.tv_height4 = self.product_id.tv_height4
        self.tv_size = self.product_id.tv_size
        self.arches_radius = self.product_id.arches_radius
        self.arches_rise = self.product_id.arches_rise
        self.arches_plate = self.product_id.arches_plate
        self.slabs_template = self.product_id.slabs_template
        self.address_blocks_type = self.product_id.address_blocks_type
        self.address_blocks_color = self.product_id.address_blocks_color


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    sale_partner_id = fields.Many2one('res.partner','Customer',related='production_id.sale_partner_id',store=True)

    @api.multi
    def name_get(self):
        return [(wo.id, "%s - %s" % (wo.production_id.name, wo.production_id.sale_partner_id.name)) for wo in self]
