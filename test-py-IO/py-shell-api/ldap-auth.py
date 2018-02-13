
import ldap
ldapServer = 'LDAP://localhost'
domain = 'mtime'
userName = 'shengchong.zhao'
domainUserName = domain + '\\' + userName
password = 'DoNotUseMe'
try:
    conn = ldap.initialize(ldapServer)
    conn.simple_bind_s(domainUserName, password)
    # 认证通过
except:
    pass
    # 认证失败。找原因

'''

#
# import ldap3
# import configparser
# conn = ldap3.get_config_parameter("ldap://10.10.30.206")
# print(type(conn))

# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, ALL, SUBTREE, ServerPool,

LDAP_SERVER_POOL = ["10.10.30.206", ]
LDAP_SERVER_PORT = 389
ADMIN_DN = "mtime\\shengchong.zhao"
ADMIN_PASSWORD = "zscxxcr1-2018"
SEARCH_BASE = "ou=xxx,dc=xxx,dc=xxx"

ldap_server_pool = ServerPool(LDAP_SERVER_POOL)
conn = Connection(ldap_server_pool)
print(conn)
print(conn.open())
conn.bind()


def ldap_auth(username, password):
    ldap_server_pool = ServerPool(LDAP_SERVER_POOL)
    conn = Connection(ldap_server_pool, user=ADMIN_DN, password=ADMIN_PASSWORD, check_names=True, lazy=False, raise_exceptions=False)
    conn.open()
    conn.bind()

    res = conn.search(
        search_base = SEARCH_BASE,
        search_filter = '(sAMAccountName={})'.format(username),
        search_scope = SUBTREE,
        attributes = ['cn', 'givenName', 'mail', 'sAMAccountName'],
        paged_size = 5
    )

    if res:
        entry = conn.response[0]
        dn = entry['dn']
        attr_dict = entry['attributes']

        # check password by dn
        try:
            conn2 = Connection(ldap_server_pool, user=dn, password=password, check_names=True, lazy=False, raise_exceptions=False)
            conn2.bind()
            if conn2.result["description"] == "success":
                print((True, attr_dict["mail"], attr_dict["sAMAccountName"], attr_dict["givenName"]))
                return (True, attr_dict["mail"], attr_dict["sAMAccountName"], attr_dict["givenName"])
            else:
                print("auth fail")
                return (False, None, None, None)
        except Exception as e:
            print("auth fail")
            return (False, None, None, None)
    else:
        return (False, None, None, None)


if __name__ == "__main__":
    ldap_auth("shengchong.zhao", "admin2018")


'''
