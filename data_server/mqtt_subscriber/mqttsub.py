import paho.mqtt.client as paho
import datetime
import pytz
import math
import logging
from django.conf import settings

logger = logging.getLogger(__name__)
 

class MQTTDemuxClient:

    def on_connect(self, client, userdata, flags, rc):
        logger.info('Successfully connected to MQTT broker!')
        client.subscribe('shine/+/+/+/#', 2)
        logger.info('On_connect: Subscribing to shine/data/+/+/#')
 
    def on_message(self, client, userdata, msg):
 
        messagebyte = bytearray(msg.payload)
        print( "On message. Received topic %s with qos %s." % (msg.topic, str(msg.qos)) )
        topic = msg.topic.split('/')
        
        if topic[1] == 'data' and len(topic) >= 4:
            print("Pass packet to data module")
            if topic[2] == 'aggregate':
                self.parse_aggregate_pkt(topic[3], messagebyte)
            elif topic[2] == 'sensor':
                self.parse_sensor_pkt(topic[3], messagebyte)
        elif topic[1] == 'statistics' and len(topic) == 5:
            self.parse_statistics_pkt(topic[2], topic[4], messagebyte.decode('utf-8'))
 
    def on_publish(self, client, userdata, mid):
        logger.debug('On publishing mib: %s ' % (str(mid))) 
    
    def on_subscribe(self, client, userdata, mid, granted_qos):
        logger.debug('On Subscribed, mib: %s with qos: %s' % (str(mid), granted_qos))
 
    def bits(self, n):
        shift_bit = 0

        while n > (1<<shift_bit):
            result = n & (1<<shift_bit)
            if result:
                yield shift_bit
            n ^= (1<<shift_bit)
            shift_bit+=1

    def parse_aggregate_pkt(self, nodeid, topic, message):
        print("Parsing aggregate packet");
        gw_timestamp, sensor_timestamp, confVer, bitMap, length = struct.unpack('<IIHBB', message[:12])
        sys_tz = pytz.timezone(settings.TIME_ZONE)
        RXTimestamp = datetime.datetime.fromtimestamp(gw_timestamp, tz=sys_tz)
        print("\nGateway Received Timestamp in seconds: %d Date %s" % (gw_timestamp, str(RXTimestamp)))	
        print("configVer is %d" % confVer)
        print("bitMap %d" % bitMap)
        print("Bitmap in binary %s" % bin(bitMap))
        print("length %d" % length)
        lenData = len(message[12:])
        print("\nRemaining Data Length :%d" %lenData)
        #result = TYPE_MAPPING[confSeq](self, int(nodeid), timestamp, seqno, timestamp, bitMap, message[15:])
        

    def parse_sensor_pkt(self, nodeid, topic, message):
        print("Parsing sensor packet");
        print("/******* END PACKET PARSING******/\n\n")


    def parse_statistics_pkt(self, nodeid, type, message):
        pass

    def __init__(self):
        self.mqttc = paho.Client("shine_demux_sub_pub", clean_session=True, userdata=None, protocol=paho.MQTTv311)
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.connect(settings.EXT_BROKER_URL, settings.EXT_BROKER_PORT, settings.EXT_BROKER_TIMEOUT)
        self.mqttc.loop_forever()
