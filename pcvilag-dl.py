#!/usr/bin/env python
# coding: utf-8

"""
pcvilag.muskatli.hu downloader
Copyright (C) 2015 Gyulai Gergő
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

import platform
import urllib
import re
from subprocess import call

#get platform
PF = platform.system() 

#set HOME for the files...
WIN = 'Windows'

if PF==WIN:
  HOME = "C:\\PCVilag-docs\\"
  bs = "\\"
else:
  HOME = os.path.expanduser('~')+"/PCVilag-docs/"
  bs = "/"

#Check the root folder... if not exists it will create
#if it exists do nothing
def check_root():
  print "Checking root folder...",
  if not os.path.exists(HOME):
    print "CREATING DIRECTORYs"
    os.mkdir(HOME, 0755) 
    if not os.path.exists(HOME+"books"):
      os.mkdir(HOME+"books", 0755)
    if not os.path.exists(HOME+"mags"):
      os.mkdir(HOME+"mags", 0755)
  else:
    print "OK"

#Make folders for files
def make_folders(u_name, book, full):
	if book:
		print "Making folder: \""+u_name.split(("\\" if PF==WIN else "/"))[1]+"\" in books...",
		if not os.path.exists(HOME+u_name):
			os.mkdir(HOME+u_name, 0755)
		if os.path.exists(HOME+u_name) and not os.path.exists(HOME+u_name+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/")):
			os.mkdir(HOME+u_name+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/"), 0755)
	else:
		if not os.path.exists(HOME+u_name):
			os.mkdir(HOME+u_name, 0755)
		if os.path.exists(HOME+u_name) and not os.path.exists(HOME+u_name+full[5]):
			os.mkdir(HOME+u_name+full[5], 0755)
		if os.path.exists(HOME+u_name+full[5]) and not os.path.exists(HOME+u_name+full[5]+("\\" if PF==WIN else "/")+full[6]):
			os.mkdir(HOME+u_name+full[5]+("\\" if PF==WIN else "/")+full[6], 0755)
		if os.path.exists(HOME+u_name+full[5]+"\\"+full[6]) and not os.path.exists(HOME+u_name+full[5]+("\\" if PF==WIN else "/")+full[6]+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/")):
			os.mkdir(HOME+u_name+full[5]+("\\" if PF==WIN else "/")+full[6]+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/"), 0755)
	print "DONE"

#Check the url
def check_url(url):
	pattern = re.compile("http:\/\/pcvilag.muskatli.hu\/[a-zA-Z0-9\/]+\.html")
	return pattern.match(url)

#get links from */link.php
def get_piclinks(url):
	print "Get pictures' link...",
	s = url.split("/")
	alap = "/".join(s[:-1])+"/"
	link = alap+"/link.php"
	data = urllib.urlopen(link).read()
	tmp = re.findall("kep\.php\?kepparam\=([a-zA-z0-9\-]+\.\w+)",data)
	res = []
	i=0
	
	for element in tmp:
		res.append(alap+element)
		i+=1

	print "DONE"
	return res

#download pictures
def get_pics(links, path, book, full):
  print "Downloading pictures..."
  i=1

  if book:
    path = path+"src"+("\\" if PF==WIN else "/")
  else:
    path = path+full[5]+("\\" if PF==WIN else "/")+full[6]+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/")

  for element in links:
    print str(i).rjust(5)+".",
    urllib.urlretrieve(element,path+element.split("/")[-1])
    print "DONE"
    i+=1

  print "ALL PICTURES DOWNLOADED"

#call bash/cmd with ImageMagick convert method
def convertToPDF(path,u_name, book, full):
	print "Converting pictures to one PDF...",

	if book:
		os.system("convert "+path+"src"+("\\" if PF==WIN else "/")+"*.jpg "+path+u_name.split(("\\" if PF==WIN else "/"))[1]+".pdf")
	else:
		path = path+full[5]+("\\" if PF==WIN else "/")
		os.system("convert "+path+full[6]+("\\" if PF==WIN else "/")+"src"+("\\" if PF==WIN else "/")+"*.jpg "+path+"\\"+u_name.split(("\\" if PF==WIN else "/"))[1]+"-"+full[6]+".pdf")

	print "DONE"

#MAIN
def main():
  check_root()
  url = raw_input("Enter URL:\n")
  
  while(not check_url(url)):
    print "It's not a valid url"
    url = raw_input("Enter a valid URL:\n")

  s = url.split("/")
  
  if s[4]=='cbooks':
    NAME = "books"+("\\" if PF==WIN else "/")+s[5]+("\\" if PF==WIN else "/")
    BOOK = True
  else:
    BOOK = False
    NAME = "mags"+("\\" if PF==WIN else "/")+s[4]+("\\" if PF==WIN else "/")
    
  #todo: unique folder name....
  
  make_folders(NAME, BOOK, s)
  piclinks = get_piclinks(url)
  get_pics(piclinks, HOME+NAME, BOOK, s)
  convertToPDF(HOME+NAME, NAME, BOOK, s)
  
  print "Downloaded and converted files are here: "+HOME+NAME

#############################################################################

if __name__=="__main__":
  main()

