from app.projects.views import *

project.add_url_rule("/createproject", view_func=CreateProject.as_view('createproject'))
project.add_url_rule("/deleteproject", view_func=DeleteProject.as_view('deleteproject'))
project.add_url_rule("/updateproject", view_func=UpdateProject.as_view('updateproject'))
project.add_url_rule('/getbyid/<int:id>', view_func=GetPrjById.as_view('getbyid'))
project.add_url_rule('/getbyname/<string:name>', view_func=GetPrjByName.as_view('getbyname'))
project.add_url_rule('/getallproject', view_func=GetAllPrj.as_view('getallproject'))
project.add_url_rule('/createdb', view_func=CreateDb.as_view('createdb'))
project.add_url_rule('/modifyfdb', view_func=ModifyDb.as_view('modifyfdb'))
project.add_url_rule('/getdbbyid/<int:id>', view_func=GetDbById.as_view('getdbbyid'))
project.add_url_rule('/getalldb', view_func=GetAllDb.as_view('getalldb'))
project.add_url_rule('/createdbfac', view_func=CreateDbfac.as_view('createdbfac'))
project.add_url_rule('/getdfbyid/<int:id>', view_func=GetFacByid.as_view('getdfbyid'))
project.add_url_rule('/getalldf', view_func=GetAllDf.as_view('getalldf'))
project.add_url_rule('/modifydbf', view_func=ModifyDbf.as_view('modifydbf'))
project.add_url_rule('/createenv', view_func=CreateEnv.as_view('createenv'))
project.add_url_rule('/getenvforprjid/<int:id>', view_func=GetConfForP.as_view('getenvforprjid'))
project.add_url_rule('/modproconf', view_func=ModifyProConf.as_view('modproconf'))
project.add_url_rule('/createmodel', view_func=CreateModel.as_view('createmodel'))
project.add_url_rule('/modifymodel', view_func=ModifyModel.as_view('modifymodel'))
project.add_url_rule('/getmodelbyid/<int:id>', view_func=GetModelById.as_view('getmodelbyid'))
project.add_url_rule('/getallmodel', view_func=GetAllModel.as_view('getallmodel'))
project.add_url_rule('/getmodelbyprjid/<int:id>', view_func=GetModelByPrjId.as_view('getmodelbyprjid'))
project.add_url_rule('/exedbfac', view_func=ExeDbFac.as_view('exedbfac'))
project.add_url_rule("/addproject", view_func=AddProject.as_view('addproject'))




