from distutils.core import setup
import py2exe

setup(
	console=['app.py'],
	options={"py2exe":{
		"includes":["binio", "flask", "urllib", "socket", "jinja2.ext"],
		"excludes":["email.message"],
		"optimize":2,
		#"bundle_files":1,
		"compressed":True,
		"xref":True
		}
	}
)