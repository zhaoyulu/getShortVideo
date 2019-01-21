#!/bin/bash
set i=0
set j=0
for((i=0;i<10;))
do
         sleep 1s
 	 adb shell input swipe 540 1300 540 500 100
done

