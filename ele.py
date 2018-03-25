#!/usr/bin/python
#Filename: ele.py
#Function that proceed recognising element
import sys
def element_reg(z):
	if z==1:
		return 'H'
	elif z==2:
		return 'He'
	elif z==3:
                return 'Li'
        elif z==4:
                return 'Be'
        elif z==5:
                return 'B'
        elif z==6:
                return 'C'
        elif z==7:
                return 'N'
        elif z==8:
                return 'O'
        elif z==9:
                return 'F'
        elif z==10:
                return 'Ne'
        elif z==11:
                return 'Na'
        elif z==12:
                return 'Mg'
        elif z==13:
                return 'Al'
        elif z==14:
                return 'Si'
        elif z==15:
                return 'P'
        elif z==16:
                return 'S'
        elif z==17:
                return 'Cl'
        elif z==18:
                return 'Ar'
        elif z==19:
                return 'K'
        elif z==20:
                return 'Ca'
        elif z==21:
                return 'Sc'
        elif z==22:
                return 'Ti'
        elif z==23:
                return 'V'
        elif z==24:
                return 'Cr'
        elif z==25:
                return 'Mn'
        elif z==26:
                return 'Fe'
        elif z==27:
                return 'Co'
        elif z==28:
                return 'Ni'
        elif z==29:
                return 'Cu'
        elif z==30:
                return 'Zn'
        elif z==31:
                return 'Ga'
        elif z==32:
                return 'Ge'
        elif z==33:
                return 'As'
        elif z==34:
                return 'Se'
        elif z==35:
                return 'Br'
        elif z==36:
                return 'Kr'
        elif z==37:
                return 'Rb'
        elif z==38:
                return 'Sr'
        elif z==39:
                return 'Y'
        elif z==40:
                return 'Zr'
        elif z==41:
                return 'Nb'
        elif z==42:
                return 'Mo'
        elif z==43:
                return 'Tc'
        elif z==44:
                return 'Ru'
        elif z==45:
                return 'Rh'
        elif z==46:
                return 'Pd'
        elif z==47:
                return 'Ag'
        elif z==48:
                return 'Cd'
        elif z==49:
                return 'In'
        elif z==50:
                return 'Sn'
        elif z==51:
                return 'Sb'
        elif z==52:
                return 'Te'
        elif z==53:
                return 'I'
        elif z==54:
                return 'Xe'
        elif z==55:
                return 'Cs'
        elif z==56:
                return 'Ba'
        elif z==57:
                return 'La'
        elif z==58:
                return 'Ce'
        elif z==59:
                return 'Pr'
        elif z==60:
                return 'Nd'
        elif z==61:
                return 'Pm'
        elif z==62:
                return 'Sm'
        elif z==63:
                return 'Eu'
        elif z==64:
                return 'Gd'
        elif z==65:
                return 'Tb'
        elif z==66:
                return 'Dy'
        elif z==67:
                return 'Ho'
        elif z==68:
                return 'Er'
        elif z==69:
                return 'Tm'
        elif z==70:
                return 'Yb'
        elif z==71:
                return 'Lu'
        elif z==72:
                return 'Hf'
        elif z==73:
                return 'Ta'
        elif z==74:
                return 'W'
        elif z==75:
                return 'Re'
        elif z==76:
                return 'Os'
        elif z==77:
                return 'Ir'
        elif z==78:
                return 'Pt'
        elif z==79:
                return 'Au'
        elif z==80:
                return 'Hg'
        elif z==81:
                return 'Tl'
        elif z==82:
                return 'Pb'
        elif z==83:
                return 'Bi'
        elif z==84:
                return 'Po'
        elif z==85:
                return 'At'
        elif z==86:
                return 'Rn'
        elif z==87:
                return 'Fr'
        elif z==88:
                return 'Ra'
        elif z==89:
                return 'Ac'
        elif z==90:
                return 'Th'
        elif z==91:
                return 'Pa'
        elif z==92:
                return 'U'
        elif z==93:
                return 'Np'
        elif z==94:
                return 'Pu'
        elif z==95:
                return 'Am'
        elif z==96:
                return 'Cm'
        elif z==97:
                return 'Bk'
        elif z==98:
                return 'Cf'
        elif z==99:
                return 'Es'
        elif z==100:
                return 'Fm'
        elif z==101:
                return 'Md'
        elif z==102:
                return 'No'
        elif z==103:
                return 'Lr'
        elif z==104:
                return 'Rf'
        elif z==105:
                return 'Db'
        elif z==106:
                return 'Sg'
        elif z==107:
                return 'Bh'
        elif z==108:
                return 'Hs'
        elif z==109:
                return 'Mt'
        elif z==110:
                return 'Ds'
        elif z==111:
                return 'Rg'
	else:
		print "Atomic number not recognised! Error exit."
		sys.exit(1)
