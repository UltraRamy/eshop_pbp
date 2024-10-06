from django.urls import path
from main.views import edit, delete, add_mood_entry_ajax
from main.views import show_main, create_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('create-entry', create_entry, name='create_entry'),
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<uuid:id>', edit, name='edit'),
    path('delete/<uuid:id>', delete, name='delete'),
    path('create-ajax', add_mood_entry_ajax, name='add_mood_entry_ajax'),
        
]