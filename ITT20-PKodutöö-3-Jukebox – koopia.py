#!python




class JukeboxPlaat:
    ''' '''
    sisukord = []
    sisukord_txt = ''
    autorid = []
    autoriplaat=False
    autornimi=''
    failinimi=''
    plaadinimi=''

    def __init__(self, failinimi=''):
        ''' '''

    def laadiPlaat(self, failinimi):
        ''' '''
        return True
    
    def get_sisukord(self):
        ''' '''
        return []
    
    def get_lugude_arv(self):
        ''' '''
        return 0

    def get_autorid(self):
        ''' '''
        return []
    
    def get_plaadinimi(self):
        ''' '''
        return ''

    def get_lugu_num(self, number):
        ''' '''
        return []

    def get_lugu_nimi(self, nimi):
        ''' '''
        return []

    def get_lugu_autor(self, number):
        ''' '''
        return []

    def is_autoriplaat(self):
        '''Kas plaadil on lood ainult ühelt autorilt'''
        return True

    def __str__(self):
        ''' '''
        return ''
    

class Jukebox:
    ''' '''
    kaustatee='.'
    plaadid={}
    selle_plaadi_num =0
    selle_plaadi_nimi=''
    selle_plaadi_fail=''

    def __init__(self):
        ''' '''
    
    def laadiKaust(self, sahtel):
        '''
        returns:int, Laetud plaatide arv
        '''
        self.kaustatee = sahtel
        #leia plaadid
        for plfn in []:
            JP = JukeboxPlaat()
            JP.laadiPlaat(plfn)
            self.plaadid['plnimi'] = JP
        return 0

    def valiPlaat(self, nimi):
        ''' 
        nimi:str, failinimi või nimi
        '''

        return True

    def kuvaPlaadNimi(self):
        ''' 
        returns:str, valitud plaadi nimi
        '''
        return ''

    def kuvaPlaadSisukord(self, vorm=0):
        '''
        vorm::int, väljundi tüüp: 0=str, 1=list
        returns:str|list
        '''
        if vorm==0:
            return ''

        return []

    def listPlaadid(self, vorm=0):
        ''' '''
        if vorm==0:
            return ''

        return []

    def __str__(self):
        ''' '''
        
        return "kaust: {}\n plaadid: {}\n valitud plaat:\n  nimi: {}\n  number: {}\n  fail: {}\n  lugusi: {}".format(self.kaustatee, ', '.join(self.plaadid), self.selle_plaadi_num, self.selle_plaadi_nimi, self.selle_plaadi_fail, 4 )








juk = Jukebox()
juk.laadiKaust('.')
print(juk.listPlaadid(0), '\nSisestage failinimi:')
valik='80ndad.txt'
valik='jukebox'

juk.valiPlaat(valik)
print('Muusikapalade valik:')
print( juk.kuvaPlaadNimi() )
print( juk.kuvaPlaadSisukord(0) )

print('\nSisestage laulu number:')
valik='2'


doc = ''
doc_f = open("./jukebox_doc.txt", "a")
for method in [method for method in dir(Jukebox) if method.startswith('_') is False]:
    exec(f"doc_f.write(Jukebox.{method}.__doc__)")
for method in [method for method in dir(JukeboxPlaat) if method.startswith('_') is False]:
    exec(f"doc_f.write(JukeboxPlaat.{method}.__doc__)")
doc_f.close()