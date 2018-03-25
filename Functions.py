#!/usr/bin/python
#All the functios that have been used in main module(auto module).
import os
#Cfour output function
def Cfour_output(Cfourbasis,f):
	'''Give Cfour format output.

Put Cfour basis set format into a file.'''
	NumofAM=0
	StrofAM=''
	StrofContracted_AM=''
	StrofComplete_AM=''
	COE_PRECISION_CTRL=True
	if Cfourbasis.LT_EXP_COE_S:
		NumofAM+=1
		AM='0'
		AM=AM.rjust(5)
		StrofAM+=AM
		Num=len(Cfourbasis.LT_EXP_COE_S)
		Num=str(Num)
		Num=Num.rjust(5)
		StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_S[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
	if Cfourbasis.LT_EXP_COE_P:
		NumofAM+=1
                AM='1'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_P)
		Num=str(Num)
                Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_P[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_D:
                NumofAM+=1
	        AM='2'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_D)
		Num=str(Num)
                Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_D[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_F:
                NumofAM+=1
                AM='3'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_F)
		Num=str(Num)
                Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_F[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
	if Cfourbasis.LT_EXP_COE_G:
                NumofAM+=1
                AM='4'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_G)
		Num=str(Num)
                Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_G[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_H:
                NumofAM+=1
                AM='5'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_H)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_H[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_I:
                NumofAM+=1
                AM='6'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_I)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_I[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_K:
                NumofAM+=1
                AM='7'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_K)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_K[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_L:
                NumofAM+=1
                AM='8'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_L)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_L[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_M:
                NumofAM+=1
                AM='9'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_M)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
                NumC=len(Cfourbasis.LT_COE_M[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
        if Cfourbasis.LT_EXP_COE_N:
                NumofAM+=1
                AM='10'
                AM=AM.rjust(5)
                StrofAM+=AM
                Num=len(Cfourbasis.LT_EXP_COE_N)
                Num=str(Num)
		Num=Num.rjust(5)
                StrofComplete_AM+=Num
		NumC=len(Cfourbasis.LT_COE_N[0])
                NumC=str(NumC)
                NumC=NumC.rjust(5)
                StrofContracted_AM+=NumC
	f.write(Cfourbasis.element_name+':Define your basis name here\n')
	f.write(Cfourbasis.element_name+':Please add your comment here\n')
        f.write('\n')
	NumofAM=str(NumofAM)
	NumofAM=NumofAM.rjust(3)
	f.write(NumofAM+'\n')
	f.write(StrofAM+'\n')
	f.write(StrofContracted_AM+'\n')
	f.write(StrofComplete_AM+'\n')
	COE_PRECISION_CTRL=Cfour_COE_SCAN(Cfourbasis)
	#S
	length=len(Cfourbasis.LT_EXP_S)
	for i,item in enumerate(Cfourbasis.LT_EXP_S):
                if i%5==0:
                        f.write('\n')
		f.write("%16.6f"%item)
		if i+1==length:
			f.write('\n')
	f.write('\n')
	if Cfourbasis.LT_COE_S:
		if COE_PRECISION_CTRL==False:
	        	for item in Cfourbasis.LT_COE_S:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
		else:	
			for item in Cfourbasis.LT_COE_S:
				for flag in item:
					f.write("%10.7f"%flag+' ')
				f.write('\n')
        #P
        length=len(Cfourbasis.LT_EXP_P)
        for i,item in enumerate(Cfourbasis.LT_EXP_P):
                if i%5==0:
                        f.write('\n')
		f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_P:
		if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_P:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_P:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #D
        length=len(Cfourbasis.LT_EXP_D)
        for i,item in enumerate(Cfourbasis.LT_EXP_D):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_D:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_D:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_D:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
               	 		f.write('\n')
        #F
        length=len(Cfourbasis.LT_EXP_F)
        for i,item in enumerate(Cfourbasis.LT_EXP_F):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_F:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_F:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_F:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #G
        length=len(Cfourbasis.LT_EXP_G)
        for i,item in enumerate(Cfourbasis.LT_EXP_G):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_G:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_G:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_G:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #H
        length=len(Cfourbasis.LT_EXP_H)
        for i,item in enumerate(Cfourbasis.LT_EXP_H):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_H:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_H:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_H:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #I
        length=len(Cfourbasis.LT_EXP_I)
        for i,item in enumerate(Cfourbasis.LT_EXP_I):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_I:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_I:
                        	for flag in item:
                        	        f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_I:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #K
        length=len(Cfourbasis.LT_EXP_K)
        for i,item in enumerate(Cfourbasis.LT_EXP_K):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_K:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_K:
                        	for flag in item:
                        	        f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_K:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #L
        length=len(Cfourbasis.LT_EXP_L)
        for i,item in enumerate(Cfourbasis.LT_EXP_L):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_L:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_L:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_L:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #M
        length=len(Cfourbasis.LT_EXP_M)
        for i,item in enumerate(Cfourbasis.LT_EXP_M):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_M:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_M:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_M:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
        #N
        length=len(Cfourbasis.LT_EXP_N)
        for i,item in enumerate(Cfourbasis.LT_EXP_N):
                if i%5==0:
                        f.write('\n')
                f.write("%16.6f"%item)
                if i+1==length:
                        f.write('\n')
        f.write('\n')
	if Cfourbasis.LT_COE_N:
                if COE_PRECISION_CTRL==False:
                	for item in Cfourbasis.LT_COE_N:
                        	for flag in item:
                                	f.write("%13.6E"%flag+'     ')
                        	f.write('\n')
        	else:
        		for item in Cfourbasis.LT_COE_N:
                		for flag in item:
                			f.write("%10.7f"%flag+' ')
                		f.write('\n')
		#Pseodopotential output

#Dirac output function
def Dirac_output(Dbasis,f):
	StrofAM=[]
	COE_PRECISION_CTRL=True
	f.write('a %s'%Dbasis.Z+'\n')
	f.write('$ Add your description here\n')
	f.write('$ Add your description here\n')
	COE_PRECISION_CTRL=Dirac_COE_SCAN(Dbasis)
	#print "HERE:"
	#print Dirac_COE_SCAN(Dbasis)
	Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_S,Dbasis.LT_EXP_S,Dbasis.LT_COE_S,'S')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_P,Dbasis.LT_EXP_P,Dbasis.LT_COE_P,'P')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_D,Dbasis.LT_EXP_D,Dbasis.LT_COE_D,'D')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_F,Dbasis.LT_EXP_F,Dbasis.LT_COE_F,'F')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_G,Dbasis.LT_EXP_G,Dbasis.LT_COE_G,'G')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_H,Dbasis.LT_EXP_H,Dbasis.LT_COE_H,'H')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_I,Dbasis.LT_EXP_I,Dbasis.LT_COE_I,'I')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_K,Dbasis.LT_EXP_K,Dbasis.LT_COE_K,'K')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_L,Dbasis.LT_EXP_L,Dbasis.LT_COE_L,'L')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_M,Dbasis.LT_EXP_M,Dbasis.LT_COE_M,'M')
        Dirac_L_output_AG(f,COE_PRECISION_CTRL,Dbasis.LT_EXP_COE_N,Dbasis.LT_EXP_N,Dbasis.LT_COE_N,'N')
