from django.contrib import admin

from .models import Team, Mentor, Meetup, Coworking, Post, Event, Application, \
    ImageMedia, About, OkthessMeetup, ResourceCategory, Resource, ApplyText, Partner

admin.site.register(Team)
admin.site.register(Mentor)
admin.site.register(Meetup)
admin.site.register(Coworking)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Application)
admin.site.register(ImageMedia)
admin.site.register(About)
admin.site.register(OkthessMeetup)
admin.site.register(ResourceCategory)
admin.site.register(Resource)
admin.site.register(ApplyText)
admin.site.register(Partner)
