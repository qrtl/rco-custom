import logging

from odoo import fields, models


class LotLabelLayout(models.TransientModel):
    _inherit = "lot.label.layout"

    print_format = fields.Selection(
        selection_add=[("A4", "A4")], ondelete={"A4": "cascade"}
    )

    def process(self):
        report_action = super(LotLabelLayout, self).process()
        # Replace xml_id or modify the result
        if self.print_format == "A4":
            logging.info("Testing__________")
            logging.info(report_action)
            new_xml_id = "report_lot_custom_layout.action_report_lot_custom_label"
            docids = report_action.get("context", {}).get("active_ids", [])
            report_action = self.env.ref(new_xml_id).report_action(docids)

        return report_action