#Dirac AM output
def Dirac_L_output_AG(f,COE_PRECISION_CTRL,basislt_EXP_COE,basislt_EXP,basislt_COE,AM):
        if basislt_EXP_COE:
                length1=len(basislt_EXP)
                length1=str(length1)
                length1=length1.rjust(5)
		length2=0
#                length2=len(basislt_COE[0])
                length2=str(length2)
                length2=length2.rjust(5)
                StrofAM=length1+length2
                f.write('$ ')
		f.write(AM)
		f.write('-TYPE FUNCTIONS\n')
                f.write(StrofAM+'    0')
                length3=len(basislt_EXP)
                if COE_PRECISION_CTRL==True:
                        for i in range(length3):
                                f.write('\n')
                                f.write("   %15f"%basislt_EXP[i])
#                                for j,item in enumerate(basislt_COE[i]):
#                                        if j==5:
#                                                f.write('\n   ')
#                                        elif (j-5)%5==0 and j!=0:
#                                                f.write('\n   ')
#                                        f.write("%12.8f"%item)
#				
                else:
                        for i in range(length3):
                                f.write('\n')
                                f.write("%15E"%basislt_EXP[i])
#                                for j,item in enumerate(basislt_COE[i]):
#                                        if j==5:
#                                                f.write('\n               ')
#                                        elif (j-5)%5==0 and j!=0:
#                                                f.write('\n               ')
#                                        f.write("%12.4E"%item)
                f.write('\n')

