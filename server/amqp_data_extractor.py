import sarracenia.moth
import sarracenia.moth.amqp
import sarracenia.credentials

import urllib.request
import xml.etree.ElementTree

import server.data_outputter as data_outputter

# TODO: set up data extractor to have the queue running all the time, with a polling option to allow other parts of the program to know if there have been any updates.

class amqp_data_extractor:

    def __init__(self, outputter: data_outputter):
        self.outputter = outputter
        self.region_en = ''
        self.region_fr = ''
        self.utc_stamp = ''
        self.air_quality_health_index = ''
        self.special_notes = ''

    # The main program loop. Runs continuously, pulling data from the Government datamart.
    # Once data has been received, it notifies the observing data_outputter class to output the data according to its implementation of data_outputter.output().
    def extract_data(self):
        options = sarracenia.moth.default_options

        options.update(sarracenia.moth.amqp.default_options)

        options['broker'] = sarracenia.credentials.Credential('amqps://anonymous:anonymous@dd.weather.gc.ca')
        options['topicPrefix'] = ['v02', 'post']
        options['bindings'] = [('xpublic', ['v02', 'post'], ['air_quality', 'aqhi', 'ont', 'observation', 'realtime', 'xml', '#']  )]
        options['queueName'] = 'q_anonymous_aqsamqpreader_devqueue'
        options['batch'] = 1

        print('options: %s' % options)  

        moth = sarracenia.moth.Moth.subFactory(options)

        while True:
            incoming_messages = moth.newMessages()
            for message in incoming_messages:
                url = message['baseUrl']
                if 'retPath' in message:
                    url += message['retPath']
                else:
                    url += message['relPath']
                
                with urllib.request.urlopen(url) as posted_file:
                    # Attepmt to get string data from URL. If this fails, skip the file. TODO: figure out why this fails.
                    try:
                        xml_data = posted_file.read().decode('utf-8') 
                    except UnicodeDecodeError:
                        print(url)
                        continue

                    # Attempt to parse the data. If it fails, skip the file.
                    try:
                        xml_data = xml.etree.ElementTree.fromstring(xml_data)
                    except xml.etree.ElementTree.ParseError:
                        posted_file.close()
                        continue

                    for element in xml_data.iter('*'):
                        if element.tag == 'region':
                            self.region_en = element.attrib.get('nameEn')
                            self.region_fr = element.attrib.get('nameFr')
                        elif element.tag == 'UTCStamp' and element.text is not None:
                            self.utc_stamp = element.text
                        elif element.tag == 'airQualityHealthIndex' and element.text is not None:
                            self.air_quality_health_index = element.text
                        elif element.tag == 'specialNotes' and element.text is not None:
                            self.special_notes = element.text 
                    
                    data = (self.region_en, self.region_fr, self.utc_stamp, self.air_quality_health_index, self.special_notes)
                    self.outputter.output(data)

            moth.ack(incoming_messages)

        moth.cleanup()
        moth.close()

# Example data:
# [{'_format': 'v02', '_deleteOnPost': {'exchange', 'local_offset', 'subtopic', 'ack_id', '_format', 'topic'}, 
# 'sundew_extension': 'encodeobs:CMC:AQHI:XML::20241030214445', 'from_cluster': 'DDSR.CMC', 'to_clusters': 'ALL', 
# 'filename': 'msg_ddsr-WXO-DD_02816d1e3e7d0bb141f3df6b0da2b181:encodeobs:CMC:AQHI:XML::20241030214445', 
# 'source': 'WXO-DD', 'mtime': '20241030T214446.560', 'atime': '20241030T214446.560', 'pubTime': '20241030T214446.560', 
# 'baseUrl': 'https://dd5.weather.gc.ca', 'relPath': '/air_quality/aqhi/atl/observation/realtime/xml/AQ_OBS_DAFMJ_202410302100.xml', 
# 'subtopic': ['air_quality', 'aqhi', 'atl', 'observation', 'realtime', 'xml'], 'identity': {'method': 'md5', 'value': 'QAZpqiOG8w1knmarONlPTQ=='}, 
# 'size': 705, 'exchange': 'xpublic', 'topic': 'v02.post.air_quality.aqhi.atl.observation.realtime.xml', 'ack_id': {'delivery_tag': 1, 'channel_id': 2, 
# 'connection_id': '467b7399-7e4b-4b6b-b951-117fcbf172de_sub', 'broker': 'dd.weather.gc.ca:5671//'}, 'local_offset': 0}]