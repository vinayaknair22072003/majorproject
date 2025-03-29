from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name='index'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('userreg/',views.userreg,name='userreg'),
    path('user_list_view/',views.user_list_view,name='user_list_view'),
    path('login/',views.login,name='login'),
    path('user_edit_view/',views.user_edit_view,name='user_edit_view'),
    path('userhome/',views.userhome,name='userhome'),
    path('station_reg/',views.station_reg,name='station_reg'),
    path('adminchargingstationview/',views.charging_station_admin_view,name='adminchargingstationview'),
    path('station_table',views.StationTable,name="StationName"),
    path('adminuserview',views.admuserview,name='adminuserview'),
    path('stationsearch',views.stationsearch,name='stationsearch'),
    path('chargestaionhome',views.chargestationhome,name='chargestataionhome'),
    path('chargestaionprofile',views.stationprofile,name='chargestationprofile'),
    path('view_advertisement',views.advertisement,name='advertisement'),
    path('advertisememnt_view',views.advertisememnt_view,name='advertisememnt_view'),
    path('adminstation_view',views.adminstation_view,name='adminstation_view'),
    path('advertisement_edit/<int:id>',views.advertisement_edit,name='advertisement_edit'),
    path('advertisememnt_view_user',views.advertisememnt_view_user,name='advertisememnt_view_user'),
    path('advertisement_delete/<int:id>',views.advertisement_delete,name='advertisement_delete'),
    path('slotbookings/<int:login_id>/', views.slotbookings, name='slotbookings'),
    path('slotbookingview',views.slotbookingview,name='slotbookingview'),
    path('slotedit/<int:id>',views.slotedit,name='slotedit'),
    path('slot_cancel/<int:id>',views.slot_cancel,name='slot_cancel'),
    path('slotstationview',views.slotstationview,name='slotstationview'),
    path('slot_delete/<int:id>',views.slot_delete,name='slot_delete'),
    path('feedback/<int:id>',views.feedbacks,name='feedback'),
    path('view_feedback/<int:id>',views.view_feedback,name='view_feedback'),
    path('user_feedback/', views.user_feedback, name='user_feedback'),
    path('edit_feedback/<int:id>',views.edit_feedback, name='edit_feedback'),
    path('delete_feedback/<int:id>',views.delete_feedback, name='delete_feedback'),
    path('complaint_add',views.complaint_add, name='complaint_add'),
    path('view_complaints/',views.view_complaints, name='view_complaints'),
    path('user_viewcomplaints/',views.user_viewcomplaints, name='user_viewcomplaints'),
    path('edit_complaint/<int:id>/',views.edit_complaint, name='edit_complaint'),
    path('delete_complaint/<int:id>/',views.delete_complaint, name='delete_complaint'),
    path('complaint_reply/<int:id>/',views.complaint_reply, name='complaint_reply'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
