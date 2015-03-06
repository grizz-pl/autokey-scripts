#autokey script - Todoist - quick add  by grizz - Witek Firlej http://grizz.pl
# ver. 2015.02.16.1
# Copyright (C) 2015 Witold Firlej

retCode, task = dialog.input_dialog("Todoist - quick add", "Add task to inbox")

import urllib2, urllib

from os.path import expanduser

home = expanduser("~")

f = open(home + "/.autokey-tds-tkn")
token = f.readline()

finalTask = urllib.quote_plus(task)

baseURL = "https://api.todoist.com/API/addItem?content=" + finalTask + "&priority=1&token=" + token

try:
    reader_req = urllib2.Request(baseURL)
    reader_resp = urllib2.urlopen(reader_req)
    reader_resp_content = reader_resp.read()

    decoded = reader_resp_content.decode('utf-8')
except:
    dialog.info_dialog("Todoist - quick add", "Something wrong with url")

if task not in decoded:
    dialog.info_dialog("Todoist - quick add", "Not added")
else:
    pass  # dialog.info_dialog("Todoist - quick add","oki")



