# -*- coding: utf-8 -*-
# (c) 2017 Consultoría Informática Studio 73 S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Suministro Inmediato de Información de importaciones con DUA",
    "version": "12.0.0.1.0",
    "category": "Accounting & Finance",
    "website": "https://odoo-community.org/",
    "author": "Consultoría Informática Studio 73 S.L., "
              "Acysos S.L.",
    "license": "AGPL-3",
    "depends": [
        "l10n_es_aeat_sii",
        "l10n_es_dua",
    ],
    "data": [
        "data/aeat_sii_map_data_1_1.xml"
    ],
    "application": False,
    "installable": True,
    "auto_install": True,
}
