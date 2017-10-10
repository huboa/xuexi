#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from pyzabbix import ZabbixAPI
server_name_in_zabbix = 'my server'
hostid =   # This is what host you want to add the scenarios
applicationid =    # This is what application you want to add
retries = 1
delay = 10
status = 200
the_string_required = 'Copyright'
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8'
def auth():
    zapi = ZabbixAPI("http://zabbix url")
    zapi.login("my username", "my secret")
    return zapi
def get_host_name(login_zabbix):
    host_dict = login_zabbix.host.get(filter={"name": server_name_in_zabbix})[0]
    host_name = host_dict.get('host')
    return host_name
def get_host_id(login_zabbix):
    host_dict = login_zabbix.host.get(filter={"name":server_name_in_zabbix})[0]
    hostid = host_dict.get("hostid")
    return hostid
def get_url(login_zabbix, host_name):
    with open('your file') as f:
        for url in f:
            monitor_url = url
            name = monitor_url.split('//')[-1].split('\n')[0]
            create_web_scenarios(login_zabbix, host_name, monitor_url=monitor_url, name=name)
def create_web_scenarios(login_zabbix, host_name, monitor_url, name):
    request = login_zabbix.httptest.get(filter={"name": name})
    if request:
        print ('"{}" is exist'.format(name))
        create_trigger(login_zabbix, host_name, name)
    else:
        login_zabbix.httptest.create({
            "name": name,
            "agent": agent,
            "hostid": hostid,
            "applicationid": applicationid,
            "delay": delay,
            "retries": retries,
            "steps": [{
                'name': name+' index',
                'url': monitor_url,
                'required': the_string_required,
                'status_codes': status,
                'no': '1'}]
        })
        create_trigger(login_zabbix, host_name, name)
def create_trigger(login_zabbix, host_name, name):
    login_zabbix.trigger.create({
        "description": "{} http code got an exception".format(name),
        "expression": "{%s:web.test.rspcode[%s,%s index].last()}>400" % (host_name, name, name),
        "priority": "2"
    })
    login_zabbix.trigger.create({
        "description": "{} response slow now".format(name),
        "expression": "{%s:web.test.time[%s,%s index,resp].count(2m,10,"gt")}>5" % (host_name, name, name),
        "priority": "2"
    })
    login_zabbix.trigger.create({
        "description": "{} seems error".format(name),
        "expression": "{%s:web.test.error[%s].str(required pattern,3)}=1" % (host_name, name),
        "priority": "2"
    })
def main():
    login_zabbix = auth()
    host_name = get_host_name(login_zabbix)
    # host_id = get_host_id(login_zabbix)
    get_url(login_zabbix, host_name)
    print ("Everything is done,please check on your zabbix server")
if __name__ == '__main__':
    main()