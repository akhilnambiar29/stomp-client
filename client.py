import random
import time

import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)


count = 0


def get_random_data():
    sample = random.sample(range(-100, 100), 9)
    a = ','.join(str(s) for s in sample)
    return '01,' + a


conn = stomp.Connection12(
    host_and_ports=[('b-f1caac15-cb49-4d06-b87c-22f983f0da7c-1.mq.eu-west-1.amazonaws.com', 61614)], use_ssl=True)
conn.set_listener('', MyListener())
conn.connect('raceleap', 'racingandleaping', wait=True, headers={'client-id': 'subscribedToAkhil'})
# print(conn.get_ssl(host_and_port=[('b-f1caac15-cb49-4d06-b87c-22f983f0da7c-1.mq.eu-west-1.amazonaws.com', 61614)]))
# conn.connect('/gs-guide-websocket')
while True:
    conn.send(body=get_random_data(), destination='/topic/racequeue')
    time.sleep(1)
conn.disconnect()
