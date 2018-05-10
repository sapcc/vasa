#hannes.ebelt@sap.com
#create dump of vpserver process each 30min
#crontab -e: */30 * * * * /opt/netapp/vpserver/jdklogger.sh 

for i in $(pgrep -u vpserver); do
  /jail/support/jdk1.8.0_131/bin/jstack -l $i |gzip > /support/vpserver/file_$(date +%Y%m_%d%H%M%S).log.gz
done
