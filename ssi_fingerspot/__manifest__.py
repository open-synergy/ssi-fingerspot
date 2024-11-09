# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Fingerspot Attendance Machine Integration with Odoo",
    "version": "14.0.3.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "external_dependencies": {"python": ["pandas"]},
    "depends": [
        "ssi_timesheet_attendance",
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_date_duration_mixin",
        "ssi_transaction_queue_done_mixin",
        "ssi_transaction_queue_cancel_mixin",
        "ssi_m2o_configurator_mixin",
        "base_automation",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "data/ir_cron.xml",
        "data/ir_cron_import_attendance.xml",
        "data/hr_attendance_reason.xml",
        "menu.xml",
        "views/fingerspot_data_machine_views.xml",
        "views/fingerspot_attendance_machine_views.xml",
        "views/fingerspot_backend_views.xml",
        "views/res_company_views.xml",
        "views/hr_timesheet_attendance_views.xml",
        "views/fingerspot_attendance_machine_batch_views.xml",
    ],
}
