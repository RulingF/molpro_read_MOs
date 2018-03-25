#!/usr/bin/python
#Filename: auto.py
import Classes
import Functions
import ele
import Nest
import sys
import os
import cPickle
#Main function that executes.

#Multi elements input
#No_of_basis=Nest.Number_of_Basisin()
No_of_basis=15
#Reading basis type
#In_basis_format=Nest.Type_of_Basisin()
In_basis_format=3
#############################################################################################################
#############################################################################################################
#############################################################################################################
#gbasis part	
if In_basis_format==1:
        #error control
        while True:
                Usr_in_basis_name=raw_input('Please specify the gbasis directory and file name (ex: home/kirk/gbasis/CC-PVTZ.BAS) :')
                if os.path.isfile(Usr_in_basis_name)==True:
                        break
                else:
                        print 'File does not exist, please check your input.\n 1.Continue \n 2.Exit'
                        Ctrl_local_exit=raw_input('')
                        if Ctrl_local_exit=='2':
                                sys.exit(1)
                        elif Ctrl_local_exit=='1':
                                continue
                        else:
                                print 'Wrong input, error exit!'
                                sys.exit(1)
	for count_i in range(No_of_basis):
        	f=file(Usr_in_basis_name,'r')
		Gbl_Z=raw_input('Please input what is the atomic number of the element that you want: ')
		#Read gbasis
		while True:
			line=f.readline()
			if len(line)==0:
				print 'There is no such basis set in this file! \n 1. Continue  2. Exit \n'
                                Ctrl_local_exit=raw_input('')
                                if Ctrl_local_exit=='2':
                                        sys.exit(1)
                                elif Ctrl_local_exit=='1':
                                        f.close()
                                        f=file(Usr_in_basis_name,'r')
                                        Gbl_Z=raw_input('Please input what is the atomic number of the element that you want: ')
	                        else:
                                	print 'Wrong input, error exit!'
                                	sys.exit(1)
			if 'Z='+Gbl_Z in line[:5]:
				z=int(Gbl_Z)
				basis=Classes.Basis_set(z)
				line=f.readline()
				while line[:2]!='Z=' and line[:3]!='END':
					if line[:6]=='NUMEXP':
						basis.gbasis_read_in(f,line)
					line=f.readline()
				else:
					f.close()
					break
		#print basis.LT_EXP_COE_S
		#read regular basis if it is an augmented basis set
		Usr_in_basis_name_basename=os.path.basename(Usr_in_basis_name)
		Usr_in_basis_name_dirname=os.path.dirname(os.path.realpath(Usr_in_basis_name))
		if 'AUG' in Usr_in_basis_name_basename:
			Usr_in_basis_name_basename_no_aug=Usr_in_basis_name_basename[4:]
			Usr_in_basis_name_regular=Usr_in_basis_name_dirname+'/'+Usr_in_basis_name_basename_no_aug
			if os.path.isfile(Usr_in_basis_name)!=True:
				print 'This directory does not have a regular basis set file corresponding to the AUG basis set file, error exit!'
				sys.exit(1)
			f=file(Usr_in_basis_name_regular)
			while True:
				line=f.readline()
				if len(line)==0:
					print 'The directory you specified does not include the basis set file without augmented functions, error exit!'
					f.close()
					sys.exit(1)
				if 'Z='+Gbl_Z in line[:5]:
					line=f.readline()
					while line[:2]!='Z=' and line[:3]!='END':
						if line[:6]=='NUMEXP':
							basis.gbasis_read_in(f,line)
						line=f.readline()
					else:
						f.close()
						break
		#Split the coe's and exp's
		basis.gbasis_split_EXP_COE()
		#Put basis obj in cpickle
		str_count_i=str(count_i)
		pickle_file=file('TEMP_pickle'+str_count_i,'w')
		cPickle.dump(basis,pickle_file)
                del basis
		pickle_file.close()
		print "Reading finished sucessfully!"
