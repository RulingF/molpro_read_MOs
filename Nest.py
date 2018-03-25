#!/usr/bin/python
#Filename: auto.py
import Classes
import Functions
import ele
import sys
import os
import cPickle

#def Gbasis_readin():
#def Molpro_regular_readin():
	
def Number_of_Basisin():
	No_of_basis=raw_input('Please specify how many elements you want?')
	if No_of_basis.isdigit()!=True:
        	print 'Please input a number, error exit...'
        	sys.exit(1)
	Int_of_basis=int(No_of_basis)
	return Int_of_basis

def Type_of_Basisin():
	print '''
	Please specify what kind of basis set format you are hoping to convert:
	1. Gbasis format.
	2. Molpro regular format.
	3. Molpro library format.
	4. Other formats.'''
	n=raw_input()
	try:
		n=int(n)
	except ValueError:
		print "Please input a integer, error exit"
		sys.exit(1)
	if n>4 or n<1:
		print "Please input the number ahead of each type, error exit..."
		sys.exit(1)
	print ''
	return n
def Usr_in_basisdir_check():
	while True:
		Dir_Name=raw_input('Please specify the directory and file name (ex: /home/kirk/gbasis/CC-PVTZ.BAS) :')
		#Error Control	
		if os.path.isfile(Dir_Name)==True:
			return Dir_Name
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
def Defaultmolpro_in_basisdir_check(Dir_Name):
	while True:
		#Error Control
		if os.path.isdir(Dir_Name)==True:
                        return Dir_Name
		else:
                        print 'Invalid current default directory: ' + Dir_Name + '\n Do you want to change it? \n 1.Continue \n 2.Exit'
                        Ctrl_local_exit=raw_input('')
                        if Ctrl_local_exit=='2':
                                sys.exit(1)
                        elif Ctrl_local_exit=='1':
                                pass
                        else:
                                print 'Wrong input, error exit!'
                                sys.exit(1)
                        Dir_Name=raw_input('Please specify a new molpro default library basis set directory and file name (ex: /home/kirk/molpro/lib/) :')
def read_molpro_library_basis(basis,f,am,z,basis_contr_lt):
        while True:
                line=f.readline()
                #error control
                if len(line)==0:
                        print 'There is no such element in this file! \n 1. Continue  2. Exit \n'
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
                line_lt=line.split(' ')
                line_lt=filter(None,line_lt)
                if line[0]!='!' and line[0]!='*' and len(line_lt)>2 and z==ele.atomicnumber_reg(line_lt[0]):
                        basis.molpro_library_basis_in(f,line,am,basis_contr_lt)
                        f.close()
                        return True 
def readline_and_strip_and_skip(f,line,z):
        line1=line.strip()
        line_lt=line1.split(',')
        while line:
                if (not line1):
                        line=f.readline()
                        line1=line.strip()
                        line_lt=line1.split(',')
                elif line1 and line1[0]=='!':
                        line=f.readline()
                        line1=line.strip()
                        line_lt=line1.split(',')
                elif line1 and line1[0]!='!' and z!=ele.atomicnumber_reg(line_lt[1]):
                        line=f.readline()
                        line1=line.strip()
                        line_lt=line1.split(',')
                elif line1 and line1[0]!='!' and z==ele.atomicnumber_reg(line_lt[1]) and line_lt[0]=='ecp':
                        line=f.readline()
                        line1=line.strip()
                        line_lt=line1.split(',')
                else:
                        return (line,line1)
        else:
                return (line,line1)
def is_number(s):
        try:
                float(s)
                return True
        except ValueError:
                return False