#Molpro output function
def Molpro_R_output(Mbasis,f):
        f.write('Define your basis set name here.\n')
	#transpose LT_COE
	Mbasis.LT_COE_S=map(list,zip(*Mbasis.LT_COE_S))
        Mbasis.LT_COE_P=map(list,zip(*Mbasis.LT_COE_P))
        Mbasis.LT_COE_D=map(list,zip(*Mbasis.LT_COE_D))
        Mbasis.LT_COE_F=map(list,zip(*Mbasis.LT_COE_F))
        Mbasis.LT_COE_G=map(list,zip(*Mbasis.LT_COE_G))
        Mbasis.LT_COE_H=map(list,zip(*Mbasis.LT_COE_H))
        Mbasis.LT_COE_I=map(list,zip(*Mbasis.LT_COE_I))
        Mbasis.LT_COE_K=map(list,zip(*Mbasis.LT_COE_K))
        Mbasis.LT_COE_L=map(list,zip(*Mbasis.LT_COE_L))
        Mbasis.LT_COE_M=map(list,zip(*Mbasis.LT_COE_M))
        Mbasis.LT_COE_N=map(list,zip(*Mbasis.LT_COE_N))
	Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_S,Mbasis.LT_EXP_S,Mbasis.LT_COE_S,'s')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_P,Mbasis.LT_EXP_P,Mbasis.LT_COE_P,'p')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_D,Mbasis.LT_EXP_D,Mbasis.LT_COE_D,'d')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_F,Mbasis.LT_EXP_F,Mbasis.LT_COE_F,'f')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_G,Mbasis.LT_EXP_G,Mbasis.LT_COE_G,'g')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_H,Mbasis.LT_EXP_H,Mbasis.LT_COE_H,'h')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_I,Mbasis.LT_EXP_I,Mbasis.LT_COE_I,'i')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_K,Mbasis.LT_EXP_K,Mbasis.LT_COE_K,'k')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_L,Mbasis.LT_EXP_L,Mbasis.LT_COE_L,'l')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_M,Mbasis.LT_EXP_M,Mbasis.LT_COE_M,'m')
        Molpro_R_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_N,Mbasis.LT_EXP_N,Mbasis.LT_COE_N,'n')
#Molpro regular basis output AG analog
def Molpro_R_output_AG(f,Mbasis,basislt_EXP_COE,basislt_EXP,basislt_COE,AM):
	if basislt_EXP_COE:
                length1=len(basislt_COE)
                i=0
                f.write('\n')
                f.write(AM+',')
                f.write(Mbasis.element_name)
                for item in basislt_EXP:
                        f.write(',')
			item_tmp=str(item)
                        f.write(item_tmp)
                f.write('\n')
                while i<length1:
			count_1=0
                        f.write('c,')
			for item in basislt_COE[i]:
				if item==1:
					count_1+=1
			if count_1==1:
				for j,item in enumerate(basislt_COE[i]):	
					if item==1:
						item_tmp=str(item)
						j+=1
						j=str(j)
						f.write(j+'.'+j+','+item_tmp)
						break
				f.write('\n')
			else:
				f.write('1.'+str(len(filter(float,basislt_COE[i]))))
				for item in basislt_COE[i]:
					if item==0:
						break
					f.write(',')
					item_tmp=str(item)
					f.write(item_tmp)
				f.write('\n')
			i+=1


