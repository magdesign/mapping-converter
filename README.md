# mapping-converter

With this tool you are able to convert .svg output from video mapping software like Madmapper or Mapio to PiMapper surfaces.<br />
Its not finished yet, but the basic concept works.<br />
Will be a new feature for PocketVJ 3.2<br />

##Problems to solve: <br />
- The zero point must be calculated and added to the values depending on the resolution. <br />
- Define if it is a quad or trianle, surface type="0" is triangle, surface type="1" is aquad
- Any help very welcome..<br />


##Instruction

- Copy parser_on_file.py to a folder.<br />
- Place a slices.svg in the same folder (I used an .svg exported from Madmapper).<br />
- cd into your folder and run: python parser_one_file.py
- to output a .xml filefor PiMapper, write: 
python parser_one_file.py > /path/to/file/surfaces.xml

- Then copy this file to your PiMapper, somewhere here:
/home/pi/openFrameworks/addons/ofxPiMapper/example/bin/data/surfaces.xml

Difference between the parser.py and parser_one_file.py, the later is only made for .svg with one quad inside.


Thanks to turingmachine for the help with the basic code.
