import sys
# Change this to the location that contains the subcells.py folder
subcell_path = '..\\subcells'
if subcell_path not in sys.path:
    sys.path.append(subcell_path)
import subcells as sc
import os
import spira.all as spira
from spira.technologies.mit.process.database import RDD

IXPORT = spira.RDD.PLAYER.IXPORT
TEXT = spira.Layer(number=182)

## Parameterization
# Trackpitch in microns
tp = 10
sc.tp = tp

# Inductor widths
Scaling = (1+(tp-10)*0.25)
L1_width = 0.14*tp*Scaling
L2_width = 0.105*tp*Scaling
L3_width = 0.12*tp*Scaling
L4_width = 0.18*tp*Scaling
L5_width = 0.145*tp*Scaling
L6_width = 0.28*tp*Scaling
L7_width = 0.3*tp*Scaling
L8_width = 0.16*tp*Scaling
L9_width = 0.2*tp*Scaling
L11_width = 0.2*tp*Scaling
L13_width = 0.14*tp*Scaling
L14_width = 0.11*tp*Scaling
L15_width = 0.13*tp*Scaling
L16_width = 0.125*tp*Scaling
L17_width = 0.13*tp*Scaling
L18_width = 0.28*tp*Scaling
L19_width = 0.3*tp*Scaling
L20_width = 0.12*tp*Scaling
L21_width = 0.22*tp*Scaling
L22_width = 0.105*tp*Scaling
L23_width = 0.17*tp*Scaling
L24_width = 0.15*tp*Scaling
LB1_width = 0.14*tp*Scaling
LB2_width = 0.2*tp*Scaling

