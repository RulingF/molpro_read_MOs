#!/usr/bin/python
#Filename: Classes.py
import ele

class Basis_set:
	'''Represents basis sets.'''
	def __init__(self,atomic_number):
		'''Initialize constructed Basis_set'''
		#Read atomic number
		self.Z=atomic_number
		#Read period number
		self.period_number=ele.periodnumber_reg(self.Z)
		self.numofs=0
		self.numofp=0
		self.numofd=0
		self.numoff=0
		self.numofg=0
		self.numofh=0
		self.numofi=0
		self.numofk=0
		self.numofl=0
		self.numofm=0
		self.numofn=0
		self.LT_EXP_COE_S=[]
		self.LT_EXP_COE_P=[]
		self.LT_EXP_COE_D=[]
		self.LT_EXP_COE_F=[]
		self.LT_EXP_COE_G=[]
		self.LT_EXP_COE_H=[]
		self.LT_EXP_COE_I=[]
		self.LT_EXP_COE_K=[]
		self.LT_EXP_COE_L=[]
		self.LT_EXP_COE_M=[]
		self.LT_EXP_COE_N=[]
                self.LT_EXP_COE_LT=[self.LT_EXP_COE_S,self.LT_EXP_COE_P,self.LT_EXP_COE_D,self.LT_EXP_COE_F,self.LT_EXP_COE_G,self.LT_EXP_COE_H,self.LT_EXP_COE_I,self.LT_EXP_COE_K,self.LT_EXP_COE_L,self.LT_EXP_COE_M,self.LT_EXP_COE_N]
                self.LT_EXP_COE_ALL=[]
                self.LT_EXP_COE_ALL_PAIR=[]
		#Split EXP and COE
		self.LT_EXP_S=[]
		self.LT_COE_S=[]
		self.LT_EXP_P=[]
                self.LT_COE_P=[]
                self.LT_EXP_D=[]
                self.LT_COE_D=[]
                self.LT_EXP_F=[]
                self.LT_COE_F=[]
                self.LT_EXP_H=[]
                self.LT_COE_H=[]
		self.LT_EXP_G=[]
		self.LT_COE_G=[]
                self.LT_EXP_I=[]
                self.LT_COE_I=[]
                self.LT_EXP_K=[]
                self.LT_COE_K=[]
                self.LT_EXP_L=[]
                self.LT_COE_L=[]
                self.LT_EXP_M=[]
                self.LT_COE_M=[]
                self.LT_EXP_N=[]
                self.LT_COE_N=[]
                self.LT_EXP_LT=[self.LT_EXP_S,self.LT_EXP_P,self.LT_EXP_D,self.LT_EXP_F,self.LT_EXP_G,self.LT_EXP_H,self.LT_EXP_I,self.LT_EXP_K,self.LT_EXP_L,self.LT_EXP_M,self.LT_EXP_N]
                self.LT_COE_LT=[self.LT_COE_S,self.LT_COE_P,self.LT_COE_D,self.LT_COE_F,self.LT_COE_G,self.LT_COE_H,self.LT_COE_I,self.LT_COE_K,self.LT_COE_L,self.LT_COE_M,self.LT_COE_N]
                self.LT_EXP_ALL=[]
                self.LT_COE_ALL=[]
		#For pseudopotential
                self.PP_LT_EXP_S=[]
                self.PP_LT_COE_S=[]
                self.PP_LT_EXP_P=[]
                self.PP_LT_COE_P=[]
                self.PP_LT_EXP_D=[]
                self.PP_LT_COE_D=[]
                self.PP_LT_EXP_F=[]
                self.PP_LT_COE_F=[]
                self.PP_LT_EXP_H=[]
                self.PP_LT_COE_H=[]
                self.PP_LT_EXP_G=[]
                self.PP_LT_COE_G=[]
                self.PP_LT_EXP_I=[]
                self.PP_LT_COE_I=[]
                self.PP_LT_EXP_K=[]
                self.PP_LT_COE_K=[]
                self.PP_LT_EXP_L=[]
                self.PP_LT_COE_L=[]
                self.PP_LT_EXP_M=[]
                self.PP_LT_COE_M=[]
                self.PP_LT_EXP_N=[]
                self.PP_LT_COE_N=[]
                self.PP_LT_EXP_ALL=[]
                self.PP_LT_COE_ALL=[]
                #Recognise which element it is
		self.element_name=ele.element_reg(self.Z)
	def gbasis_split_EXP_COE(self,AMCtrl=-1):
		'''split coe and exp and put coe in the right matrix'''
		#S
		if not self.LT_COE_S and (AMCtrl==0 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_S:
				self.LT_EXP_S.append(item[0])
			for item in self.LT_EXP_COE_S:
				self.LT_COE_S.append(item[1:])
			COE_tmp=self.LT_COE_S
			for i,item in enumerate(self.LT_COE_S):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_S=COE_tmp
		#P
                if not self.LT_COE_P  and (AMCtrl==1 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_P:
				self.LT_EXP_P.append(item[0])
			for item in self.LT_EXP_COE_P:
				self.LT_COE_P.append(item[1:])
			COE_tmp=self.LT_COE_P
			for i,item in enumerate(self.LT_COE_P):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_P=COE_tmp
		#D
                if not self.LT_COE_D  and (AMCtrl==2 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_D:
				self.LT_EXP_D.append(item[0])
			for item in self.LT_EXP_COE_D:
				self.LT_COE_D.append(item[1:])
			COE_tmp=self.LT_COE_D
			for i,item in enumerate(self.LT_COE_D):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_D=COE_tmp
		#F
                if not self.LT_COE_F and (AMCtrl==3 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_F:
				self.LT_EXP_F.append(item[0])
			for item in self.LT_EXP_COE_F:
				self.LT_COE_F.append(item[1:])
			COE_tmp=self.LT_COE_F
			for i,item in enumerate(self.LT_COE_F):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_F=COE_tmp
		#G
                if not self.LT_COE_G and (AMCtrl==4 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_G:
				self.LT_EXP_G.append(item[0])
			for item in self.LT_EXP_COE_G:
				self.LT_COE_G.append(item[1:])
			COE_tmp=self.LT_COE_G
			for i,item in enumerate(self.LT_COE_G):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_G=COE_tmp
		#H
                if not self.LT_COE_H and (AMCtrl==5 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_H:
				self.LT_EXP_H.append(item[0])
			for item in self.LT_EXP_COE_H:
				self.LT_COE_H.append(item[1:])
			COE_tmp=self.LT_COE_H
			for i,item in enumerate(self.LT_COE_H):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_H=COE_tmp
		#I
                if not self.LT_COE_I and (AMCtrl==6 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_I:
				self.LT_EXP_I.append(item[0])
			for item in self.LT_EXP_COE_I:
				self.LT_COE_I.append(item[1:])
			COE_tmp=self.LT_COE_I
			for i,item in enumerate(self.LT_COE_I):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_I=COE_tmp
		#K
                if not self.LT_COE_K and (AMCtrl==7 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_K:
				self.LT_EXP_K.append(item[0])
			for item in self.LT_EXP_COE_K:
				self.LT_COE_K.append(item[1:])
			COE_tmp=self.LT_COE_K
			for i,item in enumerate(self.LT_COE_K):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_K=COE_tmp
		#L
                if not self.LT_COE_L and (AMCtrl==8 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_L:
				self.LT_EXP_L.append(item[0])
			for item in self.LT_EXP_COE_L:
				self.LT_COE_S.append(item[1:])
			COE_tmp=self.LT_COE_L
			for i,item in enumerate(self.LT_COE_L):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_L=COE_tmp
		#M
                if not self.LT_COE_M and (AMCtrl==9 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_M:
				self.LT_EXP_M.append(item[0])
			for item in self.LT_EXP_COE_M:
				self.LT_COE_S.append(item[1:])
			COE_tmp=self.LT_COE_M
			for i,item in enumerate(self.LT_COE_M):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_M=COE_tmp
		#N
                if not self.LT_COE_N and (AMCtrl==10 or AMCtrl==-1):
			COE_tmp=[]
			length3=0
			for item in self.LT_EXP_COE_N:
				self.LT_EXP_N.append(item[0])
			for item in self.LT_EXP_COE_N:
				self.LT_COE_N.append(item[1:])
			COE_tmp=self.LT_COE_N
			for i,item in enumerate(self.LT_COE_N):
				length=len(item)
				if length==1:
					for j,flag in enumerate(COE_tmp):
						length2=len(flag)
						if i!=j:
							flag.append(0.0)
							length3=length2
						else:
							i=0
							while i<length3:
								flag.append(0.0)
								i+=1
							flag.sort()
							break
			self.LT_COE_N=COE_tmp
	def molpro_regular_basis_in(self,The_File,linein,line_lt,lbr_am):
		'''Read molpro_regular basis set file'''
		line=linein
		if line and ele.atomicnumber_reg(line_lt[1])==self.Z:
			if line_lt[0]=='s':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_S,self.LT_COE_S,self.LT_EXP_COE_S,'s')
                                return line
			elif line_lt[0]=='p':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_P,self.LT_COE_P,self.LT_EXP_COE_P,'p')	
                                return line
			elif line_lt[0]=='d':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_D,self.LT_COE_D,self.LT_EXP_COE_D,'d')
                                return line
			elif line_lt[0]=='f':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_F,self.LT_COE_F,self.LT_EXP_COE_F,'f')
                                return line
			elif line_lt[0]=='g':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_G,self.LT_COE_G,self.LT_EXP_COE_G,'g')
                                return line
			elif line_lt[0]=='h':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_H,self.LT_COE_H,self.LT_EXP_COE_H,'h')
                                return line
			elif line_lt[0]=='i':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_I,self.LT_COE_I,self.LT_EXP_COE_I,'i')
                                return line
			elif line_lt[0]=='k':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_K,self.LT_COE_K,self.LT_EXP_COE_K,'k')
                                return line
			elif line_lt[0]=='l':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_L,self.LT_COE_L,self.LT_EXP_COE_L,'l')
                                return line
			elif line_lt[0]=='m':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_M,self.LT_COE_M,self.LT_EXP_COE_M,'m')
                                return line
			elif line_lt[0]=='n':
				line=self.molpro_regular_basis_in_AG(The_File,line,self.LT_EXP_N,self.LT_COE_N,self.LT_EXP_COE_N,'n')
                                return line
                        else:
                                return line
                else:
                        return line
	def molpro_regular_basis_in_AG(self,f,tmpline,basislt_EXP,basislt_COE,basislt_EXP_COE,AM):
                '''Read molpro_regular basis set file for each angular momentum.'''
		killslash_lt=tmpline.split('\n')
		tmpline1=killslash_lt[0]
		print self.element_name
		print AM
                while tmpline1 and tmpline1[0]==AM:
                        tmpline1_lt=tmpline1.split(',')
			if ele.atomicnumber_reg(tmpline1_lt[1])!=self.Z:
				tmpline=f.readline()
				if basislt_COE:
                                	num1=len(basislt_COE[0])
                        	else:
                                	num1=0
				break
                        if tmpline1_lt[0]==AM:
                                # read in exp
                                for item in tmpline1_lt[2:]:
                                        basislt_EXP.append(float(item))
			tmpline=f.readline()
			killslash_lt=tmpline.split('\n')
			tmpline1=killslash_lt[0]
			num2=len(basislt_EXP)
			#skip the comment lines
			while tmpline1 and tmpline1[0]=='!':
				tmpline=f.readline()
				killslash_lt=tmpline.split('\n')
				tmpline1=killslash_lt[0]
                        while tmpline1 and tmpline1[0]=='c':
                                # read in coeff s
                               	tmpline1_lt=tmpline1.split(',')
                                coe_mark_lt=tmpline1_lt[1].split('.')
                                coe_tmp=[]
                                for item in tmpline1_lt[2:]:
                                       	coe_tmp.append(float(item))
                                for count_i in range(1,int(coe_mark_lt[0])):
                                       	coe_tmp.insert(0,0)
				for count_i in range(int(coe_mark_lt[1]),num2):
					coe_tmp.append(0)
                               	basislt_COE.append(coe_tmp)
				tmpline=f.readline()
				killslash_lt=tmpline.split('\n')
				tmpline1=killslash_lt[0]
				# skip the comment lines
				while tmpline1 and tmpline1[0]=='!':
					tmpline=f.readline()
					killslash_lt=tmpline.split('\n')
					tmpline1=killslash_lt[0]
			if basislt_COE:
			        num1=len(basislt_COE[0])
			else:
        			num1=0
		if num1!=num2:
			for count_i in range(0,num2-num1):
				for item in basislt_COE:
					item.append(0)
				coe_tmp=[]
				for count_j in range(0,num1+count_i):
					coe_tmp.append(0)
				coe_tmp.append(1)
				basislt_COE.append(coe_tmp)
		tmp_lt=map(list,zip(*basislt_COE))
                del basislt_EXP_COE[:]
		for i,item in enumerate(tmp_lt):
			item=[item]
			for j,jtem in enumerate(tmp_lt):
				if i==j:
					basislt_EXP_COE.append(item+jtem)
		return tmpline
	def molpro_library_basis_in(self,The_File,line,am,contr):
		linelt=line.split(' ')
		linelt=filter(None,linelt)
		while line and self.Z==ele.atomicnumber_reg(linelt[0]):
                        if linelt[1] in am:
                                i='spdfghiklmn'.index(linelt[1])
                                line=self.molpro_library_basis_in_AG(The_File,line,self.LT_EXP_COE_LT[i],linelt[1],contr)
                                for j in range(0,len(self.LT_EXP_COE_LT[i])):
                                        self.LT_EXP_LT[i].append(self.LT_EXP_COE_LT[i][j][0])
                                        self.LT_COE_LT[i].append(self.LT_EXP_COE_LT[i][j][1:])
                                tmp_lt=map(list,zip(*self.LT_COE_LT[i]))
                                del self.LT_COE_LT[i][:]
                                self.LT_COE_LT[i].extend(tmp_lt)
        			linelt=line.split(' ')
        			linelt=filter(None,linelt)
                        else:
                                line=The_File.readline()
                                linelt=line.split(' ')
                                linelt=filter(None,linelt)
                                while line and self.Z!=ele.atomicnumber_reg(linelt[0]):
                                        line=The_File.readline()
                                        linelt=line.split(' ')
                                        linelt=filter(None,linelt)
	def molpro_library_basis_in_AG(self,f,line,basislt_EXP_COE,AM,C):
                linelt=line.split(':')
                linelt[0]=linelt[0].split()
                linelt[1]=linelt[1].split()
                linelt[0]=filter(None,linelt[0])
                linelt[1]=filter(None,linelt[1])
                cctmp=[]
                lt2=[]
                lt3=[]
                numofbas=int(linelt[1][0])
                print self.element_name
                print AM
                if C and C[0]=='c':
                        numofcbas=int(linelt[1][1])
                        for i in range(0,numofcbas):
                        	lttmp=linelt[1][2+i].split('.')
                        	cctmp.append(lttmp)
		        linelt=line.split(' ')
		        linelt=filter(None,linelt)
		        while not self.is_Num(linelt[0]):
		        	line=f.readline().strip('\n')
		        	linelt=line.split(' ')
		        	linelt=filter(None,linelt)
		        while line and self.is_Num(linelt[0]):
		        	for item in linelt:
		        		lt2.append(float(item));
		        	line=f.readline()
		        	line=line.strip()
                                linelt=line.split(' ')
                                linelt=filter(None,linelt)
		        for i in range(0,numofbas):
		        	lt3.append(lt2[i])
		        	basislt_EXP_COE.append(lt3)
		        	lt3=[]
		        count=numofbas
		        for i in range(0,numofcbas):
		        	for j in range(0,numofbas):
		        		if j<int(cctmp[i][0])-1:
		        			basislt_EXP_COE[j].append(0)
		        		elif j>int(cctmp[i][0])-2 and j<int(cctmp[i][1]):
		        			try:
		        				basislt_EXP_COE[j].append(lt2[j+count])
		        			except IndexError:
		        				basislt_EXP_COE[j].append(1)
		        				count-=1
		        		else:
		        			basislt_EXP_COE[j].append(0)
		        	count+=int(cctmp[i][1])-int(cctmp[i][0])+1
                elif C and C[0]!='c' and ('c' in C[0]):
                        numofcbas=int(C[0].strip('c'))
                        for i in range(0,numofcbas):
                                lttmp=C[1+i].split('.')
                                cctmp.append(lttmp)
                        linelt=line.split(' ')
                        linelt=filter(None,linelt)
                        while not self.is_Num(linelt[0]):
                                line=f.readline()
                                linelt=line.split(' ')
                                linelt=filter(None,linelt)
                        while line and self.is_Num(linelt[0]):
                                for item in linelt:
                                        lt2.append(float(item))
                                line=f.readline()
                                line=line.strip()
                                linelt=line.split(' ')
                                linelt=filter(None,linelt)
                        for i in range(0,numofbas):
                                lt3.append(lt2[i])
                                basislt_EXP_COE.append(lt3)
                                lt3=[]
                        count=numofbas
                        for i in range(0,numofcbas):
                                for j in range(0,numofbas):
                                        if j<int(cctmp[i][0])-1:
                                                basislt_EXP_COE[j].append(0)
                                        elif j>int(cctmp[i][0])-2 and j<int(cctmp[i][1]):
                                                try:
                                                        basislt_EXP_COE[j].append(lt2[j+count])
                                                except IndexError:
                                                        basislt_EXP_COE[j].append(1)
                                                        count-=1
                                        else:
                                                basislt_EXP_COE[j].append(0)
                                count+=int(cctmp[i][1])-int(cctmp[i][0])+1 
                elif not C:
                    linelt=line.split()
                    while not self.is_Num(linelt[0]):
                        line=f.readline()
                        linelt=line.split()
                        linelt=filter(None,linelt) 
                    while line and self.is_Num(linelt[0]):
                        for item in linelt:
                            lt2.append(float(item))
                        line=f.readline()
                        line=line.strip()
                        linelt=line.split(' ')
                        linelt=filter(None,linelt)
                    for i in range(0,numofbas):
                        lt3.append(lt2[i])
                        basislt_EXP_COE.append(lt3)
                        lt3=[] 
                else:
                        print 'What the hell is'
                        print C[0]+'?'
                        print '\n There is a format error in the input file!'
                return line
	def gbasis_read_in_PP(self,The_File):
		'''Read PP from a gbasis file'''
				
	def gbasis_read_in_PP(self,The_File):
		'''Read PP from a gbasis file'''
	def gbasis_read_in(self,The_File,angular_momentum_line):
		'''Read angular_momentum from a line that contains angular momentum'''
		#Read angular momentum
		flag=0
		tmplt=[]
		tmpline=''
		value1=angular_momentum_line[10:]
	#	print value1
		value2=angular_momentum_line[:10]
	#	print value2
		if ('S' or 's') in value1:
			self.numofs=int(filter(str.isdigit,value2))
	#		print "This is a number : %d" %self.numofs
		#Read in coeff s:
			while(flag<self.numofs):
				tmpline=The_File.readline()
	#			print tmpline
	#			print flag
				tmplt=self.read_in_Num(tmpline)
				self.LT_EXP_COE_S.append(tmplt)
				flag+=1
		elif ('P' or 'p') in value1:
			self.numofp=int(filter(str.isdigit,value2))
	#		print "This is a number : %d" %self.numofp
                #Read in coeff p:
                        while(flag<self.numofp):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_P.append(tmplt)
				flag+=1
		elif ('D' or 'd') in value1:
			self.numofd=int(filter(str.isdigit,value2))
                #Read in coeff d:
                        while(flag<self.numofd):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_D.append(tmplt)
				flag+=1
		elif ('F' or 'f') in value1:
			self.numoff=int(filter(str.isdigit,value2))
                #Read in coeff f:
                        while(flag<self.numoff):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_F.append(tmplt)
				flag+=1
                elif ('G' or 'g') in value1:
                        self.numoff=int(filter(str.isdigit,value2))
                #Read in coeff f:
                        while(flag<self.numoff):
                                tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_G.append(tmplt)
                                flag+=1

		elif ('H' or 'h') in value1:
			self.numofh=int(filter(str.isdigit,value2))
                #Read in coeff h:
                        while(flag<self.numofg):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_H.append(tmplt)
				flag+=1
		elif ('I' or 'i') in value1:
			self.numofi=int(filter(str.isdigit,value2))
                #Read in coeff i:
                        while(flag<self.numofi):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_I.append(tmplt)
				flag+=1
		elif ('K' or 'k') in value1:
			self.numofk=int(filter(str.isdigit,value2))
                #Read in coeff k:
                        while(flag<self.numofk):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_K.append(tmplt)
				flag+=1
		elif ('L' or 'l') in value1:
			self.numofl=int(filter(str.isdigit,value2))
                #Read in coeff l:
                        while(flag<self.numofl):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_L.append(tmplt)
				flag+=1
                                self.LT_EXP_COE_M.append(tmplt)
				flag+=1
		elif 'N' or 'n' in value1:
			self.numofn=int(filter(str.isdigit,value2))
                #Read in coeff n:
                        while(flag<self.numofn):
				tmpline=The_File.readline()
                                tmplt=self.read_in_Num(tmpline)
                                self.LT_EXP_COE_N.append(tmplt)
				flag+=1
                #sort and split
                self.LT_EXP_COE_S.sort(reverse=True)
                self.LT_EXP_COE_P.sort(reverse=True)
                self.LT_EXP_COE_D.sort(reverse=True)
                self.LT_EXP_COE_F.sort(reverse=True)
                self.LT_EXP_COE_G.sort(reverse=True)
                self.LT_EXP_COE_H.sort(reverse=True)
                self.LT_EXP_COE_I.sort(reverse=True)
                self.LT_EXP_COE_K.sort(reverse=True)
                self.LT_EXP_COE_L.sort(reverse=True)
                self.LT_EXP_COE_M.sort(reverse=True)
                self.LT_EXP_COE_N.sort(reverse=True)
	def read_in_Num(self,exp_coe_line):
		'''Read Exponentials and Coefficients in one line'''
		line=exp_coe_line.split()
		i=0
		while i<len(line):
			if 'D' in line[i]:
				line[i]=line[i].replace('D','E')
			i+=1
		return map(float,line)
	def is_Num(self,inputstr):
		dot_count=0
		E_count=0
		plus_count=0
		minus_count=0
		inputstr=inputstr.strip('-+')
		for item in inputstr:
			if item=='.':
				dot_count+=1
			elif item=='E' or item=='D' or item=='e':
				E_count+=1
			elif item=='+':
				plus_count+=1
			elif item=='-':
				minus_count+=1
			elif not item.isdigit():
				return False
		if dot_count>1:
			return False
		elif E_count>1:
			return False
		elif plus_count>1:
			return False
		elif minus_count>1:
			return False
		else:
			return True
        def Sum_lt(self):
                for item,jtem in zip('SPDFGHIKLMN',self.LT_EXP_COE_LT):
                        self.LT_EXP_COE_ALL.append([item]+jtem)
                for item,jtem in zip('SPDFGHIKLMN',self.LT_EXP_LT):
                        self.LT_EXP_ALL.append([item]+jtem)
                for item,jtem in zip('SPDFGHIKLMN',self.LT_COE_LT):
                        self.LT_COE_ALL.append([item]+jtem)
        def Pair_ALL(self):
                tmplt1=[]
                tmplt2=[]
                for i1tem in self.LT_EXP_COE_ALL:
                        try:    
                                tmplt2.append(i1tem[0])
                                for k in range(0,len(i1tem[1][1:])):
                                        for i2tem in i1tem[1:]:
                                                if i2tem[k+1] != 0:
                                                        tmplt1.append([i2tem[0],i2tem[k+1]])
                                        tmplt2.append(tmplt1)
                                        tmplt1=[]
                                self.LT_EXP_COE_ALL_PAIR.append(tmplt2)
                                tmplt2=[]
                        except IndexError:
                                print 'Warning: '+'Empty'+' '+i1tem[0]+' '+'angular momentum basis!!!'
                         
