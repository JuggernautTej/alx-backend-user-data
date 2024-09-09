#!/usr/bin/env python3
"""
Main file
"""

import os
from db import DB
from user import User

db_file = 'a.db'

if os.path.exists(db_file):
    os.remove(db_file)
my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)