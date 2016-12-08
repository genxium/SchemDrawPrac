import SchemDraw as schem
import SchemDraw.elements as e
d = schem.Drawing()

l_1 = d.add(e.LINE, d='right', l=d.unit)
dot_1 = d.add(e.DOT, label='a')
l_2 = d.add(e.LINE, d='down')
l_3 = d.add(e.LINE, d='left')
l_4 = d.add(e.LINE, d='up') 

d.loopI([dot_1, l_2, l_3, l_4], theta1=45, theta2=360, d='ccw', label='$I_1$')

d.draw()