#############################################################################################################
#Molpro_regular_basis_in part
elif In_basis_format==2:
	Usr_in_basis_name_tmp=Nest.Usr_in_basisdir_check()
	Usr_in_basis_name=Functions.molproregular_basisfile_pre_processor(Usr_in_basis_name_tmp)
	Usr_in_basis_name_basename='Undefined converted by Python'
	Usr_in_basis_name_default_dir=Nest.Defaultmolpro_in_basisdir_check('/home/kipeters/molpro/sandybridge/lib/')
	#Read molpro_regular_basis_sets	
	for count_i in range(No_of_basis):
                f=file(Usr_in_basis_name,'r')
                Gbl_Z=raw_input('Please input what is the atomic number of the element that you want: ')
                z=int(Gbl_Z)
                line=f.readline()
                while not f.closed:
                        tmp_tp=Nest.readline_and_strip_and_skip(f,line,z)
                        line=tmp_tp[0]
                        line1=tmp_tp[1]
                        line_lt=line1.split(',')
            			#error control
                        if len(line)==0:
                                try:
                                        if basis:
                                                for item in basis.LT_COE_LT:
                                                        tmp_lt=map(list,zip(*item))
                                                        del item[:]
                                                        item.extend(tmp_lt)
                                                for LT_EXP_COE_AM,LT_EXP_AM,LT_COE_AM in zip(basis.LT_EXP_COE_LT,basis.LT_EXP_LT,basis.LT_COE_LT):
                                                        del LT_EXP_COE_AM[:]
                                                        for item,jtem in zip(LT_EXP_AM,LT_COE_AM):
                                                                LT_EXP_COE_AM.append([item]+jtem)
                                                print 'End of Molpro Regular File!'
                                                f.close()
                                                pass
                                except NameError:
                                        print 'There is no such basis set in this file! \n 1. Continue  2. Exit \n'
                                        Ctrl_local_exit=raw_input('')
                                        if Ctrl_local_exit=='2':
                                                sys.exit(1)
                                        elif Ctrl_local_exit=='1':
                                                f.close()
                                                f=file(Usr_in_basis_name,'r')
                                                Gbl_Z=raw_input('Please input what is the atomic number of the element that you want: ')
				        	z=int(Gbl_Z)
                                        else:
                                                print 'Wrong input, error exit!'
                                                sys.exit(1)
                        #end of error control
                        try:
                                if basis:
                                        pass 
                        except NameError:
                                basis=Classes.Basis_set(z)
                                pre_am=''
                        while line and line_lt[1]:
                                if not Nest.is_number(line_lt[2]):
                                        library_basis_sc_lt=line_lt
                                        library_basis_lt=library_basis_sc_lt[:3]
                                        library_basis_contr_lt=library_basis_sc_lt[3:]
                                        lbr_am=library_basis_lt[0]
                                        pre_am=lbr_am
                                        lbr_element=library_basis_lt[1]
                                        lbr_element_atomicnumber=ele.atomicnumber_reg(lbr_element)
                                        lbr_basis_name=library_basis_lt[2].lower()
                                        try:
                                                fd=file(Usr_in_basis_name_default_dir+lbr_basis_name+'.libmol','r')
                                        except IOError:
                                                lbr_basis_name=lbr_basis_name.replace('-','_')
                                                try:
                                                        fd=file(Usr_in_basis_name_default_dir+lbr_basis_name+'.libmol','r')
                                                except IOError:
                                                        print Usr_in_basis_name_default_dir + lbr_basis_name + '.libmol' + ' does not exist! Select a solution: ' + ' \n 1. Continue (Manually specify the default library file )  2. Exit \n'
                                                        Ctrl_local_exit=raw_input('')
                                                        if Ctrl_local_exit=='2':
                                                                f.close()
                                                                sys.exit(1)
                                                        elif Ctrl_local_exit=='1':
                                                                Usr_in_basis_name_default_full=raw_input('Please type in the full file name including PATH and file NAME: ')
                                                                if os.path.isfile(Usr_in_basis_name_default_full):
                                                                        fd=file(Usr_in_basis_name_default_full,'r')
                                                                else:
                                                                        continue
                                                        else:
                                                                print 'Wrong input, error exit!'
                                                                f.close()
                                                                sys.exit(1)
                                        Nest.read_molpro_library_basis(basis,fd,lbr_am,lbr_element_atomicnumber,library_basis_contr_lt)
                                        line=f.readline()
                                        if not line:
                                                for letter_am in lbr_am:
                                                        i='spdfghiklmn'.index(letter_am)
                                                        del basis.LT_EXP_COE_LT[i][:]
                                                        tmpltlt=[]
                                                        tmplt=[]
                                                        count=len(basis.LT_EXP_LT[i])
                                                        for k in range(0,count):
                                                            for j in range(0,count):
                                                                if k==j:
                                                                    tmplt.append(1)
                                                                else:
                                                                    tmplt.append(0)
                                                            tmpltlt.append(tmplt)
                                                            tmplt=[]
                                                        del basis.LT_COE_LT[i][:]
                                                        basis.LT_COE_LT[i].extend(tmpltlt)
                                                        for item,jtem in zip(basis.LT_EXP_LT[i],tmpltlt):
                                                            basis.LT_EXP_COE_LT[i].append([item]+jtem)
                                        while line and line[0]!='c':
                                                for letter_am in lbr_am:
                                                        i='spdfghiklmn'.index(letter_am)
                                                        del basis.LT_EXP_COE_LT[i][:]
                                                        tmpltlt=[]
                                                        tmplt=[]
                                                        count=len(basis.LT_EXP_LT[i])
                                                        for k in range(0,count):
                                                            for j in range(0,count):
                                                                if k==j:
                                                                    tmplt.append(1)
                                                                else:
                                                                    tmplt.append(0)
                                                            tmpltlt.append(tmplt)
                                                            tmplt=[]
                                                        del basis.LT_COE_LT[i][:]
                                                        basis.LT_COE_LT[i].extend(tmpltlt)
                                                        del basis.LT_EXP_COE_LT[i][:]
                                                        for item,jtem in zip(basis.LT_EXP_LT[i],tmpltlt):
                                                            basis.LT_EXP_COE_LT[i].append([item]+jtem)
                                                linelt=line.split(',')
                                                print line
                                                if line.strip() and linelt[1]!=basis.element_name:
                                                    break
                                                elif line.strip() and linelt[1]==basis.element_name and linelt[0] not in lbr_am:
                                                    break
                                                else:
                                                    line=f.readline()
                                        while line and line[0]=='c':
                                                for letter_am in lbr_am:
                                                        i='spdfghiklmn'.index(letter_am)
                                                        line1=line.strip()
                                                        line1_lt=line1.split(',')
                                                        cctmp=line1_lt[1]
                                                        cccoe=line1_lt[2:]
                                                        tmplt=[]
                                                        for j in range(1,int(cctmp.split('.')[0])):
                                                                tmplt.append(0)
                                                        for j in range(int(cctmp.split('.')[0]),int(cctmp.split('.')[1])+1):
                                                                tmplt.append(float(cccoe[j-int(cctmp.split('.')[0])]))
                                                        for j in range(int(cctmp.split('.')[1]),len(basis.LT_EXP_LT[i])):
                                                                tmplt.append(0)
                                                        basis.LT_COE_LT[i].append(tmplt)
                                                        tmplt=map(list,zip(*basis.LT_COE_LT[i]))
                                                        del basis.LT_EXP_COE_LT[i][:]
                                                        for item,jtem in zip(basis.LT_EXP_LT[i],tmplt):
                                                                basis.LT_EXP_COE_LT[i].append([item]+jtem)
                                                line=f.readline()
                                        break
                                elif Nest.is_number(line_lt[2]) :
			                line=basis.molpro_regular_basis_in(f,line,line_lt,pre_am)
                                        break
		#Put basis obj in cpickle
                str_count_i=str(count_i)
                pickle_file=file('TEMP_pickle'+str_count_i,'w')
                cPickle.dump(basis,pickle_file)
                del basis
                pickle_file.close()
                print "Reading finished sucessfully!"
