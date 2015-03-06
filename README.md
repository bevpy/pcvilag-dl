# pcvilag-dl

## Intro
This script has been created according to the requirements of the [PCVilág Downloader Project (Hungarian)](http://www.inf.unideb.hu/~szathml/pmwiki/index.php?n=Py.20150301a) given by Dr. László Szathmáry at the University of Debrecen.

## About
It is a downloader for the [PCVilág (Hungarian)](http://pcvilag.muskatli.hu/), with this script you can easily download books and mags from the site and the pictures will be converted to _one_ (in right order)  PDF file.

## Requirements:
 - ImageMagick convert method

### Libraries:
 - *os*
 - *platform*
 - *urllib*
 - *re*
 - *call from subprocess*

## Tested and worked on:
 - Windows 8.1
 - Elementary OS (Luna)

##Step-by-step
1. Download where you want...
2. Run with `python <absolute or relative file path>/pcvilag-dl.py` or give run attribute (`chmod u+x <path>/pcvilag-dl.py`[Unix system]) for it and you can type this: `<absolute or relative file path>/pcvilag-dl.py`.
3. Firstly it will check it's own directorys `C:\PCVilag-docs\books` and `C:\PCVilag-docs\mags`
  - If not it will create the folder structure
4. Enter a URL... (Valid looks like this: *http://pcvilag.muskatli.hu/irodalom/cbooks/c641/c8.html* point to a book or mag first page.
5. It will create a folder structure in `books` or `mags`. It depends on the link.
6. Download pictures from the website.
7. Convert pictures to PDF. (May be a few moments)
8. Print to the screen where you can find the source files (pictures *src* dir) and the converted ones (full path).

##License
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