#Molpro lib format output
def Molpro_L_output(Mbasis,f,gbasis_type_name):
	gbasis_type_name_lt=gbasis_type_name.split('.')
	gbasis_type_name=gbasis_type_name_lt[0]
	print 'For'+' '+Mbasis.element_name+':'
	Ctrl=raw_input('Do you want the program to define your basis set name?(Only if you have given the right input name)\n 1. YES  2. NO \n')
        basis_type=''
        basis_type_abbre=''
	if Ctrl=='1' or Ctrl=='YES' or Ctrl=='yes': 
		basis_type_list=gbasis_type_name.split('-')
		for i in range(len(basis_type_list)):
			if basis_type_list[i]=='AUG':
				basis_type_list[i]='aug'
				basis_type_abbre='A'
			if basis_type_list[i]=='CC':
				basis_type_list[i]='cc'
			if 'Z' in basis_type_list[i]:
				basis_type_list[i]=basis_type_list[i].lower()
				if 'c' in basis_type_list[i]:
					basis_type_list_half1=basis_type_list[i][-4:]
					basis_type_list_half1=basis_type_list_half1.upper()
					basis_type_list_half2=basis_type_list[i][:-4]
					basis_type_list[i]=basis_type_list_half2+basis_type_list_half1
					basis_type_abbre=basis_type_abbre+'WC'
				else:
					basis_type_list_half1=basis_type_list[i][-3:]
					basis_type_list_half1=basis_type_list_half1.upper()
					basis_type_list_half2=basis_type_list[i][:-3]
					basis_type_list[i]=basis_type_list_half2+basis_type_list_half1
					basis_type_abbre=basis_type_abbre+basis_type_list_half1
			if 'PP' in basis_type_list[i]:
				basis_type_abbre=basis_type_abbre+'-PP'
			if 'DK' in basis_type_list[i]:
				basis_type_abbre=basis_type_abbre+'-DK'
			if 'F12' in basis_type_list[i]:
				basis_type_abbre=basis_type_abbre+'-F12'
		for item in basis_type_list:
			basis_type=basis_type+item+'-'
	elif Ctrl=='2' or Ctrl=='NO' or Ctrl=='no':
		basis_type=gbasis_type_name
		basis_type_abbre='Undefined'
	else:
		print 'Please give the right number, error exit'
		sys.exit(1)
	#Transpose the matrix
        Mbasis.LT_COE_S=map(list,zip(*Mbasis.LT_COE_S))
        Mbasis.LT_COE_P=map(list,zip(*Mbasis.LT_COE_P))
        Mbasis.LT_COE_D=map(list,zip(*Mbasis.LT_COE_D))
        Mbasis.LT_COE_F=map(list,zip(*Mbasis.LT_COE_F))
        Mbasis.LT_COE_G=map(list,zip(*Mbasis.LT_COE_G))
        Mbasis.LT_COE_H=map(list,zip(*Mbasis.LT_COE_H))
        Mbasis.LT_COE_I=map(list,zip(*Mbasis.LT_COE_I))
        Mbasis.LT_COE_K=map(list,zip(*Mbasis.LT_COE_K))
        Mbasis.LT_COE_L=map(list,zip(*Mbasis.LT_COE_L))
        Mbasis.LT_COE_M=map(list,zip(*Mbasis.LT_COE_M))
        Mbasis.LT_COE_N=map(list,zip(*Mbasis.LT_COE_N))
	#Start to output
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_S,Mbasis.LT_COE_S,Mbasis.LT_EXP_S,'s',basis_type,basis_type_abbre)
	Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_P,Mbasis.LT_COE_P,Mbasis.LT_EXP_P,'p',basis_type,basis_type_abbre)
	Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_D,Mbasis.LT_COE_D,Mbasis.LT_EXP_D,'d',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_F,Mbasis.LT_COE_F,Mbasis.LT_EXP_F,'f',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_G,Mbasis.LT_COE_G,Mbasis.LT_EXP_G,'g',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_H,Mbasis.LT_COE_H,Mbasis.LT_EXP_H,'h',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_I,Mbasis.LT_COE_I,Mbasis.LT_EXP_I,'i',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_K,Mbasis.LT_COE_K,Mbasis.LT_EXP_K,'k',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_L,Mbasis.LT_COE_L,Mbasis.LT_EXP_L,'l',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_M,Mbasis.LT_COE_M,Mbasis.LT_EXP_M,'m',basis_type,basis_type_abbre)
        Molpro_L_output_AG(f,Mbasis,Mbasis.LT_EXP_COE_N,Mbasis.LT_COE_N,Mbasis.LT_EXP_N,'n',basis_type,basis_type_abbre)
