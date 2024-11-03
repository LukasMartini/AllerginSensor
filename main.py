from server.server import activate_server
from server.amqp_data_extractor import amqp_data_extractor
from server.data_outputter import data_printer

def main():
    # activate_server()
    outputter = data_printer()
    extractor = amqp_data_extractor(outputter)

    extractor.extract_data()

main()