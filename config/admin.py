from django.contrib import admin


class OmnibackAdminSite(admin.AdminSite):
    title_header = "Omniback Admin"
    site_header = "Omniback Administration"
    index_title = "Omniback Site Admin"
    site_title = "Omniback | Site"
