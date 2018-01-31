# time.py 
#
# (c) 2010 Michel J. Anders (varkenvarken)
#
# all rights reserved

import cherrypy
import os.path
from time import asctime

current_dir = os.path.dirname(os.path.abspath(__file__))

class Root(object):
	
	@cherrypy.expose
	def index(self):
		return '''<html>
		<head><script type="text/javascript" src="/jquery.js" ></script></head>
		<body><h1>The current time is ...</h1><div id="time"></div>
		<script type="text/javascript">
		//$.ajaxSetup({cache:false});
		//window.setInterval(function(){$("#time").load("time");},1000);
		window.setInterval(function(){$.ajax({url:"time",cache:false,success:function(data,status,request){
			$("#time").html(data);
		}});},1000);
		</script>
		</body>
		</html>'''
	
	@cherrypy.expose
	def time(self,_=None):
		return asctime()

	#Inserting Host and Port Output
	cherrypy.config.update({
                'server.socket_host': '0.0.0.0',
                'server.socket_port': 8088,
	})

cherrypy.quickstart(Root(),config={
		'/jquery.js':
		{ 'tools.staticfile.on':True,
		'tools.staticfile.filename':os.path.join(current_dir,"static","jquery","jquery-1.4.2.js")
		}
	})
