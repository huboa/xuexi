# -*- coding: utf-8 -*-
import importlib,sys
importlib.reload(sys)
sys.setdefaultencoding('utf-8') 
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.contrib import *
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import time,datetime,ldap,json
from django.core.mail import send_mail
import urllib
#from grant.models import *
from django.core.cache import cache
from django.db import connection,transaction
import pymysql

def login(request):

	cur = connection.cursor()
#	cur.execute("select ip from granthost")
#	hostlist = cur.fetchall()


	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			try:
				flag = "true"
				domain = "mtime"
				domain_username = domain + "\\" + username
				conn = ldap.initialize("ldap://10.10.30.206")
				conn.simple_bind_s(domain_username,password)
			except Exception as mesg:
				flag = "false"
			if flag == 'true':

				request.session['username'] = username
				#url = "http://cd-ztree-api.inc-mtime.com/getallcmdbhosts"
				#result = urllib2.urlopen(url).read()
				#hostlist = json.loads(result)

				return HttpResponseRedirect('/grant/')
			else:
				return render_to_response('login.html',{'login_error':'用户名或密码错误!'})
	else:
		return render_to_response('login.html')

# def grant(request):
# 	error = ""
# 	note = 0
# 	execresult = ""
# 	true = ""
# 	false = ""
# 	null =  ""
# 	r = ""
# 	vle = ""
#         hostlist = ""
#         #url = "http://cd-ztree-api.inc-mtime.com/getallcmdbhosts"
#         #result = urllib2.urlopen(url).read()
#         #hostlist = json.loads(result)
#         #if cache.get("hostlist") == None:
#         #
# 	#    url = "http://cd-ztree-api.inc-mtime.com/getallcmdbhosts"
# 	#    result = urllib2.urlopen(url).read()
# 	#    hostlist = json.loads(result)
#         #    cache.set("hostlist",hostlist)
#         #    hostlist = cache.get("hostlist")
#         #else:
#         #    hostlist = cache.get("hostlist")
# 	try:
# 		cur = connection.cursor()
# 	#	cur.execute("select ip from granthost")
# 	#	hostlist = cur.fetchall()
#
#
# 		if request.method == 'POST':
#
# 			username = request.session['username']
#
# 			if username is None:
# 				return render_to_response('login.html')
#
# 			osuser = request.POST.get('osuser','')
# 			ipaddr = request.POST.get('ipaddr','')
# 			dateid = request.POST.get('dateid')
# 			idc = request.POST.get('idc')
# 			remark = request.POST.get('remark')
#
# 			username = request.session['username']
#
#
# 			cursor = connection.cursor()
#
# 		#获取当前时间，写入数据库作为创建时间
# 			currenttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+3600*8))
#
# 		#检验系统登录用户、主机名、授权时长
# 			if osuser == '':
# 				return HttpResponse("系统登录账号不能为空！")
# 			if ipaddr == '':
# 				return HttpResponse("服务器主机名不能为空！")
#
# 			if dateid == '1':
# 				dateid = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*8+86400))
# 			elif dateid == '2':
# 				dateid = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*8+86400*7))
# 			elif dateid == '3':
# 				dateid = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*8+86400*30))
# 			elif dateid == '4':
# 				dateid = time.strftime('%Y-%m-%d',time.localtime(time.time()+3600*8+86400*30*3))
# 			else:
# 				message = "请选择授权时长！"
# 				return render_to_response('grant.html',{'error':message})
#
#
#
# 			if ipaddr and osuser != 'rd' :
#
# 				sql = "select ID, count(1) cnt from (select ID from fortress where UserName='%s' and OsUser='%s' and IPAddr='%s' and IDC='lfzb' ) a " % (username,osuser,ipaddr)
# 				cursor.execute(sql)
# 				result = cursor.fetchone()
# 				if result[1] > 0:
# 					u_sql = "update fortress set DeadLineTime ='%s' where ID='%s' " % (dateid,result[0])
# 					cursor.execute(u_sql)
# 				else:
# 					idc = 'lfzb'
# 					print idc
# 					cursor.execute("insert into fortress(UserName,OsUser,IPAddr,DeadLineTime,IDC,Remark,CreateTime) values (%s,%s,%s,%s,%s,%s,%s)",[username,osuser,ipaddr,dateid,idc,remark,currenttime])
#
# 				subject = "廊坊总部--线上服务器账户申请"
# 				content = "廊坊总部--线上服务器账户信息：" + "\n" + "\n" + "申请人：" + username +  "\n" + "系统登录帐号：" + osuser + "\n" + "服务器主机名：" + ipaddr + "\n" + "授权日期截止到：" + dateid + "\n" + "申请理由：" + remark + "\n" + "请细请点击：" + "\n" + "http://192.168.51.182:8085/query/"
# 				send_mail(subject,content,'monitor@service.mtime.com', ['itteam@mtime.com'],fail_silently=True)
# 				return HttpResponse("申请已提交成功，等待运维人员审核！")
#
# 		#若申请rd账户，自动授权
# 			if ipaddr and osuser in ['rd']:
# 				idc = 'lfzb'
# 				url = "http://lf-zb-rundeck.wandafilm.com/api/13/job/8e321d00-e790-48a3-b5a2-9e2221d6e82c/run?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG&argString=-APP_USER+'%s'+-SERVER_USER+'%s'+-SERVER_IP+'%s'+-D_DATE+'%s'" % (username,osuser,ipaddr,dateid)
#
# 				urlresult = urllib2.urlopen(url).read()
# 				time.sleep(3)
# 				idx1 = urlresult.index('id=')
# 				idx2 = urlresult.index('href')
# 				execid = urlresult[idx1+4:idx2-2]
# 				execresult = "http://lf-zb-rundeck.wandafilm.com/api/10/execution/%d/state?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG" % int(execid)
#
# 				for i in range(60):
# 					urlresult2 = urllib2.urlopen(execresult).read()
# 					time.sleep(1)
# 					r = eval(urlresult2)
# 					for k,v in r.items():
# 						if k == "executionState":
# 							if v == 'FAILED':
# 								u_sql = "update fortress set Status = 9,ExecID = '%s' where UserName = '%s' and OsUser = '%s' and IPAddr = '%s' and DeadLineTime = '%s'" % (execid,username,osuser,ipaddr,dateid)
# 								cursor.execute(u_sql)
# 								vle = v
# 								break
# 							elif v == 'SUCCEEDED':
# 								u_sql = "update fortress set Status = 1,ExecID = '%s' where UserName = '%s' and OsUser = '%s' and IPAddr = '%s' and DeadLineTime = '%s'" % (execid,username,osuser,ipaddr,dateid)
# 								cursor.execute(u_sql)
# 								vle = v
# 								break
# 							else:
# 								vle = 'RUNNING'
# 						else:
# 							continue
# 					time.sleep(1)
# 					if vle == 'RUNNING':
# 						continue
# 					else:
# 						break
#
# 			else:
# 				return HttpResponse("申请已提交，请等待审批！")
#
#
# 		#判断如果库中有值，则进行update,若是新记录，则进行insert
# 			cursor = connection.cursor()
# 			sql = "select ID, count(1) cnt from (select ID from fortress where UserName='%s' and OsUser='%s' and IPAddr='%s' and IDC='lfzb' ) a " % (username,osuser,ipaddr)
# 			cursor.execute(sql)
# 			result = cursor.fetchone()
# 			if result[1] > 0:
# 				u_sql = "update fortress set DeadLineTime ='%s' where ID='%s' " % (dateid,result[0])
# 				cursor.execute(u_sql)
# 				note = 1
# 			else:
# 			    if vle == 'SUCCEEDED':
# 				Status = '1'
# 				cursor.execute("insert into fortress(UserName,OsUser,IPAddr,DeadLineTime,IDC,Remark,ExecID,CreateTime,Status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",[username,osuser,ipaddr,dateid,idc,remark,execid,currenttime,Status])
# 				note = 1
# 			    else:
# 				Status = '9'
# 				cursor.execute("insert into fortress(UserName,OsUser,IPAddr,DeadLineTime,IDC,Remark,ExecID,CreateTime,Status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",[username,osuser,ipaddr,dateid,idc,remark,execid,currenttime,Status])
# 				note = 1
# 		else:
# 			#验证是否登录，如果未登录，则自动跳转到login.html页面
# 			try:
# 				username = request.session['username']
# 			except Exception, e:
# 				return render_to_response('login.html')
#
# 	except Exception, e:
# 		error = str(e)
#         return render_to_response('grant.html',{'error':error,'note':note,'hostlist':hostlist})
#
#
#
#
# def wait(request):
#         error = ""
#         try:
#                 try:
#                         username = request.session['username']
#                 except Exception, e:
#                         return render_to_response('login.html')
#
#                 sql = "select UserName,OsUser,IPAddr, DeadLineTime,ID,Status,ExecID,Remark,IDC,CreateTime from fortress where Status = 0 and IDC='lfzb' order by ID desc"
#                 cursor = connection.cursor()
#                 cursor.execute(sql)
#                 result = cursor.fetchall()
#         except Exception, e:
#                 error = str(e)
#         return render_to_response('wait.html',{'error':error,'result':result},context_instance=RequestContext(request))
#
#
#
#


