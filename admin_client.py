from confluent_kafka.admin import AdminClient, NewTopic

from constants import Topics, BOOTSTRAP_SERVERS, NUM_PARTITIONS

a = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})

new_topics = [NewTopic(topic, num_partitions=NUM_PARTITIONS, replication_factor=1) for topic in [Topics.TOPIC_1, Topics.TOPIC_2]]
# Note: In a multi-cluster production scenario, it is more typical to use a replication_factor of 3 for durability.

# Call create_topics to asynchronously create topics. A dict
# of <topic,future> is returned.
fs = a.create_topics(new_topics)

# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
