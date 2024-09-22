from populate_edi855_data import get_database

class TrainingData:

    def training_data(self):
        edi855_json_db = get_database("edi855_edi_json_data")
        timestamp_collection = edi855_json_db["timestamp"]
        timestamps = timestamp_collection.find().sort({"timestamp":-1})
        print(timestamps)
        for timestamp in timestamps:
            latest = True
            if latest:
                data = edi855_json_db["edi855_edi_json_data"].find({"timestamp" : timestamp.get("timestamp")})
                return data
            latest = False
        return []


