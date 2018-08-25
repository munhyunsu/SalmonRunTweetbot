#!/bin/bash

rsync -azv -e "ssh -i XXX.pem" SRC/ id@ip:DST/
