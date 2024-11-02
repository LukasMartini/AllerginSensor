from server.server import activate_server
from server.amqp_data_extractor import amqp_data_extractor

def main():
    activate_server()
    amqp_data_extractor()