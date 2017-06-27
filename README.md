# mapping-converter

With this tool you are able to convert .svg output from video mapping software like Madmapper, Mapio or Resolume to PiMapper surfaces.<br />
Its not finished yet, but the basic concept works.<br />
<br />

##Problems to solve: <br />
- Dont know how to get the zero points, the quads size is correct, but position not, tryed to add numbers like x value + 960 and y value +540.... <br />
- Define if it is a quad or trianle, surface type="0" is triangle, surface type="1" is quad
- Any help very welcome..<br />

Here you see the two masks I exported from Madmapper:

![alt tag](https://github.com/magdesign/mapping-converter/blob/master/screenshots/madmapper_export.jpg)

and here you see how this looks then in PiMapper after converting with this tool:

![alt tag](https://github.com/magdesign/mapping-converter/blob/master/screenshots/PiMapper_import.jpg)

the size looks the same, but the placing... and I guess it eats the content mirrored..

##Instruction

- Copy parser_one_file.py to a folder.<br />
- Place a slices.svg (I used an .svg exported from Madmapper) in the same folder as the script.<br />
- cd into your folder and run: python parser_one_file.py
- output the .xml file for PiMapper, do something like: 
python parser_one_file.py > /path/to/file/surfaces.xml

- Then copy this file to your PiMapper, located somewhere here (depending where you isntalled openframeworks:
/home/pi/openFrameworks/addons/ofxPiMapper/example/bin/data/surfaces.xml

Difference between the parser.py and parser_one_file.py, the later is only made for .svg with one quad inside, parser.py is made for more than one quad, and looks for a file called slices2.svg

You might need to install depencies first: pip install svgtools svgpathtools svgwrite

Thanks to turingmachine https://github.com/turingmachine for the help with the basic code.
