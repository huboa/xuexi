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