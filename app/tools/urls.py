from app.tools.views import *


tools.add_url_rule("/changecard", view_func=Changecard.as_view('changecard'))


