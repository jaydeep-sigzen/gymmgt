from . import __version__ as app_version

app_name = "gymmgt"
app_title = "Gym Management"
app_publisher = "Jaydeep-Sigzen"
app_description = "A gym management system is a software application designed to help gym owners and managers streamline their operations and manage day-to-day tasks. This may include things like membership management, scheduling, billing and payments, facility and equipment management, and reporting and analytics."
app_email = "jaydeep@sigzen.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/gymmgt/css/gymmgt_desk.css"
# app_include_js = "/assets/gymmgt/js/gymmgt.js"

required_apps = ["erpnext"]

# include js, css files in header of web template
web_include_css = "/assets/gymmgt/css/gymmgt_web.css"
# web_include_js = "/assets/gymmgt/js/gymmgt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gymmgt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# website user home page (by Role)
# role_home_page = {
# "Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# "methods": "gymmgt.utils.jinja_methods",
# "filters": "gymmgt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gymmgt.install.before_install"
# after_install = "gymmgt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gymmgt.uninstall.before_uninstall"
# after_uninstall = "gymmgt.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gymmgt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }

permission_query_conditions = {
    "Gym Members":
    "gymmgt.permission.query.get_permission_query_conditions_for_gym_member",
    "Gym Trainer":
    "gymmgt.permission.query.get_permission_query_conditions_for_trainer"
}

#
# has_permission = {
# "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# "*": {
# "on_update": "method",
# "on_cancel": "method",
# "on_trash": "method"
# }
# }
fixtures = [{
    "dt":
    "Role",
    "filters": [["name", "in", ["Gym Member", "Gym Trainer", "Gym Admin"]]]
}, {
    "dt": "Role Profile",
    "filters": [["name", "in", ["Gym Member", "Gym Trainer"]]]
}, {
    'dt': "Module Profile"
}, {
    'dt': "Web Page"
}, {
    'dt': "Website Settings"
}, {
    'dt': "Custom DocPerm"
}]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# "all": [
# "gymmgt.tasks.all"
# ],
# "daily": [
# "gymmgt.tasks.daily"
# ],
# "hourly": [
# "gymmgt.tasks.hourly"
# ],
# "weekly": [
# "gymmgt.tasks.weekly"
# ],
# "monthly": [
# "gymmgt.tasks.monthly"
# ],
# }

# Testing
# -------

# before_tests = "gymmgt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# "frappe.desk.doctype.event.event.get_events": "gymmgt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# "Task": "gymmgt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gymmgt.utils.before_request"]
# after_request = ["gymmgt.utils.after_request"]

# Job Events
# ----------
# before_job = ["gymmgt.utils.before_job"]
# after_job = ["gymmgt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# {
# "doctype": "{doctype_1}",
# "filter_by": "{filter_by}",
# "redact_fields": ["{field_1}", "{field_2}"],
# "partial": 1,
# },
# {
# "doctype": "{doctype_2}",
# "filter_by": "{filter_by}",
# "partial": 1,
# },
# {
# "doctype": "{doctype_3}",
# "strict": False,
# },
# {
# "doctype": "{doctype_4}"
# }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# "gymmgt.auth.validate"
# ]
