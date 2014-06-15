# !/bin/bash

while true
do
		rsync --progress --delete --exclude="sync*.sh" -avze ssh vc/ $1:/webapps/vc-mgr/vc
		sleep 1
done