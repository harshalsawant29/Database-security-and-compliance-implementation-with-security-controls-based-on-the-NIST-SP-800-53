#!/usr/bin/env bash

echo "Welcome to the ELearningPlatform!"
# "$@" will pass script arguments to mysql.
mysql -s -t "$@"
