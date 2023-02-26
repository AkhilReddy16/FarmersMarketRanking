hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
 -file /home/akhil/farmersMarket/code/mapper.py \
 -mapper /home/akhil/farmersMarket/code/mapper.py \
 -file /home/akhil/farmersMarket/code/reducer.py \
 -reducer /home/akhil/farmersMarket/code/reducer.py \
 -input /user/akhil/fm_data.csv -output /user/akhil/fm