#AG analog function
def Molpro_L_output_AG(f,Mbasis,basislt_COE_EXP,basislt_COE,basislt_EXP,AM,basis_type,basis_type_abbre):
        if basislt_COE_EXP:
                length1=len(basislt_COE)
                f.write(Mbasis.element_name+'  ')
                f.write(AM+' ')
                f.write(basis_type[:-1]+' ')
                f.write(basis_type_abbre+'   :   ')
                f.write(str(len(basislt_EXP))+'   ')
                f.write(str(len(basislt_COE))+'  ')
                i=0
                while i<length1:
                        count_1=0
                        for item in basislt_COE[i]:
                                if item==1:
                                        count_1+=1
                        if count_1==1:
                                for j,item in enumerate(basislt_COE[i]):
                                        if item==1:
                                                j+=1
                                                j=str(j)
                                                f.write(j+'.'+j+' ')
                        else:
                                bfr=len(filter(float,basislt_COE[i]))
                                bfrs=str(bfr)
                                f.write('1.'+bfrs+' ')
                        i+=1
                f.write('\n')
                f.write(basis_type[:-1]+'\n')
                j=0
                for item in basislt_EXP:
                        if item!=0:
                                item_tmp=str('%16.7E'%item)
                                f.write(item_tmp+' ')
                                j+=1
                        if j%5==0 and j!=0:
				if j==len(basislt_EXP)+len(basislt_COE):
					break
				else:
                                	f.write('\n')
		len_of_COE=0
		for item in basislt_COE:
                        for flag in item:
                                if flag!=0:
                			len_of_COE=len_of_COE+1
                for item in basislt_COE:
                        for flag in item:
                                if flag!=0:
                                        flag_tmp=str('%16.7E'%flag)
                                        f.write(flag_tmp+' ')
                                        j+=1
                                	if j%5==0 and j!=0:
						if j==len(basislt_EXP)+len_of_COE:
							break
                                        	else:
							f.write('\n')
                f.write('\n')
#Txt type output
def Txt_output(Tbasis,f):
        Strof_Contactiontype_AM=["",""]
        COE_PRECISION_CTRL=True
        f.write('%s:'%Tbasis.element_name+'Define your basis set type name here:')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_S,Tbasis.LT_COE_S,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'s ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_P,Tbasis.LT_COE_P,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'p ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_D,Tbasis.LT_COE_D,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'d ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_F,Tbasis.LT_COE_F,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'f ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_G,Tbasis.LT_COE_G,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'g ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_H,Tbasis.LT_COE_H,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'h ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_I,Tbasis.LT_COE_I,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'i ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_K,Tbasis.LT_COE_K,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'k ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_L,Tbasis.LT_COE_L,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'l ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_M,Tbasis.LT_COE_M,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'m ')
        Strof_Contactiontype_AM=Txt_output_Title_AM(Tbasis.LT_EXP_COE_N,Tbasis.LT_COE_N,Strof_Contactiontype_AM[0],Strof_Contactiontype_AM[1],'n ')
	f.write("( %s) -> "%Strof_Contactiontype_AM[0])
	f.write("[ %s]\n"%Strof_Contactiontype_AM[1])
	if Tbasis.LT_EXP_COE_S:
		AG_number=0
	if Tbasis.LT_EXP_COE_P:
		AG_number=1
	if Tbasis.LT_EXP_COE_D:
		AG_number=2
	if Tbasis.LT_EXP_COE_F:
                AG_number=3
	if Tbasis.LT_EXP_COE_G:
                AG_number=4
	if Tbasis.LT_EXP_COE_H:
                AG_number=5
	if Tbasis.LT_EXP_COE_I:
                AG_number=6
	if Tbasis.LT_EXP_COE_K:
                AG_number=7
	if Tbasis.LT_EXP_COE_L:
                AG_number=8
	if Tbasis.LT_EXP_COE_M:
                AG_number=9
	if Tbasis.LT_EXP_COE_N:
                AG_number=10
	f.write(str(AG_number)+'\n')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_S,Tbasis.LT_EXP_S,Tbasis.LT_COE_S,'S')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_P,Tbasis.LT_EXP_P,Tbasis.LT_COE_P,'P')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_D,Tbasis.LT_EXP_D,Tbasis.LT_COE_D,'D')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_F,Tbasis.LT_EXP_F,Tbasis.LT_COE_F,'F')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_G,Tbasis.LT_EXP_G,Tbasis.LT_COE_G,'G')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_H,Tbasis.LT_EXP_H,Tbasis.LT_COE_H,'H')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_I,Tbasis.LT_EXP_I,Tbasis.LT_COE_I,'I')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_K,Tbasis.LT_EXP_K,Tbasis.LT_COE_K,'K')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_L,Tbasis.LT_EXP_L,Tbasis.LT_COE_L,'L')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_M,Tbasis.LT_EXP_M,Tbasis.LT_COE_M,'M')
        Txt_output_AG(f,COE_PRECISION_CTRL,Tbasis.LT_EXP_COE_N,Tbasis.LT_EXP_N,Tbasis.LT_COE_N,'N')
	f.write('\n')
