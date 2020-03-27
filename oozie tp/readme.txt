#create file script pig for word count
[optionl if script exist ] sudo gedit /home/cloudera/countscript.pig

#create file textWord for data
use interface graphic

# create folder in hadoop
hadoop fs -mkdir countword

# copy file script pig to hadoop folder
hadoop fs -copyFromLocal /home/cloudera/countscript.pig countword/

# copy file textWord to hadoop folder
hadoop fs -copyFromLocal /home/cloudera/textWord countword/

# list items folder in hadoop
hadoop fs -ls countword/

# execute script pig 
pig
# console pig
grunt> exec hdfs://quickstart.cloudera:8020/user/cloudera/countword/countscript.pig

# go to Hue UI to see job running

# get output from hadoop

hadoop fs -copyToLocal result/ /home/cloudera/results/

# open folder results in local to see result of script word count