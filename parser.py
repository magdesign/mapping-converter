from svgpathtools import svg2paths
import cmath
paths, attributes = svg2paths('slices2.svg')
print "<surfaces>"
for path in paths[1:-1]:
    print """    <surface type="1">
        <vertices>"""
    for line in path:
        print  "            <vertex>"
        print "                <x>" + str(line.start.real) + "</x>"
        print "                <y>" + str(line.start.imag) + "</y>"
        print  "            </vertex>"
    print """        </vertices>
        <texCoords>
            <texCoord>
                <x>0.000000000</x>
                <y>0.000000000</y>
            </texCoord>
            <texCoord>
                <x>1.000000000</x>
                <y>0.000000000</y>
            </texCoord>
            <texCoord>
                <x>1.000000000</x>
                <y>1.000000000</y>
            </texCoord>
            <texCoord>
                <x>0.000000000</x>
                <y>1.000000000</y>
            </texCoord>
        </texCoords>
        <source>
            <source-type>none</source-type>
            <source-name>none</source-name>
        </source>
        <properties>
            <perspectiveWarping>1</perspectiveWarping>
        </properties>
    </surface>"""
print """</surfaces>"""        

# <surface type="0"> means triangle surface 
# <surface type="1"> means quad surface 
# textCoords are the coordinates for the input texture
# <source-type>none</source-type> you can insert image or movie
# <source-name>none</source-name> the actual name of the source, e.g. testscreen.png

