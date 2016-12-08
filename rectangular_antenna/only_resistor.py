import SchemDraw as schem
import SchemDraw.elements as e
d = schem.Drawing()

seg_length = (d.unit)
l_1 = d.add(e.LINE, d='right', l=seg_length)
dot_1 = d.add(e.DOT, label='a')

r_1 = d.add(e.RES, d='down', l=seg_length, label='R')

dot_2 = d.add(e.DOT, botlabel='b')
l_2 = d.add(e.LINE, l=seg_length, d='left')
l_3 = d.add(e.LINE, l=seg_length, d='up') 

d.loopI([l_1, r_1, l_2, l_3], theta1=45, theta2=315, d='ccw', label='$I_1$')

d.draw()
