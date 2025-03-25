#
# Regular cron jobs for the python3-huggingface-hub package.
#
0 4	* * *	root	[ -x /usr/bin/python3-huggingface-hub_maintenance ] && /usr/bin/python3-huggingface-hub_maintenance
