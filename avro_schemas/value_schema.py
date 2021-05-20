value_schema_str = """
{
    "name": "SCHEMA_VALUE",
    "type": "record",
    "fields" : [
        {
            "name" : "bedrooms",
            "type" : "float"
        },
        {
            "name": "laundry",
            "type": {
                "type": "enum",
                "name": "laundry",
                "symbols": ["IN_UNIT", "IN_PROPERTY"]
            }
        }
   ]
}
"""
