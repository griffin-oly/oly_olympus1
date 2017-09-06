import active_directory

me = active_directory.AD_object ("LDAP://ou=it,dc=gb,dc=vo,dc=local")

me = active_directory.AD_object (GetObject ("LDAP://ou=it,dc=gb,dc=vo,dc=local"))

#
# Historical method
#
me = active_directory.AD_object (path="LDAP://ou=ot,dc=gb,dc=vo,dc=local")

