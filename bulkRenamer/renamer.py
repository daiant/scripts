#!/usr/bin/env python3

import os
import sys
import argparse
def main(dir, name):
  i = 0
  if(dir == None):
      dir = "."
  if(name != None):
      name = name + "_"
  else:
      name = ""
  for filename in os.listdir(dir):
    dst =  name + str(i) + ".jpg"
    src = dir + filename
    dst = dir + dst

    # os.rename(src,dst)
    print(src)
    print(dst)
    i += 1

# Driver Code

if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  ap.add_argument("-d", "--dir", required=False,
                    help="images directory")
  ap.add_argument("-n", "--name", required=False,
                    help="aditional name")
  args = vars(ap.parse_args())
  print(args["name"])
  main(args["dir"],args["name"])
