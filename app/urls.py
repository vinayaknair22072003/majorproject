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
    

    
    

   ]   +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
