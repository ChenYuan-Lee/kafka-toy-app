from enum import Enum

from confluent_kafka.admin import AdminClient
from confluent_kafka.schema_registry import SchemaRegistryClient


class Topics(Enum):
    TOPIC_1 = "topic1"
    TOPIC_2 = "topic2"


SCHEMA_REGISTRY_URL = "http://127.0.0.1:8081"
SCHEMA_REGISTRY_CLIENT = SchemaRegistryClient({'url': SCHEMA_REGISTRY_URL})
BOOTSTRAP_SERVERS = "127.0.0.1:9092"
NUM_PARTITIONS = 3
ADMIN_CLIENT = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})
