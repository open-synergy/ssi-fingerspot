# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Fingerspot Attendance Machine Integration + Operating Unit",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_fingerspot",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/fingerspot_attendance_machine_batch.xml",
        "security/ir_rule/fingerspot_attendance_machine_batch.xml",
        "view/fingerspot_attendance_machine_batch.xml",
    ],
}
