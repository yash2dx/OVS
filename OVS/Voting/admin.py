from django.contrib import admin
from Voting.models import *
# Register your models here.



admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(AddElections)
admin.site.register(AlreadyVoted)
admin.site.register(Election)
admin.site.register(MainElection)
admin.site.register(SeatDetails)