def query(request):
	error = ""
	o_result = ""
	o_sql = ""
	result = ""
	true = false = null = ""
	r = vle = sql = ""
	jxpasswdsql = dbpasswdsql = dbprepasswdsql = ""
	try:
		#验证是否登录，如果未登录，则自动跳转到login.html页面
		try:
			username = request.session['username']
		except Exception, e:
			return render_to_response('login.html')


		o_id = request.POST.get('o_id')
		r_id = request.POST.get('r_id')
		cursor = connection.cursor()

		if o_id:
		    if username in settings.ALL_OPS: 
			print username
			o_sql = "select UserName,OsUser,IPAddr, DeadLineTime,ID,IDC from fortress where ID = %d and IDC='lfzb' " % int(o_id)
			cursor.execute(o_sql)
			o_result = cursor.fetchone()
			

			url = "http://lf-zb-rundeck.wandafilm.com/api/13/job/8e321d00-e790-48a3-b5a2-9e2221d6e82c/run?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG&argString=-APP_USER+'%s'+-SERVER_USER+'%s'+-SERVER_IP+'%s'+-D_DATE+'%s'" % (o_result[0],o_result[1],o_result[2],o_result[3])
			
		#	return HttpResponse(url)

			urlresult = urllib2.urlopen(url).read()
			time.sleep(3)

			idx1 = urlresult.index('id=')
			idx2 = urlresult.index('href')
			execid = urlresult[idx1+4:idx2-2]
	
			execresult = "http://lf-zb-rundeck.wandafilm.com/api/10/execution/%d/state?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG" % int(execid)
		

			for i in range(60):
				urlresult2 = urllib2.urlopen(execresult).read()
				time.sleep(1)
				r = eval(urlresult2)
				for k,v in r.items():
					if k == "executionState":
						if v == 'FAILED':
							u_sql = "update fortress set Status = 9,ExecID = '%s' where ID = %d" % (execid,int(o_id))
							cursor.execute(u_sql)
							vle = v
							break
						elif v == 'SUCCEEDED':
							u_sql = "update fortress set Status = 1,ExecID = '%s' where ID = %d" % (execid,int(o_id))
							cursor.execute(u_sql)
							vle = v
							break
						else:
							vle = 'RUNNING'
				time.sleep(1)
				if vle == 'RUNNING':
					continue
				else:
					break

		    else:
			return HttpResponse("对不起，您无权限操作！请联系运维人员")
			





					

		if r_id:
		    if username in settings.ALL_OPS: 
			r_sql = "update fortress set Status = 2 where ID = %d" % int(r_id)
			cursor.execute(r_sql)
		    else:
			return HttpResponse("对不起，您无权限操作！")

	#显示隐藏密码
		jxpasswd = request.POST.get('jxpasswd')

		if jxpasswd:
			try:

				url = "http://cd-ztree-api.inc-mtime.com/getalluserpassword"
				result = urllib2.urlopen(url).read()
				result = json.loads(result)

				for i in result:
					for k,v in i.items():
						if k == username:
							jxpasswdsql = v


			except Exception, e:
				error = "对不起，您还未申请成都机房服务器！"

		if username not in settings.ALL_OPS:
			sql="select UserName,OsUser,IPAddr,DeadLineTime,ID,Status,ExecID,Remark,IDC,CreateTime  from fortress where UserName = '%s' and IDC='lfzb' order by ID desc" % (username)
		else:

			sql = "select UserName,OsUser,IPAddr, DeadLineTime,ID,Status,ExecID,Remark,IDC,CreateTime from fortress where IDC='lfzb' order by ID desc"
		cursor = connection.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
	except Exception, e:
		error = str(e)
	return render_to_response('query.html',{'error':error,'result':result,'sql':sql,'jxpasswdsql':jxpasswdsql},context_instance=RequestContext(request))

#显示流程图
def flow(request):
	image_data = open("/home/mtime/fortress_cd/grant/static/images/flow.jpg", "rb").read()  
	return HttpResponse(image_data, mimetype="image/png") 
