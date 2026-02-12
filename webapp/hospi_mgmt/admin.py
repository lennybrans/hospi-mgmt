from django.contrib import admin

import hospi_mgmt.models as mdl


# Register your models here.
class AvailabilityAdmin(admin.ModelAdmin):
    pass


class OccupantAdmin(admin.ModelAdmin):
    pass


admin.site.register(mdl.Availability, AvailabilityAdmin)
admin.site.register(mdl.Occupant, OccupantAdmin)
