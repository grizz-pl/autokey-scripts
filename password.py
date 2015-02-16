#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autokey script - generate password  by grizz - Witek Firlej http://grizz.pl
# ver. 2015.02.16.1
# Copyright (C) 2015 Witold Firlej

#idea from http://www.pythonforbeginners.com/code-snippets-source-code/script-password-generator

#set password length 


passwordLenMin=12
passwordLenMax=16

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(passwordLenMin, passwordLenMax)))
clipboard.fill_clipboard(password) # copy to clipboard - to paste into 'repeat password' field
keyboard.send_keys(password)