def atomicnumber_reg(S):
	if S=='H' or S=='h':
		return 1
	elif S=='He' or S=='HE' or S=='he':
		return 2
	elif S=='Li' or S=='LI' or S=='li':
		return 3
        elif S=='Be' or S=='BE' or S=='be':
                return 4
        elif S=='B' or S=='b':
                return 5
        elif S=='C' or S=='c':
                return 6
        elif S=='N' or S=='n':
                return 7
        elif S=='O' or S=='o':
                return 8
        elif S=='F' or S=='f':
                return 9
        elif S=='Ne' or S=='NE' or S=='ne':
                return 10
        elif S=='Na' or S=='NA' or S=='na':
                return 11
        elif S=='Mg' or S=='MG' or S=='mg':
                return 12
        elif S=='Al' or S=='AL' or S=='al':
                return 13
        elif S=='Si' or S=='SI' or S=='si':
                return 14
        elif S=='P' or S=='p':
                return 15
        elif S=='S' or S=='s':
                return 16
        elif S=='Cl' or S=='CL' or S=='cl':
                return 17
        elif S=='Ar' or S=='AR' or S=='ar':
                return 18
        elif S=='k' or S=='K':
                return 19
        elif S=='Ca' or S=='CA' or S=='ca':
                return 20
        elif S=='Sc' or S=='SC' or S=='sc':
                return 21
        elif S=='TI' or S=='Ti' or S=='ti':
                return 22
        elif S=='v' or S=='V':
                return 23
        elif S=='Cr' or S=='CR' or S=='cr':
                return 24
        elif S=='MN' or S=='Mn' or S=='mn':
                return 25
        elif S=='FE' or S=='Fe' or S=='fe':
                return 26
        elif S=='Co' or S=='CO' or S=='co':
                return 27
        elif S=='NI' or S=='Ni' or S=='ni':
                return 28
        elif S=='Cu' or S=='CU' or S=='cu':
                return 29
        elif S=='Zn' or S=='ZN' or S=='zn':
                return 30
        elif S=='Ga' or S=='GA' or S=='ga':
                return 31
        elif S=='Ge' or S=='GE' or S=='ge':
                return 32
        elif S=='As' or S=='AS' or S=='as':
                return 33
        elif S=='Se' or S=='SE' or S=='se':
                return 34
        elif S=='Br' or S=='BR' or S=='br':
                return 35
        elif S=='KR' or S=='Kr' or S=='kr':
                return 36
        elif S=='RB' or S=='Rb' or S=='rb':
                return 37
        elif S=='SR' or S=='Sr' or S=='sr':
                return 38
        elif S=='Y' or S=='y':
                return 39
        elif S=='Zr' or S=='ZR' or S=='zr':
                return 40
        elif S=='Nb' or S=='NB' or S=='nb':
                return 41
        elif S=='MO' or S=='Mo' or S=='mo':
                return 42
        elif S=='Tc' or S=='TC' or S=='tc':
                return 43
        elif S=='Ru' or S=='RU' or S=='ru':
                return 44
        elif S=='Rh' or S=='RH' or S=='rh':
                return 45
        elif S=='PD' or S=='Pd' or S=='pd':
                return 46
        elif S=='AG' or S=='Ag' or S=='ag':
                return 47
        elif S=='Cd' or S=='CD' or S=='cd':
                return 48
        elif S=='In' or S=='IN' or S=='in':
                return 49
        elif S=='SN' or S=='Sn' or S=='sn':
                return 50
        elif S=='SB' or S=='Sb' or S=='sb':
                return 51
        elif S=='Te' or S=='TE' or S=='te':
                return 52
        elif S=='I' or S=='i':
                return 53
        elif S=='XE' or S=='Xe' or S=='xe':
                return 54
        elif S=='CS' or S=='Cs' or S=='cs':
                return 55
        elif S=='Ba' or S=='BA' or S=='ba':
                return 56
        elif S=='LA' or S=='La' or S=='la':
                return 57
        elif S=='CE' or S=='Ce' or S=='ce':
                return 58
        elif S=='PR' or S=='Pr' or S=='pr':
                return 59
        elif S=='Nd' or S=='ND' or S=='nd':
                return 60
        elif S=='Pm' or S=='PM' or S=='pm':
                return 61
        elif S=='Sm' or S=='SM' or S=='sm':
                return 62
        elif S=='EU' or S=='Eu' or S=='eu':
                return 63
        elif S=='Gd' or S=='GD' or S=='gd':
                return 64
        elif S=='Tb' or S=='TB' or S=='tb':
                return 65
        elif S=='Dy' or S=='DY' or S=='dy':
                return 66
        elif S=='HO' or S=='Ho' or S=='ho':
                return 67
        elif S=='ER' or S=='Er' or S=='er':
                return 68
        elif S=='TM' or S=='Tm' or S=='tm':
                return 69
        elif S=='YB' or S=='Yb' or S=='yb':
                return 70
        elif S=='Lu' or S=='LU' or S=='lu':
                return 71
        elif S=='HF' or S=='Hf' or S=='hf':
                return 72
        elif S=='TA' or S=='Ta' or S=='ta':
                return 73
        elif S=='w' or S=='W':
                return 74
        elif S=='RE' or S=='Re' or S=='re':
                return 75
        elif S=='Os' or S=='OS' or S=='os':
                return 76
        elif S=='Ir' or S=='IR' or S=='ir':
                return 77
        elif S=='PT' or S=='Pt' or S=='pt':
                return 78
        elif S=='AU' or S=='Au' or S=='au':
                return 79
        elif S=='HG' or S=='Hg' or S=='hg':
                return 80
        elif S=='TL' or S=='Tl' or S=='tl':
                return 81
        elif S=='Pb' or S=='PB' or S=='pb':
                return 82
        elif S=='Bi' or S=='BI' or S=='bi':
                return 83
        elif S=='Po' or S=='PO' or S=='po':
                return 84
        elif S=='At' or S=='AT' or S=='at':
                return 85
        elif S=='RN' or S=='Rn' or S=='rn':
                return 86
        elif S=='FR' or S=='Fr' or S=='fr':
                return 87
        elif S=='RA' or S=='Ra' or S=='ra':
                return 88
        elif S=='Ac' or S=='AC' or S=='ac':
                return 89
        elif S=='TH' or S=='Th' or S=='th':
                return 90
        elif S=='Pa' or S=='PA' or S=='pa':
                return 91
        elif S=='U' or S=='u':
                return 92
        elif S=='NP' or S=='Np' or S=='np':
                return 93
        elif S=='PU' or S=='Pu' or S=='pu':
                return 94
        elif S=='Am' or S=='AM' or S=='am':
                return 95
        elif S=='Cm' or S=='CM' or S=='cm':
                return 96
        elif S=='Bk' or S=='BK' or S=='bk':
                return 97
        elif S=='CF' or S=='Cf' or S=='cf':
                return 98
        elif S=='ES' or S=='Es' or S=='es':
                return 99
        elif S=='FM' or S=='Fm' or S=='fm':
                return 100
        elif S=='MD' or S=='Md' or S=='md':
                return 101
        elif S=='No' or S=='NO' or S=='no':
                return 102
        elif S=='LR' or S=='Lr' or S=='lr':
                return 103
        elif S=='Rf' or S=='RF' or S=='rf':
                return 104
        elif S=='DB' or S=='Db' or S=='db':
                return 105
        elif S=='SG' or S=='Sg' or S=='sg':
                return 106
        elif S=='BH' or S=='Bh' or S=='bh':
                return 107
        elif S=='Hs' or S=='HS' or S=='hs':
                return 108
        elif S=='Mt' or S=='MT' or S=='mt':
                return 109
        elif S=='Ds' or S=='DS' or S=='ds':
                return 110
        else:
                return False
def periodnumber_reg(z):
	if z>0 and z<3:
		return 1
	elif z>2 and z<11:
		return 2
	elif z>10 and z<19:
		return 3
	elif z>18 and z<37:
		return 4
	elif z>36 and z<55:
		return 5
	elif z>54 and z<87:
		return 6
	elif z>86 and z<119:
		return 7
	else:
		print "Atomic number not recognised! Error exit."
		sys.exit(1)
