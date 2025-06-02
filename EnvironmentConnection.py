import yaml
from TM1py.Services import TM1Service

# Get Environment Connection Details from Config.yaml file
def get_environment_connection(environment_type, environment_number):
    with open('Config.yaml', 'r') as file:
        tm1_connection_details = yaml.safe_load(file)
        return tm1_connection_details[environment_type][environment_number]

# Connect to TM1 instance
def connect_to_TM1(environment_type, environment_number):
    tm1_connection_details = get_environment_connection(environment_type, environment_number)
    print(tm1_connection_details)
    tm1 = TM1Service(**tm1_connection_details)
    print("Connection Success to " + tm1.get_server_name())
    return 

# Testing
connect_to_TM1('LocalEnvironment', 'Environment1')