#!/bin/bash

speed=3000000000
mass=1
Energy=$(bc << EOF
$mass*$speed*$speed
EOF
)
echo "The energy of the moving object is $Energy"
