# !/bin/bash

while true
do
		rsync --progress --delete --exclude="sync*.sh" --exclude="migrations/*" -avze ssh ../vc/ $1:/webapps/vc-mgr/
		sleep 1
done