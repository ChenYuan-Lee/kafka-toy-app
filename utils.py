import logging
from datetime import datetime
from pprint import pprint

from constants import NUM_PARTITIONS, SCHEMA_REGISTRY_CLIENT, ADMIN_CLIENT


def get_partition(listing_id: int) -> int:
    return (listing_id - 1) % NUM_PARTITIONS


def on_delivery(err, msg):
    if err is not None:
        logging.warning(f"Failed to deliver message: {err}")
    if msg is not None:
        logging.warning(f"Successfully produced msg (Key: {msg.key()}, Value: {msg.value()})")


def reset_to_beginning_on_assign(consumer, partitions):
    for partition in partitions:
        # -2 is the internal value for beginning
        # Do not seek to 0 because it might have been log compacted away
        partition.offset = -2
    consumer.assign(partitions)


def reset_to_end_on_assign(consumer, partitions):
    for partition in partitions:
        # -1 is the internal value for the end
        partition.offset = -1
    consumer.assign(partitions)


def show_subjects_with_versions():
    subjects = SCHEMA_REGISTRY_CLIENT.get_subjects()
    for subject in subjects:
        versions = SCHEMA_REGISTRY_CLIENT.get_versions(subject)
        print(f"Subject: {subject} | Version(s): {versions}")


def convert_epoch_to_datetime(milliseconds: int) -> datetime:
    return datetime.fromtimestamp(milliseconds / 1000)


def display_topics():
    pprint(ADMIN_CLIENT.list_topics().topics)
