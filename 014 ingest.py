import pyspark
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession

class Ingest:

    def __init__(self,spark):
        self.spark=spark

    def ingest_data(self):
        print("Ingesting 123")
        my_list = [1, 2, 3]
        df = self.spark.createDataFrame(my_list, IntegerType())
        df.show()

