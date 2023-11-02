from app.interfacecase.views import *

interfacecase.add_url_rule("/createcase", view_func=CreateCase.as_view('createcase'))
interfacecase.add_url_rule("/modifycase", view_func=ModifyCase.as_view('modifycase'))
interfacecase.add_url_rule("/createassert", view_func=CreateAssert.as_view('createassert'))
interfacecase.add_url_rule("/getcaseassert", view_func=GetCaseAssert.as_view('getcaseassert'))
interfacecase.add_url_rule("/modifyassert", view_func=ModifyAssert.as_view('modifyassert'))
interfacecase.add_url_rule("/getcasebymod", view_func=GetCaseByMod.as_view('getcasebymod'))
interfacecase.add_url_rule("/executecase", view_func=ExecuteCase.as_view('executecase'))
interfacecase.add_url_rule("/addprecase", view_func=AddPreCase.as_view('addprecase'))
interfacecase.add_url_rule("/addcase", view_func=AddCase.as_view('addcase'))
interfacecase.add_url_rule("/getcasebyproj", view_func=GetCaseByProj.as_view('getcasebyproj'))
interfacecase.add_url_rule("/updateprecase", view_func=Updateprecase.as_view('updateprecase'))


