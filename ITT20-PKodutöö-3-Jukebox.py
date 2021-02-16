#!python
import os, sys, textwrap
from os import listdir
from os.path import isfile, join




class JukeboxPlaat:
    '''Kirjeldab ühte plaati'''

    sisukord = []
    """list, listis on dict iga kande kohta"""
    lugudearv=0
    """int, lugude arv"""
    lugude_autorid = []
    """ list """
    lood  = []
    """ list """
    autoriplaat=False
    """bool, kas kõik lood on ühelt autorilt"""
    autorinimi=''
    """str, autori/te nimed komaga eraldatult"""
    failinimi=''
    """str, Plaadi failinimi/failitee"""
    plaadinimi=''
    """str, plaadi nimi failinimest"""
    teated=[]
    """list, teated"""
    lugudearv=0
    """ """


    def __init__(self):
        '''Vastasel korral järgmine plaat sisaldab eelmise andmeid'''
        self.sisukord = []
        self.lugude_autorid = []
        self.lood = []
        self.teated = []
        self.autorinimi = ''
        self.failinimi = ''
        self.plaadinimi = ''
        self.autoriplaat = False
        self.lugudearv=0

    def laadiPlaat(self, failinimi):
        '''Laadib failist plaadi

        parameters
        failinimi:str
        returns:bool
        '''
        plaadi_read = [str(r.strip()) for r in open(failinimi) if r != '']
        r=''
        for rida in plaadi_read:
            if ' - ' in rida:
                lugu_ja_autor = rida.split(' - ', 2)
                self.lugude_autorid.append( lugu_ja_autor[0] )
                self.lood.append( lugu_ja_autor[1] )
                self.sisukord.append( rida )
            else:
                self.teated.append('JukeboxPlaat.laadiPlaat() vale vorming '+failinimi+rida)
                return False
        self.lugudearv=len(self.sisukord)

        self.autoriplaat = True
        for a in self.lugude_autorid:
            if self.lugude_autorid[0] != a:
                self.autoriplaat = False
                break
        if self.autoriplaat==True:
            self.autorinimi=self.lugude_autorid[0]
        else:
            self.autorinimi=', '.join(self.lugude_autorid)
        
        self.failinimi=failinimi
        self.plaadinimi= os.path.splitext(os.path.basename(failinimi))[0]
        return True
    
    def get_sisukord(self):
        ''' '''
        return self.sisukord
    
    def get_sisukord_txt(self):
        ''' '''
        t=''
        i=1
        for rida in self.sisukord:
            t += f"{i}. {rida}\n"
            i += 1
        return t

    def get_lugude_arv(self):
        ''' '''
        return self.lugudearv

    def get_autorid(self):
        ''' '''
        return self.lugude_autorid

    def get_autor(self):
        ''' '''
        return self.autorinimi
    
    def get_plaadinimi(self):
        ''' '''
        return self.plaadinimi

    def get_plaadiFailiNimi(self):
        ''' '''
        return self.failinimi

    def get_lugu(self, number):
        '''Loo pealkiri ja autor'''
        if number in range(1, self.lugudearv):
            number = int(number) -1
            return self.sisukord[ number ]
        else:
            return ''

    def get_lugu_pealkiri(self, number):
        '''Loo pealkiri'''
        if number in range(1, self.lugudearv):
            number = int(number) -1
            return self.lood[number]
        else:
            return ''

    def get_lugu_autor(self, number):
        '''Loo autor'''
        if number in range(1, self.lugudearv):
            number = int(number) -1
            return self.lugude_autorid[number]
        else:
            return ''

    def is_autoriplaat(self):
        '''Kas plaadil on lood ainult ühelt autorilt'''
        return self.autoriplaat

    






