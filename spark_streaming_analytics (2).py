##################################################################################################################
# PURPOSE:      Computes the frequency of Twitter hashtags in each batch of data
# INSTRUCTIONS: Run this code on CLIENT terminal to consume Twitter tweets from SERVER and return streaming analytics
# FILENAME:     spark_streaming_analytics.py
# LAST UPDATE:  4/16/21
##################################################################################################################
## CLIENT SECTION 1 START (COPY/PASTE THIS ENTIRE SECTION INTO TERMINAL)

## LIBRARIES
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext given cores and batch interval (this is an integer)
batch_interval = 10

sc = SparkContext('local[2]', 'NetworkWordCount')

# create Streaming Context from spark context w interval size 5 seconds
ssc = StreamingContext(sc, batch_interval)

lines = ssc.socketTextStream('localhost', 9009)

# set checkpoint for RDD recovery
ssc.checkpoint('checkpoint_twitter_streaming_app')

#####
# Split each line into words
words = lines.flatMap(lambda l: l.split(' '))

# Retain hashtags (hint:#) and map each hashtag in each batch to (hashtag,1)
hashtags = words.filter(lambda tag: '#' in tag).map(lambda tagplace: (tagplace, 1))

# Count the hashtags in the batch
wordCounts = hashtags.reduceByKey(lambda x, y: x+y)

# Print hashtags, counts for each batch
wordCounts.pprint()

# Start the computation
ssc.start()  

## CLIENT SECTION 1 END
##################################################################################################################
