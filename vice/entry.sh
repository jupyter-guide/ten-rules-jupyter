#!/bin/bash

echo '{"irods_host": "data.cyverse.org", "irods_port": 1247, "irods_user_name": "anonymous", "irods_zone_name": "iplant"}' | envsubst > $HOME/.irods/irods_environment.json

cd $HOME/vice
mv $HOME/ten-rules-jupyter $HOME/vice/

echo '{"irods_host": "data.cyverse.org", "irods_port": 1247, "irods_user_name": "$IPLANT_USER", "irods_zone_name": "iplant"}' | envsubst > $HOME/.irods/irods_environment.json

exec jupyter lab --no-browser
