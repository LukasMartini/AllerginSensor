import sarracenia.moth
import sarracenia.moth.amqp
import sarracenia.credentials

import urllib.request
import xml.etree.ElementTree

# Setup sarracenia settings
options = sarracenia.moth.default_options

options.update(sarracenia.moth.amqp.default_options)

options['broker'] = sarracenia.credentials.Credential('amqps://anonymous:anonymous@dd.weather.gc.ca')
options['topicPrefix'] = ['v02', 'post']
options['bindings'] = [('xpublic', ['v02', 'post'], ['air_quality', 'aqhi', '#']  )]
options['queueName'] = 'q_anonymous_aqsamqpreader_devqueue'
options['batch'] = 1

print('options: %s' % options)  

moth = sarracenia.moth.Moth.subFactory(options)

while True:
    incoming_messages = moth.newMessages()
    for message in incoming_messages:
        print(incoming_messages)

# Example data:
# [{'_format': 'v02', '_deleteOnPost': {'exchange', 'local_offset', 'subtopic', 'ack_id', '_format', 'topic'}, 
# 'sundew_extension': 'encodeobs:CMC:AQHI:XML::20241030214445', 'from_cluster': 'DDSR.CMC', 'to_clusters': 'ALL', 
# 'filename': 'msg_ddsr-WXO-DD_02816d1e3e7d0bb141f3df6b0da2b181:encodeobs:CMC:AQHI:XML::20241030214445', 
# 'source': 'WXO-DD', 'mtime': '20241030T214446.560', 'atime': '20241030T214446.560', 'pubTime': '20241030T214446.560', 
# 'baseUrl': 'https://dd5.weather.gc.ca', 'relPath': '/air_quality/aqhi/atl/observation/realtime/xml/AQ_OBS_DAFMJ_202410302100.xml', 
# 'subtopic': ['air_quality', 'aqhi', 'atl', 'observation', 'realtime', 'xml'], 'identity': {'method': 'md5', 'value': 'QAZpqiOG8w1knmarONlPTQ=='}, 
# 'size': 705, 'exchange': 'xpublic', 'topic': 'v02.post.air_quality.aqhi.atl.observation.realtime.xml', 'ack_id': {'delivery_tag': 1, 'channel_id': 2, 
# 'connection_id': '467b7399-7e4b-4b6b-b951-117fcbf172de_sub', 'broker': 'dd.weather.gc.ca:5671//'}, 'local_offset': 0}]