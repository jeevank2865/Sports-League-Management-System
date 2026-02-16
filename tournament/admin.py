from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Sport, Tournament, Team, Player, Match, PointsTable

# CUSTOM USER 
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

# TEAM ADMIN
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'captain')
    fields = ('name', 'coach_name', 'tournament', 'captain')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "captain":
            kwargs["queryset"] = CustomUser.objects.filter(role='captain')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# MATCH ADMIN 
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'team1', 'team2', 'scheduled_date', 'status')
    list_filter = ('tournament', 'status')

    def get_form(self, request, obj=None, **kwargs):
        """
        obj is the Match instance when editing (Update Match Result)
        """
        form = super().get_form(request, obj, **kwargs)

        if obj:  
            form.base_fields['winner'].queryset = Team.objects.filter(
                id__in=[obj.team1_id, obj.team2_id]
            )
            form.base_fields['POM'].queryset = Player.objects.filter(
                team__in=[obj.team1, obj.team2]
            )
        else: 
            form.base_fields['winner'].queryset = Team.objects.none()
            form.base_fields['POM'].queryset = Player.objects.none()

        return form

# REGISTER OTHERS 
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Sport)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(PointsTable)