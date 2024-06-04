from app.tasks.views import *

tasks.add_url_rule("/createtask", view_func=Createtask.as_view('createtask'))
tasks.add_url_rule("/taskfilter", view_func=Taskfilter.as_view('taskfilter'))
tasks.add_url_rule("/executetask", view_func=Executetask.as_view('executetask'))
tasks.add_url_rule("/taskreport", view_func=Taskreport.as_view('taskreport'))
tasks.add_url_rule("/reruntask", view_func=Reruntask.as_view('reruntask'))
tasks.add_url_rule("/creatorlist", view_func=Creatorlist.as_view('creatorlist'))