def Txt_output_Title_AM(basis_EXP_COE,basis_COE,StrofComplete_AM,StrofContracted_AM,AM):
	if basis_EXP_COE:
		StrofAM=[]
                Num=len(basis_EXP_COE)
                Num=str(Num)+AM
		StrofComplete_AM+=Num
		StrofAM.append(StrofComplete_AM)
                NumC=len(basis_COE[0])
                NumC=str(NumC)+AM
		StrofContracted_AM+=NumC
                StrofAM.append(StrofContracted_AM)
		return StrofAM
	else:
		StrofAM=[]
		StrofAM.append(StrofComplete_AM)
		StrofAM.append(StrofContracted_AM)
                return StrofAM
#def Txt_output_AG(f,COE_PRECISION_CTRL,basislt_EXP_COE,basislt_EXP,basislt_COE,AM):
#        if basislt_EXP_COE:
#                length1=len(basislt_EXP)
#                length1=str(length1)
#                length2=len(basislt_COE[0])
#                length2=str(length2)
#                f.write(AM+' '+length1+' '+length2)
#                length3=len(basislt_EXP)
#                if COE_PRECISION_CTRL==True:
#                        for i in range(length3):
#                                f.write('\n')
#                                f.write("%15f"%basislt_EXP[i])
#                                for j,item in enumerate(basislt_COE[i]):
#                                        if j==6:
#                                                f.write('\n   ')
#                                        elif j%7==0 and j!=0:
#                                                f.write('\n   ')
#                                        f.write("%12.8f"%item)
#                else:
#                        for i in range(length3):
#                                f.write('\n')
#                                f.write("%15f"%basislt_EXP[i])
#                                for j,item in enumerate(basislt_COE[i]):
#                                        if j==6:
#                                                f.write('\n   ')
#                                        elif j%7==0 and j!=0:
#                                                f.write('\n   ')
#                                        f.write("%15.7E"%item)
#                f.write('\n')
#Txt output that David wants
def Txt_output_AG(f,COE_PRECISION_CTRL,basislt_EXP_COE,basislt_EXP,basislt_COE,AM):
        if basislt_EXP_COE:
                length1=len(basislt_EXP)
                length1=str(length1)
                length2=len(basislt_COE[0])
                length2=str(length2)
                f.write(AM+' '+length1+' '+length2)
                length3=len(basislt_EXP)
		for i in range(length3):
			f.write('\n')
			f.write("%.6E"%basislt_EXP[i])
			f.write(" ")
			for j,item in enumerate(basislt_COE[i]):
				f.write("%.7E"%item)
				f.write(" ")
                f.write('\n')

#Gaussian output
def Gaussian_output(Gbasis,f):
        str="%-6.2s" % (Gbasis.element_name)
        f.write(str+'0\n')
        Gbasis.Sum_lt()
        Gbasis.Pair_ALL()
        for item in Gbasis.LT_EXP_COE_ALL_PAIR:
                for jtem in item[1:]:
                        f.write("%-4.2s%-4.2s%-4.3s\n" %(item[0],len(jtem),'1.00'))
                        for ktem in jtem:
                                for ltem in ktem:
                                        try:
                                                f.write("% 15.7f        " %ltem)
                                        except TypeError:
                                                print ltem
                                f.write('\n')
        f.write('****\n')
        f.write('\n')

