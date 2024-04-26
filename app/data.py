from os import getenv

from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from dotenv import load_dotenv
from certifi import where


class Database:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection="Monsters"):
        self.collection = self.database.get_collection(collection)

    def seed(self, amount=1000) -> bool:
        # correctly inserts the specified number of documents into the collection.
        records = [Monster().to_dict() for i in range(amount)]
        return self.collection.insert_many(records).acknowledged

    def reset(self) -> bool:
        # correctly deletes all documents from the collection.
        return self.collection.delete_many({}).acknowledged

    def count(self) -> int:                 
        # correctly returns the number of documents in the collection.
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # correctly returns a DataFrame containing all documents in the collection.
        return DataFrame(list(self.collection.find({}, {"_id": False})))

    def html_table(self) -> str:
        #correctly returns an HTML table representation of the DataFrame, or None if the collection is empty.
        count = self.count()
        if count > 0:
            return self.dataframe().to_html()
        else:
            return "None"

if __name__ == '__main__':
    db = Database()
    db.count()
    print("collections created:", db.count())