#############################################################################################################
#Molpro_library_basis_in part
elif In_basis_format==3:
        Usr_in_basis_name=Nest.Usr_in_basisdir_check()
        #Read molpro_library_basis_sets 
        z_lt=[89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
        for count_i,z in zip(range(No_of_basis),z_lt):
                f=file(Usr_in_basis_name,'r')
                #Gbl_Z=raw_input('Please input what is the atomic number of the element that you want: ')
                #z=int(Gbl_Z)
                basis=Classes.Basis_set(z)
                Nest.read_molpro_library_basis(basis,f,'spdfghiklmn',z,['c'])
                for item in basis.LT_COE_LT:
                        tmplt=map(list,zip(*item))
                        del item[:]
                        item.extend(tmplt)
                #Put basis obj in cpickle
                str_count_i=str(count_i)
                pickle_file=file('TEMP_pickle'+str_count_i,'w')
                cPickle.dump(basis,pickle_file)
                del basis
                pickle_file.close()
                print "Reading finished sucessfully!"
#############################################################################################################
#other parts that you want to add.		
elif In_basis_format==4:
	print "There is no other format currently."
	sys.exit(1)

#Basis Set Debug

#Print test
#print 'EXP_______COE'
#for item in basis.LT_EXP_COE_P:
#	print item
#	print '\n'
#print 'EXP_______'
#print basis.LT_EXP_P
#print 'COE_______'
#for item in basis.LT_COE_P:
#	print item
#	print '\n'
#LT_COE_P_TMP=map(list,zip(*basis.LT_COE_P))
#for item in LT_COE_P_TMP:
#        print item
#        print '\n'
#print basis.LT_EXP_COE_P
#print basis.LT_EXP_COE_D
#print basis.LT_EXP_COE_F
#print basis.LT_EXP_F
#print basis.LT_COE_F
#print basis.LT_EXP_COE_H
#print basis.LT_EXP_COE_I
#print basis.LT_EXP_COE_K
#print basis.LT_EXP_COE_L
#print basis.LT_EXP_COE_M
#print basis.LT_EXP_COE_N
#print basis.element_name
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#Basis set output format
print '''
Please specify what kind of basis set format you want to get?
1. Cfour format.
2. Dirac format.
3. Molpro regular format.
4. Molpro lib format.
5. Gbs(Gaussian basis set) format
6. Decontracted Gbs format
7. Web Txt format.
8. MOLCAS format.
9. Other types'''
Out_basis_format=raw_input()
print ''
#############################################################################################################
#Out put to types
if Out_basis_format=='1' or Out_basis_format=='2' or Out_basis_format=='3' or Out_basis_format=='4' or Out_basis_format=='5' or Out_basis_format=='6' or Out_basis_format=='7' or Out_basis_format=='8':
	Usr_out_basis_name=raw_input('Please specify the directory and file name that you want your output to be (ex: home/kirk/gbasis/CC-PVTZ.BAS) :')
	f1=file(Usr_out_basis_name,'w')
	for count_i in range(No_of_basis):
		str_count_i=str(count_i)
		pickle_file=file('TEMP_pickle'+str_count_i)
		basis=cPickle.load(pickle_file)
		#Cfour format output
		if Out_basis_format=='1':
			Functions.Cfour_output(basis,f1)
		#Dirac format output
		elif Out_basis_format=='2':
			Functions.Dirac_output(basis,f1)
		#Molpro format output
		elif Out_basis_format=='3':
			Functions.Molpro_R_output(basis,f1)
		#Molpro Lib format output
		elif Out_basis_format=='4':
			Functions.Molpro_L_output(basis,f1,Usr_in_basis_name_basename)
                #Gaussian format output
                elif Out_basis_format=='5':
                        Functions.Gaussian_output(basis,f1)
                #Gaussian format output
                elif Out_basis_format=='6':
                        Functions.Gaussian_Decon_output(basis,f1)
                #TXT format output
		elif Out_basis_format=='7':
			Functions.Txt_output(basis,f1)
                #MOLCAS format output
                elif Out_basis_format=='8':
                        Functions.MOLCAS_output(basis,f1)
		pickle_file.close()
		os.remove('TEMP_pickle'+str_count_i)
	f1.close()
	print 'Output sucessfully!'
#############################################################################################################
#Other parts that you want to add
elif Out_basis_format=='9':
        print "There is no other format currently."
	for count_i in range(No_of_basis):
		str_count_i=str(count_i)
		os.remove('TEMP_pickle'+str_count_i)
        sys.exit(1)
#Error exit
else:
        print "Please input the number ahead each type, error exit..."
	for count_i in range(No_of_basis):
                str_count_i=str(count_i)
                os.remove('TEMP_pickle'+str_count_i)
        sys.exit(1)

if In_basis_format == 2:
    print '''
    Do you want to keep the formatted molpro regular basis set file?
    YES or NO
    1 or 2
    '''
    TMP_file_ctrl=raw_input()
    print ''
    if TMP_file_ctrl=='1' or TMP_file_ctrl=='YES':
            sys.exit()
    elif TMP_file_ctrl=='2' or TMP_file_ctrl=='NO':
            try:
                    os.remove(Usr_in_basis_name)
                    sys.exit(1)
            except OSError:
                    print 'Never mind...'
                    sys.exit(1)
    else:
            print 'Wrong input, keeping the file.'
            sys.exit()
