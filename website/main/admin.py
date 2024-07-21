from django.contrib import admin
from .models import Problem, Funding

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('problem_type', 'locality', 'description', 'geo_location', 'progress', 'created_by')
    list_filter = ('progress', 'created_by')
    search_fields = ('problem_type', 'locality', 'description')
    list_editable = ('progress',)
    def get_readonly_fields(self, request, obj=None):
        # Ensure that progress is editable for all users
        readonly_fields = list(self.readonly_fields)
        if not request.user.is_superuser:
            readonly_fields.append('created_by')  # Only add fields you want to be read-only for non-superusers
        return readonly_fields

admin.site.register(Problem, ProblemAdmin)

# admin.py



class FundingAdmin(admin.ModelAdmin):
    list_display = ('upi_id', 'amount', 'date_submitted')

admin.site.register(Funding,FundingAdmin)