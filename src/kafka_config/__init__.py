
import os



# Cloud API Keys
# API_KEY = os.getenv('API_KEY',None)
# API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
# BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)

API_KEY = "W355CXVFQLRZCLGQ"
API_SECRET_KEY = "bb9cq18mJnftmEU2lE857wzPrT/LUwRm/oQP6zJZMMBSl0yxjxfLjYwW39t2w3/D"
BOOTSTRAP_SERVER = "pkc-921jm.us-east-2.aws.confluent.cloud:9092"

# Authentication Related Variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

# Schema Related Variables
ENDPOINT_SCHEMA_URL  = "https://psrc-e8157.us-east-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY = "RFEPHXCH7POAXQET"
SCHEMA_REGISTRY_API_SECRET = "yxDR9auNCzRK8E9aaxAxGMYz5YuVQ8jI854YWC8aDYb0rkVlb54z7R0iZnMojQ8A"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

