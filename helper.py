'''
https://replit.com/@MaxOffreal/GravitySimple#main.py
dv_xdt1 = (
      	    - G * m2 * (x1 - x2)
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            - G * m3 * (x1 - x3)
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            + k * q1 * q2 / m1 * (x1 - x2)
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            + k * q1 * q3 / m1 * (x1 - x3)
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
        )

dv_xdt1 = force(m1,q1,x1,y1, m2,q2,x2,y2, 0)
		+ force(m1,q1,x1,y1, m3,q3,x3,y3, 0)
'''

def force(ma, qa, xa, ya, mb, qb, xb, yb, axis):
	'''
	axis - номер оси, х = 0, у = 1
	'''
	G, k = 6.67e-11, 9.0e9
	dist = ((xa - xb)**2 + (ya - yb)**2)**1.5
	d = [xa - xb, ya - yb]
	f = ((- G * mb + k * qa * qb / ma) * d[axis]) / dist
	return f