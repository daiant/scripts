import urllib.request
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from db import *
import os
import random
import sys
import argparse

def getPath():
	user = os.getenv('USER')
	path = '/home/' + user + '/Pictures/Wallpapers/'
	if not os.path.exists(path):
		os.mkdir(path)
	return path
def getRandomPath():
	try:
		dir = random.choice(getDirectories())
		print(dir)
		return dir
	except:
		print("Empty directory list")
		exit()


def download():
	path = getRandomPath()
	try:
		choice = random.choice(os.listdir(path))
		return os.path.join(path,choice)
	except:
		pass


def change_wallpaper(dir):
	if(dir!=None):
		full_path=os.path.abspath(dir)
	else:
		full_path=download()

	if full_path is None:
		print("Directory empty. Aborting...")
	else:
		# Feh se encarga de la whitelist
		os.system("feh --bg-scale "+full_path)


if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  ap.add_argument("-a", "--add", required=False,
                    help="add directory")
  ap.add_argument("-d", "--del", required=False,
					help="delete directory")
  ap.add_argument("-s", "--set", required=False,
					help="set a specific image")
  ap.add_argument("-l", "--list",action='store_true', required=False,
					help="show directories")

  args = vars(ap.parse_args())
  if(args["add"] != None):
	  setDirectory(args["add"])
	  exit()
  elif(args["del"] != None):
	  deleteDirectory(args["del"])
	  exit()
  elif(args["list"] != False):
	  stringDirectories()
	  exit()

  change_wallpaper(args["set"])
