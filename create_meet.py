import datetime
import json
from zoomus import ZoomClient
client = ZoomClient('34n5fY-dQAqLjcXZjosfyw','B7p3dhFTYrLXdwTfJipACMJxhNBYItDm0vxJ')


datetime_object = datetime.datetime.strptime('2021-03-06T05:30:00', '%Y-%m-%dT%H:%M:%S')

#print(json.loads(client.meeting.list(user_id=user_id).content))
create=(json.loads(client.meeting.create(
        user_id='swetajaiswal275@gmail.com',
        host_id='host_id',
        duration=60,
        topic='science',
        type='2',
        password='12345',
        start_time=datetime_object).content))
print("meeting id == "+str(create['id']))
print("meeting password == "+create['password'])
print("meeting topic == "+create['topic'])
print("meeting join_url == "+create['join_url'])
print("meeting start_time == "+create['start_time'])
#user_list_response = client.user.list()
#user_list = json.loads(user_list_response.content)

#for user in user_list['users']:
 #   user_id = user['id']
  #  print(user_id)
   # show=[json.loads(client.meeting.list(user_id=user_id).content)]
    #
#print(show)