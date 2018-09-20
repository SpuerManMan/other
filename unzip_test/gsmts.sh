#!/bin/sh
echo "************start gsmts.sh********************"


gsmts_path=/usr/local/nbpt/mobilets/gsmts/webapps/
g_path=/usr/local/nbpt/mobilets/gsmts/gsmts_bak/
conf_path=/usr/local/nbpt/mobilets/gsmts/gsmts_conf/
security_path=/usr/local/nbpt/mobilets/gsmts/webapps/gsmts_918/WEB-INF/classes/
security_file=security.properties
jdbc_path=/usr/local/nbpt/mobilets/gsmts/webapps/gsmts_918/WEB-INF/classes/conf/custom/
jdbc_file=jdbc.properties
server_path=/usr/local/nbpt/mobilets/gsmts/webapps/gsmts_918/WEB-INF/classes/conf/custom/
server_file=server-config.xml
g_file=/usr/local/nbpt/mobilets/gsmts/

if [ ! -d $g_path ]
then
   mkdir -p $g_path
   chmod 777 * -R
else
	rm -rf ${g_path}/*
fi

if [ ! -d $conf_path ]
then
   mkdir -p $conf_path
   chmod 777 * -R
fi

cd $gsmts_path

if [ -d 'gsmts_918' ]
then
   echo "************备份配置文件******************"
   cp -r $security_path$security_file $conf_path
	sleep 2
	cp -r $jdbc_path$jdbc_file $conf_path
	sleep 2
	cp -r $server_path$server_file $conf_path
	sleep 2 
fi

cd $gsmts_path

file_path=$gsmts_path$file
if [ -f $file_path ]
then
    echo "************rm zip******************"
	rm -rf $file
fi
sleep 2

DATE=$(date +%m%d)
if [ -d 'gsmts_918' ]
then
  echo "************备份gsmts******************"
  cp -r gsmts_918 gsmts_${DATE}_bak
  sleep 5
 
  zip -r gsmts_${DATE}_bak.zip  gsmts_${DATE}_bak
  echo "************删除 gsmts******************"
  rm -rf gsmts_918
  rm -rf gsmts_${DATE}_bak
fi

file=gsmts_${DATE}_bak.zip
zipfile=$gsmts_path$file
if [ -f $zipfile ]
then
    echo "************移动 zip******************"
    mv -f $zipfile $g_path
fi

if [ -f ${g_file}*.zip ]
then
    echo "************移动 安装包******************"
    mv -f ${g_file}*.zip $gsmts_path
	unzip -o ${gsmts_path}*.zip	
	sleep 2
	echo "************替换配置文件******************"
	cp -f $conf_path$security_file $security_path
	sleep 2
	cp -f $conf_path$jdbc_file $jdbc_path
	sleep 2
	cp -f $conf_path$server_file $jdbc_path
	
	#chmod 777 * -R
fi


echo "Done!"





