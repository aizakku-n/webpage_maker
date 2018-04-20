WD=~/workspace/webpage_maker
fo=`date "+%Y%m%d-%H%M%S"`.json

while true
do
  python $WD/python/crawlURLnyaaOverview.py | python $WD/python/crawlURLnyaaMakeJSON.py -j $WD/json/data_latest.json > $WD/json/$fo
  cp $WD/json/$fo $WD/json/data_latest.json
  ftp -n < $WD/bin/
  echo 'upload new json'
  sleep 8h
done
