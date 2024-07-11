from app.tools.views import *


tools.add_url_rule("/changecard", view_func=Changecard.as_view('changecard'))
tools.add_url_rule("/addvar", view_func=Addvar.as_view('addvar'))
tools.add_url_rule("/delvar", view_func=Delvar.as_view('delvar'))
tools.add_url_rule("/varlist", view_func=Varlist.as_view('varlist'))
tools.add_url_rule("/getvar", view_func=Getvar.as_view('getvar'))
tools.add_url_rule("/updatevar", view_func=Updatevar.as_view('updatevar'))


