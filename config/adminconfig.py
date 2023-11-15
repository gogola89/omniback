from django.contrib.admin.apps import AdminConfig


class OmnibackAdminConfig(AdminConfig):
    default_site = "config.admin.OmnibackAdminSite"
