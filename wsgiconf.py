# from gevent import monkey
# monkey.patch_all(thread=False, select=False)
#
# import multiprocessing
#
# bind = '0.0.0.0:5000'
# workers = multiprocessing.cpu_count() * 2 + 1
#
# backlog = 2048
# worker_class = "gevent"
# worker_connections = 1000
# daemon = False
# debug = True
# proc_name = 'kiwitest'
# pidfile = './log/gunicorn.pid'
# errorlog = './log/gunicorn.log'