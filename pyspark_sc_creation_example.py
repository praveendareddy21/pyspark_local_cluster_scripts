from pyspark import SparkConf, SparkContext

"""
conf = SparkConf()
conf.setMaster('spark://HEAD_NODE_HOSTNAME:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)
"""


conf = SparkConf()
conf.setMaster('spark://red-GL552VW:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

print(sc)