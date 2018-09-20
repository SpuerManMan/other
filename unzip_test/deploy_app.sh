
#!/bin/bash
#运行时输入3个参数,第一个业务程序的压缩包,第二个业务程序的起始通道号,第三个要部署业务程序的通道数量
#./deploy_app.sh ./PSService.zip 512 5

#judge user
if [ `whoami` != root ] ; then
	echo "deploy_app.sh exit:You must be root to run this script!"
	exit 1
fi


#if [[ "${variable}" =~ "^[[:digit:]]*$" ]]; then 
#echo "Found digit string!" 
#fi 

echo "source file:"$1;

inputfile="$1"
inputfile2=${inputfile^^}
#echo $inputfile2
#echo  ${inputfile2:0:2}
#echo  ${inputfile2:0:4}

echo "kill all running APP";
if [[  ${inputfile2:0:2} == "PS" ]]; then
	APP_HOME="/usr/local/nbpt/mobilets/PSService_"
	kill -9 `ps -ef|grep PSService_'[0-9]\{1,3\}'.bin | awk '{print $2}'`;
elif [[ ${inputfile2:0:4} == "WLAN" ]]; then
	APP_HOME="/usr/local/nbpt/mobilets/WLANService_"
	kill -9 `ps -ef|grep WLANService_'[0-9]\{1,3\}'.bin | awk '{print $2}'`;
else
    echo "source file error"
	exit 1
fi



mybackfile="${APP_HOME}backup-`date '+%y%m%d-%H'`.bak"


unzip_before() {
	var135="$1";
	echo "${var135}";
	rm -rf "${var135}/bin/*";
	rm -rf "${var135}/core.*";
	rm -rf "${var135}/lib*.so";
	rm -rf "${var135}/lib*.so.*";
}

unzip_after() {
	var246="$1";
	if [ ! -d "${var246}/upload" ]; then
		mkdir "${var246}/upload";
	else
		rm -rf "${var246}/upload/*";
	fi

	if [ ! -d "${var246}/config" ]; then
		mkdir "${var246}/config";
	fi

	if [ ! -d "${var246}/download" ]; then
		mkdir "${var246}/download";
	fi
	
	if [ ! -d "${var246}/temp" ]; then
		mkdir "${var246}/temp";
	else
		rm -rf "${var246}/temp/*";
	fi

	if [ ! -d "${var246}/log" ]; then
		mkdir "${var246}/log";
	else
		rm -rf ${var246}/log/*;
	fi

	chmod -R 777 "${var246}";
}
 


if [ $# -eq 3 ]; then

	echo "initialize pschannel number:"$2;
	echo "deploy number:"$3;
	
	if [ ! -f $mybackfile ] ; then
		for((temp=0;temp<$3;temp++))
		do	
			((initvalue=$2+temp));				
			if [ -d "$APP_HOME$initvalue" ];then
				echo "... APP backup >>> `basename $mybackfile` ...";
				cd "$APP_HOME$initvalue"
				rm -rf "$APP_HOME$initvalue/core.*"
				if command -v zip > /dev/null 2>&1; then 
					zip -r $mybackfile *.* bin config
				else 
					tar zcvf $mybackfile *.* bin config
				fi
				cd -
				break
			fi;
		done;
	fi
	
	
	for((temp=0;temp<$3;temp++))
	do	
		((initvalue=$2+temp));
		var=$APP_HOME$initvalue
		if [ -d "${var}" ];then
			echo "... APP Update ...";
			unzip_before ${var};
		else
			echo "... APP Install ...";
		fi;

		unzip -o $1 -d "${var}";
		
		unzip_after ${var};

	done;

elif [ $# -eq 1 ]; then
	APP_HOME2="${APP_HOME}*"
	#echo ${APP_HOME}

	if [ ! -f $mybackfile ] ; then
		for var in $APP_HOME2; do
		    echo $var
			ChId=${var#*_}
			echo $ChId
			if [[ $ChId =~ ^[0-9]+$ ]] && [ -d ${var} ] && [ $ChId -ge 100 ] && [ $ChId -le 999 ] ; then
				echo "... APP backup >>> `basename $mybackfile` ...";
				cd "${var}"
				rm -rf "${var}/core.*"
				if command -v zip > /dev/null 2>&1; then 
					zip -r $mybackfile *.* bin config
				else 
					tar zcvf $mybackfile *.* bin config
				fi
				cd -
				break
			else
				echo "skip ... ${var}"
			fi
		done
	fi
	
	echo "... APP Install or Update ...";
	for var in $APP_HOME2; do
		ChId=${var#*_}
	    if [[ $ChId =~ ^[0-9]+$ ]] && [ -d ${var} ] && [ $ChId -ge 100 ] && [ $ChId -le 999 ] ; then
			unzip_before ${var};
			
			unzip -o $1 -d "${var}";			
				
			unzip_after ${var};
		else
			echo "skip ... ${var}"
	    fi
	done 
else
    echo "input param error"
fi
	
echo "Over...";
