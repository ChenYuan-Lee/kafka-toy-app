from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import topic_record_subject_name_strategy
from confluent_kafka.schema_registry.avro import AvroSerializer

from avro_schemas.key_schema import key_schema_str
from avro_schemas.value_schema import value_schema_str
from constants import Topics, BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_CLIENT
from utils import get_partition, on_delivery

avro_serializer_config = {
    "auto.register.schemas": True,
    "subject.name.strategy": topic_record_subject_name_strategy,
}
key_serializer = AvroSerializer(
    schema_str=key_schema_str,
    schema_registry_client=SCHEMA_REGISTRY_CLIENT,
    conf=avro_serializer_config,
)
value_serializer = AvroSerializer(
    schema_str=value_schema_str,
    schema_registry_client=SCHEMA_REGISTRY_CLIENT,
    conf=avro_serializer_config,
)
producer_config = {
    "key.serializer": key_serializer,
    "value.serializer": value_serializer,
    # 'transaction.timeout.ms': 60000,
    # 'enable.idempotence': True,
    # 'debug': "all"
    "bootstrap.servers": BOOTSTRAP_SERVERS
}
producer = SerializingProducer(producer_config)
msg_key = {
    "listing_id": 1,
}
msg_value = {
    "bedrooms": 1.5,
    "laundry": "IN_UNIT",
}

producer.produce(
    topic=Topics.TOPIC_1.value,
    key=msg_key,
    value=msg_value,
    partition=get_partition(msg_key["listing_id"]),
    on_delivery=on_delivery,
)
producer.flush()
