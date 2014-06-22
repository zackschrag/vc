# !/bin/bash

while true
do
		rsync --progress --delete --exclude="sync*.sh" --exclude="migrations/*" -avze ssh velocichapter/ $1:/webapps/vc-mgr/vc
		sleep 1
done