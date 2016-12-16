
from svgpathtools import svg2paths
import cmath
paths, attributes = svg2paths('slices.svg')
print """
<surfaces>
    <surface type="1">
        <vertices>"""

for line in paths[1]:
	print  "            <vertex>"
	print "                <x>" + str(line.start.real) + "</x>"
	print "                <y>" + str(line.start.imag) + "</y>"
	print  "            </vertex>"

print """

        </vertices>
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
    </surface>
</surfaces>
"""
