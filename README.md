# mapping-converter

With this tool you are able to convert .svg output from video mapping software like Madmapper or Mapio to PiMapper surfaces.<br />
Its not finished yet, but the basic concept works.<br />
Problems to solve: <br />

Will be a new feature for PocketVJ 3.2<br />

##Instruction

- Copy parser.py to a folder.<br />
- Place a slices.svg in the same folder (I used an .svg export from Madmapper).<br />
- cd into your folder and run: python parser_one_file.py
- to output a .xml file to open in PiMapper, write: 
python parser_one_file.py > /path/to/file/surfaces.xml

/home/pi/openFrameworks/addons/ofxPiMapper/example/bin/data/surfaces.xml
