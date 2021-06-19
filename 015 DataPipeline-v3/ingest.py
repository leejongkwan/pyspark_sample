import pyspark
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession

class Ingest:

    def __init__(self,spark):
        self.spark=spark

    def ingest_data(self):
        print("Ingesting from csv")
        customer_df = self.spark.read.csv("retailstore.csv",header=True)
        customer_df.show()

        customer_df.describe().show()

        customer_df.select("Country").show()

        customer_df.groupBy("Country").count().show()

        customer_df.filter("Salary > 30000").show()

        customer_df.groupBy("gender").agg({"salary": "avg", "age": "max"}).show()

        customer_df.orderBy("Salary").show()






