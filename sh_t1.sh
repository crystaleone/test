#!/bin/sh
for i in 1..10:
  wget http://down.xiaoml.com/img/$i.png

find ./ -size +500k
