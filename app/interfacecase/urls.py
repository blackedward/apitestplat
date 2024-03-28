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
interfacecase.add_url_rule("/updatecasebase", view_func=Updatecasebase.as_view('updatecasebase'))
interfacecase.add_url_rule("/updatecasereq", view_func=Updatecasereq.as_view('updatecasereq'))
interfacecase.add_url_rule("/updatecasesql", view_func=Updatecasesql.as_view('updatecasesql'))
interfacecase.add_url_rule("/getprecase", view_func=Getprecase.as_view('getprecase'))
interfacecase.add_url_rule("/getcasedetail", view_func=Getcasedetail.as_view('getcasedetail'))
interfacecase.add_url_rule("/deletecase", view_func=Deletecase.as_view('deletecase'))
interfacecase.add_url_rule("/getcaseres", view_func=Getcaseres.as_view('getcaseres'))
interfacecase.add_url_rule("/allcases", view_func=Allcases.as_view('allcases'))
interfacecase.add_url_rule("/getbranchproto", view_func=Getbranchproto.as_view('getbranchproto'))
interfacecase.add_url_rule("/getprotomessages", view_func=GetMessageInfo.as_view('getprotomessages'))
interfacecase.add_url_rule("/getattbymessage", view_func=Getattbymessage.as_view('getattbymessage'))
interfacecase.add_url_rule("/executeproto", view_func=Executeproto.as_view('executeproto'))
interfacecase.add_url_rule("/onesaveproto", view_func=Onesaveproto.as_view('onesaveproto'))
interfacecase.add_url_rule("/getbranches", view_func=Getbranches.as_view('getbranches'))
interfacecase.add_url_rule("/forceupdatebranch", view_func=Forceupdatebranch.as_view('forceupdatebranch'))
interfacecase.add_url_rule("/executeprotomult", view_func=ExecuteprotoMult.as_view('executeprotomult'))
interfacecase.add_url_rule("/createsuite", view_func=Createsuite.as_view('createsuite'))
interfacecase.add_url_rule("/getsuitebyid", view_func=Getsuitebyid.as_view('getsuitebyid'))
interfacecase.add_url_rule("/getsuitebyname", view_func=Getsuitebyname.as_view('getsuitebyname'))
interfacecase.add_url_rule("/getsuitebyproj", view_func=Getsuitebyproj.as_view('getsuitebyproj'))
interfacecase.add_url_rule("/updatesuite", view_func=Updatesuite.as_view('updatesuite'))
interfacecase.add_url_rule("/deletesuite", view_func=Deletesuite.as_view('deletesuite'))
interfacecase.add_url_rule("/exemulproto", view_func=Exemulproto.as_view('exemulproto'))
interfacecase.add_url_rule("/getallbrmes", view_func=Getallbrmes.as_view('getallbrmes'))
interfacecase.add_url_rule("/autogencase", view_func=Autogencase.as_view('autogencase'))
interfacecase.add_url_rule("/saveautocases", view_func=Saveautocases.as_view('saveautocases'))





















