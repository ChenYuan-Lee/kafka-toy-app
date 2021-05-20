import logging

from confluent_kafka import DeserializingConsumer
from confluent_kafka.avro import SerializerError
from confluent_kafka.schema_registry.avro import AvroDeserializer

from avro_schemas.key_schema import key_schema_str
from avro_schemas.value_schema import value_schema_str
from constants import SCHEMA_REGISTRY_CLIENT, Topics, BOOTSTRAP_SERVERS
from utils import reset_to_beginning_on_assign, convert_epoch_to_datetime, reset_to_end_on_assign

consumer = DeserializingConsumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "key.deserializer": AvroDeserializer(schema_str=key_schema_str, schema_registry_client=SCHEMA_REGISTRY_CLIENT),
    "value.deserializer": AvroDeserializer(schema_str=value_schema_str, schema_registry_client=SCHEMA_REGISTRY_CLIENT),
    "group.id": "consumer",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(
    topics=[Topics.TOPIC_1.value],
    on_assign=reset_to_beginning_on_assign,
    # on_assign=reset_to_end_on_assign,
)

while True:
    try:
        msg = consumer.poll(1.0)
    except SerializerError as error:
        # Report malformed record, discard results, continue polling
        logging.error(f"Message deserialization failed. Error: {error}")
        continue
    except KeyboardInterrupt:
        break

    if msg is None:
        continue
    else:
        msg_produced_datetime = convert_epoch_to_datetime(msg.timestamp()[1])
        listing_id, = msg.key().values()
        bedrooms, laundry = msg.value().values()
        logging.warning(f"bedrooms: {bedrooms}, laundry: {laundry} (produced at: {msg_produced_datetime})")


# Leave group and commit final offsets
consumer.close()
