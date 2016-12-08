import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()
op = d.add(e.OPAMP)

short_length_1 = d.unit/12
short_length_2 = d.unit/5

# From the output.
d.add(e.LINE, d='right', xy=op.out, l=d.unit/2)
diode_positive_dot = d.add(e.DOT, botlabel='$V_{diode+}$')
d.add(e.LINE, d='right', l=d.unit/2)
diode = d.add(e.DIODE, d='down');
out_dot_1 = d.add(e.DOT)
r_load = d.add(e.RES, d='down', label='$R_L$')
out_dot_2 = d.add(e.DOT)

# From the inverting input.
d.add(e.LINE, d='left', xy=op.in1, l=d.unit/3)
d.add(e.DOT, lftlabel='$V_{-}$')
d.add(e.LINE, d='up', l=d.unit/3)
d.add(e.LINE, d='right', tox=(diode_positive_dot.center)) 
diode_negative_dot = d.add(e.DOT, toplabel='$V_{diode-}$')
d.push()
d.add(e.GAP_LABEL, d='down', toy=diode_positive_dot.center, label='$U_{diode \; bias}$')
d.pop()
d.add(e.LINE, d='right', tox=(out_dot_1.center + [short_length_2, 0]))
d.add(e.LINE, d='down', toy=out_dot_1.center)
d.add(e.LINE, d='left', tox=out_dot_1.center)

# From the non-inverting input.
d.add(e.LINE, d='left', xy=op.in2, l=d.unit/3)
in_dot_1 = d.add(e.DOT, lftlabel='$V_+$')
d.add(e.GAP_LABEL, d='down', toy=out_dot_2.center, label='$U_{in}$')
in_dot_2 = d.add(e.DOT, lftlabel='$V_{ref}$')
d.add(e.LINE, d='right', tox=out_dot_2.center)

# Add output current label.
out_current_arrow = d.add(e.ARROW_I, xy=(out_dot_1.center + [.4, -.8]), d='down', toy=out_dot_2.center + [0, .5])
out_current_label = out_current_arrow.add_label('$I_{out}$', loc='bot', align=('left', 'center'))

# Preview the whole plot.
d.draw()
