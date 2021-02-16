'''
Kodutöö 3
2021-01-29
'''
__author__ = 'Uku-Kaarel Jõesaar'

import os
from os import listdir
from os.path import isfile, join
from datetime import *

def input_taisarv(msg, lenght=0):
    input_loop = 0
    while input_loop == 0:
        arv = input(msg)
        if lenght == 0 and arv.isdigit():
            input_loop = 1
        elif len(arv)==lenght and arv.isdigit():
            input_loop = 1
    return int(arv)

def input_lubatudSona(msg, lubatudSonadS):
    '''
    msg : str kuvatakse ekraanil
    lubatudSonad : list on loend lubatud sõnadest.
    '''
    lubatudSonad = []
    for lsona in lubatudSonadS:
        lubatudSonad.append(lsona.lower())
    print ( lubatudSonad )
    input_loop = 0
    while input_loop == 0:
        sona = input(msg)
        sona = sona.strip().lower()
        if sona in lubatudSonad:
            input_loop = 1
    return sona

def input_plaadinimi(msg):
    plaadid = []
    plaatide_sisu = {}
    files = os.listdir('.')
    for f in files:
        fj = join('.', f)
        if isfile(fj) and fj.endswith('.txt'):
            read = [str(rida.strip()) for rida in open(fj)]
            on_plaadifail = False
            for rida in read:
                if ' - ' in rida:
                    on_plaadifail = True
            if on_plaadifail:
                plaadid.append(f)
    
    print('Saadaolevad plaadid: ',plaadid)
    see_plaat = input_lubatudSona('Sisestage failinimi: ', plaadid)
    print('Muusikapalade valik:')
    lugu_num = 1
    for lugu in plaatide_sisu[see_plaat]:
        print("{}. {}".format(lugu_num, lugu))
    
    see_lugu = input_lubatudSona('Valige laulu järjekorra number: ', plaatide_sisu[see_plaat] )
    print("Mängitav muusikapala on {}".format(see_lugu))

'''


    input_loop = 0
    while input_loop == 0:
        nimi = input(msg)
        for name in files:
        	print(name)
        # is file
        # plaadi formaat
        # is ext
        if nimi.replace(' ','').isalpha():
        	# nimi = nimi.camelcase()
            nimi = nimi.title()
            input_loop = 1
    return nimi
'''

def pealkiri(p):
    ''''''
    print( f"\n{p.rjust(40)}" )
    print( ''.join(["-" for i in range(40-len(p)) ] ) \
         + ''.join([" " for i in range(len(p)-1 ) ] ) + '+')
            
def yl_vastuvoetud():
    '''Rebased'''
    algusaasta=2011
    vastuvõetud = [str(rida.strip()) for rida in open('rebased.txt')]
    aastad = [str(aasta) for aasta in range( algusaasta, algusaasta+len(vastuvõetud))]
    pealkiri('Ülikooli vastuvõetud')
    print('Lõpetanute andmed on nende aastate kohta:')
    vajate = input_lubatudSona('Palun sisestage, millise aasta andmeid vajate: ', aastad)
    print("{}. aastal oli vastuvõetuid {}".format(vajate, vastuvõetud[aastad.index(vajate)]) )
#yl_vastuvoetud()



def yl_jukebox():
    """ jukebox """
    pealkiri('Jukebox')
    print('\n\nJukebox on failis \'ITT20-PKodutöö-3-Jukebox.py\'\n\n')





def yl_janesteSysteem(ringe=-1):
    '''Jänesevanemad on mures'''
    pealkiri('Jänesevanemate mure ver. 3')
    #if(ringe == -1):
    #
    #    ringe = input_taisarv("Mitu ringi jänkupoeg tegi: ")
    #print("Jänkupoeg tegi",ringe,"ja saab", sum([ i for i in range(2, ringe) if i%2==0 ]),"porgandit.")
    
    if(ringe == -1):
        ringe = input_taisarv("Mitu ringi jänkupoeg tegi: ")
    saab=0
    for r in range(0, ringe+1, 2):
        saab += r
    print("Jänkupoeg tegi",ringe,"ja saab", saab ,"porgandit.")

'''
yl_janesteSysteem(1) #0
yl_janesteSysteem(3) #2
yl_janesteSysteem(5) #6  2+4
yl_janesteSysteem(6) #12 2+4+6
yl_janesteSysteem(7) #12 2+4+6
yl_janesteSysteem(8) #20 2+4+6+8
yl_janesteSysteem(9) #20 2+4+6+8
yl_janesteSysteem(12) #42 2+4+6+8+10+12
'''
#yl_janesteSysteem(-1)


def yl_sissetulekud():
    '''Ainult sissetulekud'''
    pealkiri('Sissetulekud')
    print( "\n".join([ str(tehing) for tehing in [float(tehing.strip()) for tehing in open('konto.txt')] if tehing>0 ]) )


#yl_sissetulekud()



def yl_tahvlijuurde():
    kp = datetime.now()
    pealkiri( kp.isoformat() +'            Tahvli juurde')
    fail = input("Sisestage failinimi: ")
    if isfile(fail):
        #read = [str(rida.strip()) for rida in open(fail)]
        print('Vastama tuleb: ', [str(rida.strip()) for rida in open(fail)][kp.day] )


#yl_tahvlijuurde()





yl_def_list =  ['yl_vastuvoetud', 'yl_janesteSysteem', 'yl_jukebox', 'yl_sissetulekud', 'yl_tahvlijuurde']

print('\n\nÜlesanded', yl_def_list, '\n')
for yl_def in yl_def_list:
    locals()[yl_def]()
    yl_kasJatkata = input('\nJärgmise ülesande jaoks vajuta [Enter], Katkestamiseks [Q] ja [Enter] \n')
    if yl_kasJatkata=='':
        continue
    else:
        if yl_kasJatkata == 'Q' or  yl_kasJatkata == 'q':
            print("\n\n\nProgramm lõpetab\n\n\n")
            break
        else:
            print("\n\n\nViga #None\nSisestasite tundmatu sümboli, programm jooksis kokku!\n\n\n")
        break