class PCELL(spira.PCell):
    __name_prefix__ = "LSmitll_AND2T_v2p1"
    def create_elements(self, elems):
        M6Strips = spira.SRef(M6_strips())
        IXports = spira.SRef(IX_ports())
        M0M4M7tracks = spira.SRef(M0M4M7_tracks())
        jjfill = spira.SRef(junction_fill())
        M4M5M6M7conns = spira.SRef(M4M5M6M7_connections())
        vias = spira.SRef(M5M6_connections())
        bias = spira.SRef(biasing())
        jjs = spira.SRef(junctions())
        res = spira.SRef(resistors())
        tblocks = spira.SRef(trackblocks())
        elems += [M6Strips, IXports, M0M4M7tracks, jjfill, M4M5M6M7conns,
                  vias, bias, jjs, res, tblocks]
        # Bias ports
        PB1W = spira.Port(name='PB1W',midpoint=bias.reference.elements['bias1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB1E = spira.Port(name='PB1E',midpoint=bias.reference.elements['bias1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2W = spira.Port(name='PB2W',midpoint=bias.reference.elements['bias2'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB2E = spira.Port(name='PB2E',midpoint=bias.reference.elements['bias2'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3W = spira.Port(name='PB3W',midpoint=bias.reference.elements['bias3'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB3E = spira.Port(name='PB3E',midpoint=bias.reference.elements['bias3'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4W = spira.Port(name='PB4W',midpoint=bias.reference.elements['bias4'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB4E = spira.Port(name='PB4E',midpoint=bias.reference.elements['bias4'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5W = spira.Port(name='PB5W',midpoint=bias.reference.elements['bias5'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB5E = spira.Port(name='PB5E',midpoint=bias.reference.elements['bias5'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6W = spira.Port(name='PB6W',midpoint=bias.reference.elements['bias6'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB6E = spira.Port(name='PB6E',midpoint=bias.reference.elements['bias6'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7N = spira.Port(name='PB7N',midpoint=bias.reference.elements['bias7'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB7S = spira.Port(name='PB7S',midpoint=bias.reference.elements['bias7'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8N = spira.Port(name='PB8N',midpoint=bias.reference.elements['bias8'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PB8S = spira.Port(name='PB8S',midpoint=bias.reference.elements['bias8'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Bias Input Port
        PBias = spira.Port(name='PBias',midpoint=(9.5*tp,7.0*tp),process=spira.RDD.PROCESS.M6)
        # Resistor Ports
        PR1W = spira.Port(name='PR1W',midpoint=res.reference.elements['R1'].ports['M6:PN'].midpoint,process=spira.RDD.PROCESS.M6)
        PR1E = spira.Port(name='PR1E',midpoint=res.reference.elements['R1'].ports['M6:PS'].midpoint,process=spira.RDD.PROCESS.M6)
        # Junction ports
        PJ1 = spira.Port(name="PJ1",midpoint=jjs.reference.elements['J1'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ2 = spira.Port(name="PJ2",midpoint=jjs.reference.elements['J2'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ3 = spira.Port(name="PJ3",midpoint=jjs.reference.elements['J3'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ4 = spira.Port(name="PJ4",midpoint=jjs.reference.elements['J4'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ5 = spira.Port(name="PJ5",midpoint=jjs.reference.elements['J5'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ6 = spira.Port(name="PJ6",midpoint=jjs.reference.elements['J6'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ7 = spira.Port(name="PJ7",midpoint=jjs.reference.elements['J7'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ8 = spira.Port(name="PJ8",midpoint=jjs.reference.elements['J8'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ9 = spira.Port(name="PJ9",midpoint=jjs.reference.elements['J9'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ10 = spira.Port(name="PJ10",midpoint=jjs.reference.elements['J10'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ11 = spira.Port(name="PJ11",midpoint=jjs.reference.elements['J11'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ12 = spira.Port(name="PJ12",midpoint=jjs.reference.elements['J12'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ13 = spira.Port(name="PJ13",midpoint=jjs.reference.elements['J13'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ14 = spira.Port(name="PJ14",midpoint=jjs.reference.elements['J14'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ15 = spira.Port(name="PJ15",midpoint=jjs.reference.elements['J15'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        PJ16 = spira.Port(name="PJ16",midpoint=jjs.reference.elements['J16'].ports['M6:PJ'].midpoint,process=spira.RDD.PROCESS.M6)
        # Pin Ports
        PA = spira.Port(name="PA",midpoint=IXports.reference.elements['A'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PB = spira.Port(name="PB",midpoint=IXports.reference.elements['B'].center+(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PCLK = spira.Port(name="PCLK",midpoint=IXports.reference.elements['CLK'].center-(0.25*tp,0),process=spira.RDD.PROCESS.M6)
        PQ = spira.Port(name="PCLK",midpoint=(8.45*tp,1.5*tp),process=spira.RDD.PROCESS.M6)
        # VIAs
        PV1 = spira.Port(name="PV1",midpoint=vias.reference.elements['via1'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV2 = spira.Port(name="PV2",midpoint=vias.reference.elements['via2'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        PV3 = spira.Port(name="PV3",midpoint=vias.reference.elements['via3'].ports['M6:PV'].midpoint,process=spira.RDD.PROCESS.M6)
        # Nodes
        PN7 = spira.Port(name="PN7",midpoint=(3.5*tp,0.5*tp),process=spira.RDD.PROCESS.M6)
        PN21 = spira.Port(name="PN21",midpoint=(5.5*tp,5.5*tp),process=spira.RDD.PROCESS.M6)
        PN23 = spira.Port(name="PN23",midpoint=(6.2225*tp,3.48*tp),process=spira.RDD.PROCESS.M6)
        PN44 = spira.Port(name="PN44",midpoint=(PJ5.x,PJ14.y),process=spira.RDD.PROCESS.M6)

        # Inductors
        L1 = spira.RoutePath(port1=PA,port2=PJ1,path=[(PJ1.x,PA.y)],width=L1_width,layer=sc.M6)
        L2 = spira.RoutePath(port1=PJ1,port2=PJ2,path=[(PJ1.x,PJ2.y)],width=L2_width,layer=sc.M6)
        L3 = spira.RoutePath(port1=PJ2,port2=PN7,path=[(PJ2.x,PN7.y)],width=L3_width,layer=sc.M6)
        L4 = spira.RoutePath(port1=PN7,port2=PJ3,path=[(5.5*tp,PN7.y),(5.5*tp,PJ3.y)],width=L4_width,layer=sc.M6)
        L5 = spira.RoutePath(port1=PJ3,port2=PV1,path=[(PJ3.x,PV1.y)],width=L5_width,layer=sc.M6)
        L6_1 = spira.RoutePath(port1=PV1,port2=PJ5,path=[(PJ5.x,PV1.y)],width=L6_width,layer=sc.M5)
        L6_2 = spira.RoutePath(port1=PJ5,port2=PN44,path=[(PJ5.x,PN44.y)],width=L6_width,layer=sc.M6)
        L7_1 = spira.RoutePath(port1=PV1,port2=PJ4,path=[(PV1.x,PJ4.y)],width=L7_width,layer=sc.M5)
        L7_2 = spira.RoutePath(port1=PJ4,port2=PJ8,path=[(PJ4.x,PJ8.y)],width=L7_width,layer=sc.M6)
        L8 = spira.RoutePath(port1=PCLK,port2=PJ6,path=[(PJ6.x,PCLK.y)],width=L8_width,layer=sc.M6)
        L9 = spira.RoutePath(port1=PJ6,port2=PJ7,path=[(PJ6.x,PJ7.y)],width=L9_width,layer=sc.M6)
        L11 = spira.RoutePath(port1=PJ7,port2=PJ8,path=[(PJ8.x,PJ7.y)],width=L11_width,layer=sc.M6)
        L13 = spira.RoutePath(port1=PB,port2=PJ9,path=[(PB.x,PJ9.y)],width=L13_width,layer=sc.M6)
        L14 = spira.RoutePath(port1=PJ9,port2=PJ10,path=[(PJ9.x,PJ10.y)],width=L14_width,layer=sc.M6)
        L15 = spira.RoutePath(port1=PJ10,port2=PN21,path=[(PJ10.x,PN21.y)],width=L15_width,layer=sc.M6)
        L16 = spira.RoutePath(port1=PN21,port2=PJ11,path=[(3.5*tp,PN21.y),(3.5*tp,5.195*tp),(PJ11.x,5.195*tp)],width=L16_width,layer=sc.M6)
        L17 = spira.RoutePath(port1=PJ11,port2=PV2,path=[(PJ11.x,PV2.y)],width=L17_width,layer=sc.M6)
        L18_1 = spira.RoutePath(port1=PV2,port2=PJ13,path=[(PJ13.x,PV2.y)],width=L18_width,layer=sc.M5)
        L18_2 = spira.RoutePath(port1=PJ13,port2=PN44,path=[(PJ13.x,PN44.y)],width=L18_width,layer=sc.M6)
        L19_1 = spira.RoutePath(port1=PV2,port2=PJ12,path=[(PJ12.x,PV2.y)],width=L19_width,layer=sc.M5)
        L19_2 = spira.RoutePath(port1=PJ12,port2=PJ8,path=[(PJ12.x,PJ8.y)],width=L19_width,layer=sc.M6)
        L20 = spira.RoutePath(port1=PN44,port2=PJ14,path=[(PN44.x,PJ14.y)],width=L20_width,layer=sc.M6)
        L21 = spira.RoutePath(port1=PJ14,port2=PN23,path=[(PJ14.x,PN23.y)],width=L21_width,layer=sc.M6)
        L22 = spira.RoutePath(port1=PN23,port2=PJ15,path=[(PN23.x,PJ15.y)],width=L22_width,layer=sc.M6)
        L23 = spira.RoutePath(port1=PJ15,port2=PJ16,path=[(8.495*tp,PJ15.y),(8.495*tp,PJ16.y)],width=L23_width,layer=sc.M6)
        L24_1 = spira.RoutePath(port1=PJ16,port2=PR1W,path=[(PJ16.x,PR1W.y)],width=L24_width,layer=sc.M6)
        L24_2 = spira.RoutePath(port1=PR1E,port2=PQ,path=[(PQ.x,PR1E.y)],width=L24_width,layer=sc.M6)
        elems += [L1, L2, L3, L4, L5, L6_1, L6_2, L7_1, L7_2, L8, L9, L11, L13, L14, L15, 
                  L16, L17, L18_1, L18_2, L19_1, L19_2, L20, L21, L22, L23, L24_1, L24_2]

        # Bias inductors
        LB1_1 = spira.RoutePath(port1=PJ1,port2=PB1E,path=[(PJ1.x,PB1E.y)],width=LB1_width,layer=sc.M6)
        LB1_2 = spira.RoutePath(port1=PB1W,port2=PV3,path=[(0.5*tp,PB1W.y),(0.5*tp,PV3.y)],width=LB1_width,layer=sc.M6)
        LB2_1 = spira.RoutePath(port1=PN7,port2=PB2E,path=[(PN7.x,PB2E.y)],width=LB1_width,layer=sc.M6)
        LB2_2 = spira.RoutePath(port1=PB2W,port2=PV3,path=[(0.5*tp,PB2W.y),(0.5*tp,PV3.y)],width=LB2_width,layer=sc.M6)
        LB3_1 = spira.RoutePath(port1=PJ6,port2=PB3E,path=[(PJ6.x,PB3E.y)],width=LB1_width,layer=sc.M6)
        LB3_2 = spira.RoutePath(port1=PB3W,port2=PV3,path=[(0.5*tp,PB3W.y),(0.5*tp,PV3.y)],width=LB1_width,layer=sc.M6)
        LB4_1 = spira.RoutePath(port1=PJ7,port2=PB4E,path=[(PJ7.x,3.0*tp),(PB4E.x,3.0*tp)],width=LB1_width,layer=sc.M6)
        LB4_2 = spira.RoutePath(port1=PB4W,port2=PV3,path=[(0.5*tp,PB4W.y),(0.5*tp,PV3.y)],width=LB1_width,layer=sc.M6)
        LB5_1 = spira.RoutePath(port1=PJ9,port2=PB5W,path=[(PJ9.x,PB5W.y)],width=LB1_width,layer=sc.M6)
        LB5_2 = spira.RoutePath(port1=PB5E,port2=PV3,path=[(PV3.x,PB5E.y)],width=LB1_width,layer=sc.M6)
        LB6_1 = spira.RoutePath(port1=PN21,port2=PB6E,path=[(PN21.x,PB6E.y)],width=LB1_width,layer=sc.M6)
        LB6_2 = spira.RoutePath(port1=PB6W,port2=PV3,path=[(PB6W.x,PV3.y)],width=LB1_width,layer=sc.M6)
        LB7_1 = spira.RoutePath(port1=PN23,port2=PB7N,path=[(PN23.x,PB7N.y)],width=LB1_width,layer=sc.M6)
        LB7_2 = spira.RoutePath(port1=PB7S,port2=PV3,path=[(PV3.x,PB7S.y)],width=LB2_width,layer=sc.M6)
        LB8_1 = spira.RoutePath(port1=PJ16,port2=PB8N,path=[(PB8N.x,PJ16.y)],width=LB1_width,layer=sc.M6)
        LB8_2 = spira.RoutePath(port1=PB8S,port2=PV3,path=[(PB8S.x,PB7S.y),(PV3.x,PB7S.y)],width=LB1_width,layer=sc.M6)
        elems += [LB1_1, LB2_1, LB3_1, LB4_1, LB5_1, LB6_1, LB7_1, LB8_1,
                  LB1_2, LB2_2, LB3_2, LB4_2, LB5_2, LB6_2, LB7_2, LB8_2]

        LBias = spira.RoutePath(port1=PV3,port2=PBias,path=[(PBias.x,PBias.y)],width=LB2_width,layer=sc.M5)

        elems += LBias

        # Text Labels
        elems += spira.Label(text="bias_in",position=(9.5*tp,7*tp),layer=TEXT)
        elems += spira.Label(text="P1 M6 M4",position=(1.8125*tp,1.5025*tp),layer=TEXT)
        elems += spira.Label(text="J1 M6 M5",position=(2.505*tp,1.5025*tp),layer=TEXT)
        elems += spira.Label(text="J2 M6 M5",position=(3.505*tp,1.4875*tp),layer=TEXT)
        elems += spira.Label(text="J3 M6 M5",position=(4.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="PB1 M6 M4",position=(2.1755*tp,2.5005*tp),layer=TEXT)
        elems += spira.Label(text="PB2 M6 M4",position=(2.0745*tp,0.5*tp),layer=TEXT)
        elems += spira.Label(text="P2 M6 M4",position=(1.8125*tp,5.495*tp),layer=TEXT)
        elems += spira.Label(text="J4 M5 M6",position=(4.4875*tp,2.555*tp),layer=TEXT)
        elems += spira.Label(text="J5 M5 M6",position=(5.4525*tp,2.86*tp),layer=TEXT)
        elems += spira.Label(text="J6 M6 M5",position=(2.485*tp,4.5225*tp),layer=TEXT)
        elems += spira.Label(text="PB3 M6 M4",position=(2.135*tp,4.5225*tp),layer=TEXT)
        elems += spira.Label(text="J7 M6 M5",position=(2.995*tp,3.51*tp),layer=TEXT)
        elems += spira.Label(text="PB4 M6 M4",position=(2.0075*tp,3.49*tp),layer=TEXT)
        elems += spira.Label(text="J8 M6 M5",position=(4.4525*tp,3.4975*tp),layer=TEXT)
        elems += spira.Label(text="P3 M6 M4",position=(8.18*tp,5.5025*tp),layer=TEXT)
        elems += spira.Label(text="J9 M6 M5",position=(7.5*tp,5.4625*tp),layer=TEXT)
        elems += spira.Label(text="PB5 M6 M4",position=(7.963*tp,4.499*tp),layer=TEXT)
        elems += spira.Label(text="PB6 M6 M4",position=(5.36*tp,6.12*tp),layer=TEXT)
        elems += spira.Label(text="J10 M6 M5",position=(6.5*tp,5.505*tp),layer=TEXT)
        elems += spira.Label(text="J11 M6 M5",position=(3.8725*tp,4.8125*tp),layer=TEXT)
        elems += spira.Label(text="J12 M6 M5",position=(4.49*tp,4.4425*tp),layer=TEXT)
        elems += spira.Label(text="J13 M6 M5",position=(5.455*tp,4.14*tp),layer=TEXT)
        elems += spira.Label(text="J14 M6 M5",position=(6.0225*tp,3.48*tp),layer=TEXT)
        elems += spira.Label(text="PB7 M6 M4",position=(6.4225*tp,2.775*tp),layer=TEXT)
        elems += spira.Label(text="J15 M6 M5",position=(7.4975*tp,3.4775*tp),layer=TEXT)
        elems += spira.Label(text="J16 M6 M5",position=(7.5025*tp,2.495*tp),layer=TEXT)
        elems += spira.Label(text="PB8 M6 M4",position=(6.7675*tp,1.59*tp),layer=TEXT)
        elems += spira.Label(text="P4 M6 M4",position=(7.75*tp,1.5025*tp),layer=TEXT)
        elems += spira.Label(text="a",position=(1.5*tp,1.5*tp),layer=TEXT)
        elems += spira.Label(text="b",position=(8.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="clk",position=(1.5*tp,5.5*tp),layer=TEXT)
        elems += spira.Label(text="q",position=(8.5*tp,1.5*tp),layer=TEXT)

        # LVS Labels
        elems += spira.Label(text='VDD',position=(9.4948*tp,6.8516*tp),layer=spira.Layer(number=50,datatype=1))
        elems += spira.Label(text='GND',position=(9.653*tp,6.8645*tp),layer=spira.Layer(number=40,datatype=1))
        elems += spira.Label(text='RD',position=(7.8564*tp,1.5093*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB1',position=(2.4909*tp,1.1223*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB2',position=(3.4927*tp,1.8008*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB5',position=(5.149*tp,2.8587*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB3',position=(4.1756*tp,1.5009*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB4',position=(4.1429*tp,2.5643*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB8',position=(4.7449*tp,3.5032*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB6',position=(2.9*tp,4.5202*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB7',position=(3.0048*tp,3.8764*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB9',position=(7.5063*tp,5.8965*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB10',position=(6.5029*tp,5.1712*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB11',position=(3.4913*tp,4.8148*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB12',position=(4.1136*tp,4.4497*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB13',position=(5.104*tp,4.1523*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB14',position=(6.0211*tp,3.8476*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB15',position=(7.5005*tp,3.8099*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RB16',position=(7.4973*tp,2.8394*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB1',position=(1.6215*tp,2.5088*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB2',position=(1.437*tp,0.4947*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB3',position=(1.5744*tp,4.515*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB4',position=(1.5987*tp,3.4927*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB5',position=(8.5558*tp,4.5009*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB6',position=(4.6996*tp,6.113*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB7',position=(6.4241*tp,1.6588*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='RIB8',position=(6.7677*tp,1.2515*tp),layer=spira.Layer(number=52,datatype=1))
        elems += spira.Label(text='clk',position=(1.5013*tp,5.5047*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='q',position=(8.5045*tp,1.5077*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='a',position=(1.5014*tp,1.5089*tp),layer=spira.Layer(number=60,datatype=1))
        elems += spira.Label(text='b',position=(8.504*tp,5.5042*tp),layer=spira.Layer(number=60,datatype=1))
        return elems

class M6_strips(spira.Cell):
    __name_prefix__ = "M6_strips"
    def create_elements(self, elems):
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M6,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M6,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(3.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,0.0125*tp))
        elems += spira.Box(layer=sc.M5,width=0.025*tp,height=0.315*tp,center=(9.9875*tp,0.4925*tp))
        elems += spira.Box(layer=sc.M5,width=0.315*tp,height=0.025*tp,center=(0.4925*tp,6.9875*tp))
        return elems

class IX_ports(spira.Cell):
    __name_prefix__ = "IX_ports"
    def create_elements(self, elems):
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.8125*tp,1.5*tp),alias='A')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(1.8125*tp,5.5*tp),alias='CLK')
        elems += spira.Box(layer=IXPORT,width=0*tp,height=0.2*tp,center=(8.18*tp,5.5*tp),alias='B')
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(5.36*tp,6.115*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.963*tp,4.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(7.754*tp,1.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.768*tp,1.588*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(6.42325*tp,2.773*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.075*tp,0.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.175*tp,2.5*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.005*tp,3.495*tp))
        elems += spira.Box(layer=IXPORT,width=0.052*tp,height=0.052*tp,center=(2.135*tp,4.515*tp))
        return elems

class M0M4M7_tracks(spira.Cell):
    __name_prefix__ = "M0M4M7_tracks"
    def create_elements(self, elems):
        shape=spira.Shape(points=[(5.72*tp,3.72*tp),(5.72*tp,4.28*tp),(6.28*tp,4.28*tp),(6.28*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.04*tp,4.72*tp),(4.04*tp,4.96*tp),(4.28*tp,4.96*tp),(4.28*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,6.04*tp),(4.72*tp,6.28*tp),(5.28*tp,6.28*tp),(5.28*tp,6.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.04*tp,6.04*tp),(4.04*tp,6.28*tp),(4.28*tp,6.28*tp),(4.28*tp,6.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,2.04*tp),(4.72*tp,2.28*tp),(5.28*tp,2.28*tp),(5.28*tp,2.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,2.72*tp),(4.72*tp,4.28*tp),(5.28*tp,4.28*tp),(5.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(3.72*tp,4.72*tp),(3.72*tp,5.28*tp),(3.96*tp,5.28*tp),(3.96*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(3.04*tp,4.72*tp),(3.04*tp,4.96*tp),(3.28*tp,4.96*tp),(3.28*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,4.72*tp),(4.72*tp,4.96*tp),(5.28*tp,4.96*tp),(5.28*tp,4.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(6.72*tp,0.72*tp),(6.72*tp,2.28*tp),(6.96*tp,2.28*tp),(6.96*tp,0.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(4.72*tp,2.04*tp),(4.72*tp,2.28*tp),(5.28*tp,2.28*tp),(5.28*tp,2.04*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(6.04*tp,2.72*tp),(6.04*tp,3.28*tp),(6.28*tp,3.28*tp),(6.28*tp,2.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.72*tp,2.875*tp),(2.72*tp,3.125*tp),(2.875*tp,3.125*tp),(2.875*tp,2.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.875*tp,3.125*tp),(2.875*tp,3.28*tp),(3.125*tp,3.28*tp),(3.125*tp,3.125*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(1.875*tp,3.125*tp),(1.875*tp,3.28*tp),(2.125*tp,3.28*tp),(2.125*tp,3.125*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.125*tp,2.875*tp),(2.125*tp,3.125*tp),(2.28*tp,3.125*tp),(2.28*tp,2.875*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        shape=spira.Shape(points=[(2.875*tp,3.72*tp),(2.875*tp,4.28*tp),(3.125*tp,4.28*tp),(3.125*tp,3.72*tp)])
        elems += spira.Polygon(shape=shape,layer=sc.M0)
        elems += spira.Polygon(shape=shape,layer=sc.M4)
        elems += spira.Polygon(shape=shape,layer=sc.M7)
        
        return elems

class junction_fill(spira.Cell):
    __name_prefix__ = "junction_fill"
    def create_elements(self, elems):
        sys.stdout.write("Adding junction fill.\n")
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,6*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(6*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(7*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(8*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(9*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(5*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,5*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(4*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,3*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,2*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,1*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(2*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(3.53*tp,4.13*tp))
        elems += spira.SRef(sc.ls_FakeJJ_1p5x1p5um(),midpoint=(1*tp,4*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(6.5*tp,4.52*tp))
        elems += spira.SRef(sc.ls_FakeJJ_3umx3um(),midpoint=(3.255*tp,2.505*tp))
        return elems

class M4M5M6M7_connections(spira.Cell):
    __name_prefix__ = "M4M5M6M7_connections"
    def create_elements(self, elems):
        sys.stdout.write('Adding M4M5M6M7 connections.\n')
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,2.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8*tp,3.72*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8*tp,4.37*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8*tp,3.14*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.8*tp,2.49*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,2.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,1.11*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.28*tp,4.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,1.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,5.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,5.095*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,1.015*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,3.175*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,2.6875*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,0.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,2.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.805*tp,2.405*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,5.845*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.335*tp,6.835*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.335*tp,6.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,3.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.335*tp,5.82*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.28*tp,3.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(4.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.335*tp,0.025*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,4.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,1.735*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.335*tp,0.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.335*tp,4.125*tp))
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.945*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.935*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.985*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.1975*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.985*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.965*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.155*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(7.235*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,6.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.265*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.945*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.25*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(5.875*tp,4.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(6.62*tp,2.95*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.945*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.265*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,3.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(1.155*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,2.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(2.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(3.195*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.875*tp,1.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(9.975*tp,0.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(0.875*tp,5.335*tp),transformation=sc.r90)
        elems += spira.SRef(sc.ls_conn_M4M5M6M7(),midpoint=(8.665*tp,2.115*tp),transformation=sc.m90)
        return elems

class M5M6_connections(spira.Cell):
    __name_prefix__ = "M5M6_connections"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(9.415*tp,6.415*tp),alias="via3")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.4025*tp,2.105*tp),alias="via1")
        elems += spira.SRef(sc.ls_conn_M5M6(),midpoint=(4.4125*tp,4.715*tp),alias="via2")
        return elems

class biasing(spira.Cell):
    __name_prefix__ = "biasing"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_ib_063(),midpoint=(6.36*tp,0.445*tp),alias="bias7")
        elems += spira.SRef(sc.ls_ib_113(),midpoint=(2.14*tp,0.4375*tp),transformation=sc.r90,alias="bias2")
        elems += spira.SRef(sc.ls_ib_113(),midpoint=(5.425*tp,6.0525*tp),transformation=sc.r90,alias="bias6")
        elems += spira.SRef(sc.ls_ib_128(),midpoint=(2.2*tp,4.4525*tp),transformation=sc.r90,alias="bias3")
        elems += spira.SRef(sc.ls_ib_131(),midpoint=(2.24*tp,2.4375*tp),transformation=sc.r90,alias="bias1")
        elems += spira.SRef(sc.ls_ib_131(),midpoint=(9.14*tp,4.4375*tp),transformation=sc.r90,alias="bias5")
        elems += spira.SRef(sc.ls_ib_179(),midpoint=(2.07*tp,3.4325*tp),transformation=sc.r90,alias="bias4")
        elems += spira.SRef(sc.ls_ib_214(),midpoint=(6.705*tp,0.825*tp),alias="bias8")
        return elems

class junctions(spira.Cell):
    __name_prefix__ = "junctions"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_jj_088_sg(),midpoint=(7.5*tp,5.46*tp),alias="J9")
        elems += spira.SRef(sc.ls_jj_088_sg(),midpoint=(2.5*tp,1.51*tp),transformation=sc.r180,alias="J1")
        elems += spira.SRef(sc.ls_jj_090_sg(),midpoint=(2.485*tp,4.525*tp),transformation=sc.r270,alias="J6")
        elems += spira.SRef(sc.ls_jj_113_s(),midpoint=(4.49*tp,2.555*tp),transformation=sc.r90,alias="J4")
        elems += spira.SRef(sc.ls_jj_113_s(),midpoint=(4.49*tp,4.445*tp),transformation=sc.r90,alias="J12")
        elems += spira.SRef(sc.ls_jj_126_sg(),midpoint=(6.02*tp,3.48*tp),alias="J14")
        elems += spira.SRef(sc.ls_jj_132_sg(),midpoint=(3.875*tp,4.81*tp),transformation=sc.r90,alias="J11")
        elems += spira.SRef(sc.ls_jj_132_sg(),midpoint=(4.5*tp,1.5*tp),transformation=sc.r90,alias="J3")
        elems += spira.SRef(sc.ls_jj_150_sg(),midpoint=(3*tp,3.51*tp),alias="J7")
        elems += spira.SRef(sc.ls_jj_153_s(),midpoint=(5.46*tp,2.86*tp),transformation=sc.r90,alias="J5")
        elems += spira.SRef(sc.ls_jj_153_s(),midpoint=(5.46*tp,4.14*tp),transformation=sc.r90,alias="J13")
        elems += spira.SRef(sc.ls_jj_176_sg(),midpoint=(3.5*tp,1.5*tp),alias="J2")
        elems += spira.SRef(sc.ls_jj_176_sg(),midpoint=(6.5*tp,5.5*tp),transformation=sc.r180,alias="J10")
        elems += spira.SRef(sc.ls_jj_176_sg(),midpoint=(4.45*tp,3.5*tp),transformation=sc.r270,alias="J8")
        elems += spira.SRef(sc.ls_jj_204_sg(),midpoint=(7.5*tp,3.48*tp),alias="J15")
        elems += spira.SRef(sc.ls_jj_227_sg(),midpoint=(7.5*tp,2.5*tp),alias="J16")
        return elems

class resistors(spira.Cell):
    __name_prefix__ = "resistors"
    def create_elements(self, elems):
        elems += spira.SRef(sc.ls_res_1p36(),midpoint=(8.01*tp,1.5*tp),transformation=sc.r90,alias='R1')
        return elems

class trackblocks(spira.Cell):
    __name_prefix__ = "trackblocks"
    def create_elements(self, elems):
        T = spira.Rotation(180)
        sys.stdout.write("Adding trackblocks.\n")
        for y in range(0, 7):
            for x in range(0, 10):
                if (x in [1,8] and y in [1,5]):
                    elems += spira.SRef(sc.ls_tr_PTLconnection(),midpoint=(0+x*tp,0+y*tp))
                else:
                    elems += spira.SRef(sc.ls_tr_u_M4(),midpoint=(0+x*tp,0+y*tp))
                    elems += spira.SRef(sc.ls_tr_M7(),midpoint=(0+x*tp,0+y*tp))
        return elems

sys.stdout.write("Adjusting settings.\n")
F = RDD.FILTERS.OUTPUT.PORTS
F['cell_ports'] = False
F['edge_ports'] = False
F['contact_ports'] = False
F = RDD.FILTERS.PCELL.DEVICE
F['boolean'] = True
F['contact_attach'] = True
F = RDD.FILTERS.PCELL.CIRCUIT
F['boolean'] = False

D = PCELL()
sys.stdout.write("Writing output.\n")
D.gdsii_output(os.path.splitext(__file__)[0])