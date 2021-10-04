This is a data pipeline designed to convert a set of trace files and an OSM xml file 
to be run in the georouting veins simulation

The veins simulation requires 3 xml files to function properly

    - A sumo network file
    - A sumo polygon file
    - A sumo route file

Instructions

#1
Place bursa1origional.csv, BursaScenario.osm.xml, and POIs.csv file into the clientFiles directory
The files need to be named exactly to function properly

#2
If you have make installed simply call make in the base directory

$make

#3
Any of the previous steps in the process can be re-run by calling either

$make net
$make trace
$make poly
$make route
$make code_snippets

#for github users

-I had to remove the client files so that I am not sharing any proprietary information so this is just to showcase some of my work and not meant to actually be run

-The .net file is compressed to save on storage space, you'll need to uncompress it to use it in the program

-This program makes extensive use of a makefile to document and excecute the steps in the data pipeline process, normally make isn't used for interpretted languages like Python but I find it very useful for this purpose.
