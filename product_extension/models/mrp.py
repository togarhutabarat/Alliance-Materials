from odoo import api, fields, models, _

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    sale_partner_id = fields.Many2one('res.partner','Customer')
    address = fields.Text('Address')
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

    address_blocks_size = fields.Many2one('block.size','Size')
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
        result = []
        for wo in self:
            group_productions = self.env['mrp.production'].search([('procurement_group_id','=',wo.production_id.procurement_group_id.id)])
            address = ""
            for mo in group_productions:
                address = mo.address
                if address:
                    break
            if address:
                result.append((wo.id, "%s - %s" % (wo.production_id.name, address)))
            else:
                result.append((wo.id, "%s" % (wo.production_id.name)))
        return result

        # return [(wo.id, "%s - %s" % (wo.production_id.name, wo.production_id.sale_partner_id.name)) for wo in self]

        # result = []
        # for wo in self:
        #     name = "%s" % (wo.production_id.name)
        #     group_productions = self.env['mrp.production'].search(['procurement_group_id','=',wo.production_id.procurement_group_id])
        #     customer_name = ""
        #     for mo in group_productions:
        #         customer_name = mo.sale_partner_id and mo.sale_partner_id.name or ""
        #         if customer_name:
        #             break
        #     if customer_name:
        #         name = "%s - %s" % (wo.production_id.name, customer_name)
        #     else:
        #         name = "%s" % (wo.production_id.name)
        #     result.append((wo.id, name))
        #     return result