#Gaussian decontracted basis set output
def Gaussian_Decon_output(Gbasis,f):
        str="%-6.2s" % (Gbasis.element_name)
        f.write(str+'0\n')
        #Check and kick out >90% similar functions
        kick_out_lt=[]
        flag=0
        for am,item in zip('SPDFGHIKLMN',Gbasis.LT_EXP_LT):
                for i in range(len(item)-1,-1,-1):
                #for i in range(0,len(item)):
                       for j in range(len(item)-1,-1,-1):
                       #for j in range(0,len(item)):
                                if i!=j and min(abs(item[j]),abs(item[i]))/max(abs(item[j]),abs(item[i]))>0.90:
                                        for ktem in kick_out_lt:
                                                if [am,min(abs(item[j]),abs(item[i]))]==ktem[:2]:
                                                        flag=1
                                        if 0 == flag:
                                                kick_out_lt.append([am,min(abs(item[j]),abs(item[i])),j])
                                        else:
                                                flag=0
        TMP_LT_EXP_LT = Gbasis.LT_EXP_LT
        for item in kick_out_lt:
                for am,jtem in zip('SPDFGHIKLMN',TMP_LT_EXP_LT):
                        if am == item[0]:
                                print ("Omitting the %ith function from angular momentum %s of element %s :  %f" %(item[2],item[0],Gbasis.element_name,item[1]))
                                del jtem[item[2]]
        #write out to basis file
        for am,item in zip('SPDFGHIKLMN',TMP_LT_EXP_LT):
                for jtem in item:
                        f.write("%-4.2s%-4.2s%-4.3s\n" %(am,'1','1.00'))
                        f.write("%15.7f%15.7f\n" %(jtem,1.00000))
        f.write('****\n')
        f.write('\n')

#MOLCAS output
def MOLCAS_output(Gbasis,f):
    f.write('/'+Gbasis.element_name+'.\n'+'Edit additional information here.\n')
    f.write('************************************************************************\n')
    f.write('*Edit additional information here                                      *\n')
    f.write('************************************************************************\n')
    f.write('Options\nOrbitalEnergies\nEndOptions\n')
    Gbasis.Sum_lt()                        
    for item,jtem in zip(Gbasis.LT_EXP_ALL,Gbasis.LT_COE_ALL):
        if len(item) > 1:
            f.write('*  '+item[0].lower() + "-type ANO's, max " + str(len(jtem[1])) + ' functions can be used\n')
            f.write("%5s%5s\n" %(str(len(item)-1),str(len(jtem[1]))))
            for i in range(1,len(item)):
                f.write("%-9s" %(item[i]))
                f.write(' ')
                if i%5==0:
                    f.write('\n')
            f.write('\n')
            for i in range(1,len(jtem)):
                for number in jtem[i]:
                    f.write(" % -.10f" %(number))
                f.write('\n')
            f.write('  0\n')
#To maintain the output precision of Cfour basis set
def Cfour_COE_SCAN(Basis):
	for item in Basis.LT_COE_S:
		for i in item:
			if float("%10.7f"%i)!=i:
				return False
        for item in Basis.LT_COE_P:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_D:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_F:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_G:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_H:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_I:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_K:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_L:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_M:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
        for item in Basis.LT_COE_N:
                for i in item:
                        if float("%10.7f"%i)!=i:
                                return False
	return True

#To maintain the output precision of Dirac basis sets
def Dirac_COE_SCAN(Basis):
        for item in Basis.LT_COE_S:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_P:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_D:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_F:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_G:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_H:
                for i in item:
                	if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_I:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_K:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_L:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_M:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
        for item in Basis.LT_COE_N:
                for i in item:
                        if float("%12.8f"%i)!=i:
                                return False
	return True

def molproregular_basisfile_pre_processor(f_dir):
	f=file(f_dir,'r')
	basename=os.path.basename(f_dir)
	fnew=file(basename+"_TMP",'w')
	line=f.readline()
        while line:
	#	print line
		while line[0]=='!':
			fnew.write(line)
			line=f.readline()
		line_new=line.replace(' ',',')
		line_new=line_new.replace('\t',',')
                line_new=line_new.replace(';',',')
		while line_new.find(',,')!=-1:
			line_new=line_new.replace(',,',',')	
		line_new=line_new.replace(',\n','\n')	
		fnew.write(line_new)
		line=f.readline()
	f.close()
	fnew.close()
	return basename+"_TMP"