class Jukebox:
    '''Plaadimängija toimingid
    
    * https://stackoverflow.com/questions/36520120/overwriting-clearing-previous-console-line
    '''
    kaustatee='.'
    plaadid={}
    selle_plaadi_nimi=''
    selle_plaadi_fail=''
    selle_plaadi_id=''

    def __init__(self):
        ''' '''
        self.kaustatee = self.selle_plaadi_nimi = self.selle_plaadi_fail = self.selle_plaadi_id = '.'
        self.plaadid = {}
    
    def laadiKaust(self, sahtel):
        '''
        returns:int, Laetud plaatide arv
        '''
        self.kaustatee = sahtel
        files = os.listdir(sahtel)
        #leia plaadid
        for plfn in files:
            fj = join('.', plfn)
            if isfile(fj) and fj.endswith('.txt'):
                self.valiPlaat(plfn)
        return len(self.plaadid)

    def valiPlaat(self, nimi):
        '''Saab valida ja lisada plaadi mida masin ei näinud
        nimi:str, failitee või nimi
        '''      
        #try: if isinstance(self.plaadid[nimi_bn], JukeboxPlaat):
        if nimi in self.plaadid:
            #print('valiPlaat vali', nimi )
            self.selle_plaadi_nimi = self.plaadid[nimi].get_plaadinimi()
            self.selle_plaadi_fail = self.plaadid[nimi].get_plaadiFailiNimi()
            self.selle_plaadi_id = self.plaadid[nimi].get_plaadinimi()+'.txt'
            #self.plaadid[nimi].__get__()
            return True
        
        elif isfile(nimi) and nimi.endswith('.txt'):
            nimi_bn = os.path.basename(nimi)
            nimi_t = os.path.splitext(os.path.basename(nimi))[0]            
            #print('valiPlaat lisa', nimi, nimi_bn, nimi_t )
            JP = JukeboxPlaat()
            if JP.laadiPlaat(nimi):
                self.plaadid[nimi_bn] = JP
                self.selle_plaadi_nimi = nimi_t # self.plaadid[nimi_bn].get_plaadinimi()
                self.selle_plaadi_fail = nimi # self.plaadid[nimi_bn].get_plaadiFailiNimi()
                self.selle_plaadi_id = nimi_bn # self.plaadid[nimi_bn].get_plaadinimi()+'.txt'
                return True
        
        return False

    def kuvaPlaadNimi(self):
        ''' 
        returns:str, valitud plaadi nimi
        '''
        return self.selle_plaadi_nimi

    def plaadiId(self):
        ''' 
        returns:str, valitud plaadi nimi
        '''
        return self.selle_plaadi_id

    def PlaadiSisukord(self):
        '''
        returns:str|list
        '''
        return self.plaadid[self.selle_plaadi_id].get_sisukord_txt()
    def PlaadiTeave(self):
        '''
        returns:str
        '''
        plaat = self.plaadid[self.selle_plaadi_id]
        inf = ''
        inf += 'Plaadi nimi: '+ plaat.get_plaadinimi() +'\n'
        inf += 'Plaadi failinimi: '+ plaat.get_plaadiFailiNimi() +'\n'
        if plaat.is_autoriplaat():
            inf += 'Autor: '+ plaat.get_autor() +'\n'
        else:
            inf += textwrap.fill('Autorid: '+ ', '.join(plaat.get_autorid())+'\n' , width=70)
        inf += 'Lugude arv: '+ str(plaat.get_lugude_arv()) +'\n'
        return inf
        
   
    def Plaadid_list(self):
        ''' '''
        return textwrap.fill('[\''+ '\', \''.join(list(self.plaadid.keys())) + '\']' , width=70)

    def format_jb_screen(self, msg, o=0):
        '''
        '''
        m = msg.split('\n')
        if o == 0:
            for r in m:
                print('    | '+r)
        else:
            for r in m:
                print( f'    |' +r+ ''.join([" " for i in range(80-6-len(r)) ] ) +'|' )

    def pealkiri(self, p, s):
        '''
        paramaters
        p:str, pealkiri
        s:str, staatus
        '''
        print( ''.join(["." for i in range(80) ] ))
        print( f'[{s}]' + ''.join([" " for i in range(80-2-len(p+s)) ] ) +p )

    def clear_screen(self):
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')




# https://kyletk.com/index.php/2017/12/16/overwriting-line-console-output-python/
plaadisahtel = '.'
juk = Jukebox()
juk_n = juk.laadiKaust(plaadisahtel)
ui_loop=True
juk_staatus='#'
plaat=''
while ui_loop:
    juk.clear_screen()
    juk.pealkiri('JUK',juk_staatus)
    juk.format_jb_screen( textwrap.fill("Jukeboxi plaadisahtlis on {} plaati:".format(juk_n), width=70), 80 )
    juk.format_jb_screen( textwrap.fill("{}".format( juk.Plaadid_list()), width=70), 80 )
    juk.format_jb_screen( textwrap.fill("""Kasutada saab ainult sobivas vormis faile. Plaadi valimiseks 
    tuleb sisestada selle nimi ja lisamiseks selle täielik või suhteline faili aadress.""", width=70), 80 )
    juk.format_jb_screen( textwrap.fill( "Lõpetamiseks ja tagasi liikumiseks sisestage Q"    , width=70), 80 )
    
    plaat = input('Plaat: ').strip()
    if juk.valiPlaat(plaat):
        juk_staatus ='#'
        juk.format_jb_screen( '    SEE PLAAT\n    ---------',80 )
        juk.format_jb_screen( juk.PlaadiTeave(), 80 )
        juk.format_jb_screen(  juk.PlaadiSisukord() ,80)

        ui_laul_loop=True
        while ui_laul_loop:
            laul = input('Laulu nr: ').strip()
            if laul in 'qQ':
                break
            juk_staatus ='> ' + juk.plaadid[juk.plaadiId()].get_lugu(int(laul))
            juk.format_jb_screen('Mängimisel:        >\n'+juk.plaadid[juk.plaadiId()].get_lugu_pealkiri(int(laul)), 80)

    elif plaat in 'qQ':
        juk.clear_screen()
        break
    else:
        juk_staatus ='?'
        juk.format_jb_screen('Plaati ei õnnestunud laadida!', 80)
        break   



''''
temp = vars(juk)
print('Object juk klass: ', juk.__class__ )
attrs = vars(juk)
for item in attrs.items():
    print(item[0],':' ,item[1])
'''

'''
def pydoc(klass, fail):
    klname = klass.__name__
    doc = ''
    doc_f = open(fail, "a")

    doc_f.write(klass.__name__+"\n")
    #exec(f"doc_f.write({klname}.__doc__)")
    doc += "\n\n\n\t\t"+klname +"\n\t\t################\n\t\t<< "+ klass.__doc__+" >> \n\n"
    for method in [method for method in dir(klass) if method.startswith('_') is False]:
        doc += "\t"+method+"\n\t<< "
        #doc+=(klass.__name__).method.__doc__



        # TODO: :(
        exec(f"doc += klass.{method}.__doc__" , {'doc':doc, 'klass':klass} )





        doc += " >>\n\n"
    
    doc += "\n\n---------------\n\n"
    doc_f.write(doc)
    doc_f.close()


pydoc(Jukebox, "./jukebox_doc.txt")
pydoc(JukeboxPlaat, "./jukebox_doc.txt")
'''