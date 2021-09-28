from pyspark import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

flightPerfFilePath = "/databricks-datasets/flights/departuredelays.csv"
airportsFilePath = "/databricks-datasets/flights/airport-codes-na.txt"

airports = spark.read.csv(airportsFilePath, header='true', inferSchema='true', sep='\t')
airports.createOrReplaceTempView("airports")

flightPerf = spark.read.csv(flightPerfFilePath, header='true')
flightPerf.cache()

flightPerf.show(1)
airports.show(1)
