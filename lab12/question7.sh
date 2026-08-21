#!/bin/bash

function check {
	if [ -d ./testdir ];then
		ls ./testdir
	else
		mkdir testdir
	fi
}

check
