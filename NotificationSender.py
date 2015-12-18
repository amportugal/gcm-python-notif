from gcm import GCM
import web
import requests
import json
import httplib

API_KEY="AIzaSyA1JXqIK9EBwPEADyXQtMoMbb5ruFGUMMI"

sample_reg_id='APA91bFtxXJsZXTG8yHBmjW__PbXJ8NXClnr3p7ioUbR9M2IO1irQWhF30MF94-VBW4ixd4JABl6_mj-4XOvfkSYPupXyL25WIje3V7T7L7lHBeHZRmBYvuLGHLu5wOZy3X3Au8Qs7Z_'

paths = (
    '/sendEventUpdateNotification', 'EventUpdate',
    '/sendEventCreateNotification', 'EventCreate',
    '/sendEventJoinNotification', 'EventJoin',
    '/sendEventDeletionNotification', 'EventDelete',
)

app = web.application(paths, globals())

class EventUpdate:

    def GET(self):

        #Get json message
        json_msg_decoded=json.loads(web.data())
	json_msg_decoded['results'][0]['id']=json_msg_decoded['event_id']

        gcm = GCM(API_KEY)

        data = {'event_id' : json_msg_decoded['event_id'],
                'type_of_notify' : 'update',
                'event': json_msg_decoded['results'][0]
                }

        print "NOTIFICATION:" + json.dumps(data)

        # JSON request
        reg_ids = json_msg_decoded['reg_ids']

        if reg_ids != []:
            response = gcm.json_request(registration_ids=reg_ids, data=data)
            return response
        else:
            return httplib.OK





class EventCreate:
    def GET(self):

        #Get json message
        json_msg_decoded=json.loads(web.data())
	json_msg_decoded['results'][0]['id']=json_msg_decoded['event_id']

        gcm = GCM(API_KEY)

        data = {'event_id' : json_msg_decoded['event_id'],
                'type_of_notify' : 'create',
                'event': json_msg_decoded['results'][0]
                }


        # JSON request
        reg_ids = json_msg_decoded['reg_ids']


        print data
        print reg_ids

        if reg_ids != []:
            response = gcm.json_request(registration_ids=reg_ids, data=data)
            return response
        else:
            return httplib.OK

class EventJoin:
    def GET(self):

        #Get json message
        json_msg_decoded=json.loads(web.data())
	json_msg_decoded['results'][0]['id']=json_msg_decoded['event_id']

        gcm = GCM(API_KEY)

        data = {'event_id' : json_msg_decoded['event_id'],
                'type_of_notify' : 'join',
                'event': json_msg_decoded['results'][0],
                 'user' : json_msg_decoded['new_user']}

        print data

        # JSON request
        reg_ids = json_msg_decoded['reg_ids']

        print reg_ids

        if reg_ids != []:
            response = gcm.json_request(registration_ids=reg_ids, data=data)
            return response
        else:
            return httplib.OK

class EventDelete:
    def GET(self):
        #Get json message
        json_msg_decoded=json.loads(web.data())
	json_msg_decoded['results'][0]['id']=json_msg_decoded['event_id']

        gcm = GCM(API_KEY)

        data = {'event_id' : json_msg_decoded['event_id'],
                'type_of_notify' : 'delete',
                'event': json_msg_decoded['results'][0]}

        print json.dumps(data)

        # JSON request
        reg_ids = json_msg_decoded['reg_ids']

	print reg_ids

        if reg_ids != []:
            response = gcm.json_request(registration_ids=reg_ids, data=data)
            return response
        else:
            return httplib.OK


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(paths, globals())
    app.run(port=8080)

#requests.get("localhost:8080/sendEventUpdateNotification")



#gcm = GCM(API_KEY)
#data = {'param1': 'value1', 'param2': 'value2'}

# Plaintext request
#reg_id = '12'
#gcm.plaintext_request(registration_id=reg_id, data=data)

# JSON request
#reg_ids = ['12', '34', '69']
#response = gcm.json_request(registration_ids=reg_ids, data=data)

# Extra arguments
#res = gcm.json_request(
#    registration_ids=reg_ids, data=data,
#    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
#)
