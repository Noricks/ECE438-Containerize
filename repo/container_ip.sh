ip addr show dev eth0 | sed -n "3,3p" | sed -r 's/.*inet (.*)\/16.*/IP Address is: \1/g'