from Voting import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name="home"),
    path('register_voter',views.register_voter,name="register_voter"),
    path('register_candidate',views.register_candidate,name="register_candidate"),
    path('login_voter',views.login_voter,name="login_voter"),
    path('login_candidate',views.login_candidate,name="login_candidate"),
  #  path('voters_logged_in/<str:username>',views.voters_logged_in,name="voters_logged_in"),
    path('voter_profile/<int:id>/',views.voter_profile,name="voter_profile"),
    path('candidate_profile/<int:id>/',views.candidate_profile,name="candidate_profile"),
    path('candidate_nomination',views.candidate_nomination,name="nomination"),
    path('do_cast_your_vote',views.castVote,name="castVote"),
    path('result',views.result,name="result"),
    path('history',views.history,name="history"),
    path('result/<str:state>',views.resultstate,name="resultstate"),
    path('history/<str:state>',views.historystate,name="historystate"),
    path('history/<str:state>/<str:election_name>',views.historyelection,name="historyelection"),
    path('api',views.apiOverview,name="api-overview"),
    path('seatEntry',views.output_SeatEntry,name='seatEntry'),
    path('InputSeatEntry/',views.CreateSeatEntry,name="CreateSeat")
    #path('otp_verify/<str:voterid>',views.otp_verification,name="otpV")
]