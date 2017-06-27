import urllib
import sys
from pyspark import SparkConf, SparkContext


conf = SparkConf()
conf.setMaster('spark://red-GL552VW:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)



f = urllib.urlretrieve ("http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz", "kddcup.data_10_percent.gz")
data_file = "./kddcup.data_10_percent.gz"
raw_data = sc.textFile(data_file)



a = range(100)
data = sc.parallelize(a)

print(data.count())
print(data.take(20))
