class sobrapaev:

    Ilusat=''

    def Sobrapaeva(self):
        '''\t\tI l u s a t  s õ b r a p ä e v a !'''
        return True

    def Teile(self):
        return True

    def Koigile(self):
        return True

    def __str__(self):
        '''__str_: klassi objekt tekstina'''
        return "\t\t"+' '.join([method for method in dir(sobrapaev) if method.startswith('_') is False])
            
print(sobrapaev())
print(sobrapaev.Sobrapaeva.__doc__)


