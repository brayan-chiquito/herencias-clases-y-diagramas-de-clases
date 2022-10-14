class Pagina :
    contenido = None
    numero = 0
    def __init__(self, contenido,  numero) :
        self.contenido =  contenido
        self.numero = numero
    def  getContenido(self) :
        return self.contenido
    def setContenido(self, nuevo_contenido) :
        self.contenido = nuevo_contenido
    def  getNumero(self) :
        return self.numero
    def setNumero(self, nuevo_numero) :
        self.numero = nuevo_numero
class Libro :
    titulo = None
    isbn = 0
    autor = None
    anyoPublicacion = 0
    paginas = None
    numeroPaginas = 0
    def __init__(self, titulo,  isbn,  autor,  anyoPublicacion) :
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anyoPublicacion = anyoPublicacion
        self.paginas = [None] * (999)
        i = 0
        while (i < 999) :
            self.paginas[i] = Pagina("", 0)
            i += 1
        self.numeroPaginas = 0
    def  getTitulo(self) :
        return self.titulo
    def setTitulo(self, titulo) :
        self.titulo = titulo
    def  getIsbn(self) :
        return self.isbn
    def setIsbn(self, nuevo_isbn) :
        self.isbn = nuevo_isbn
    def  getAutor(self) :
        return self.autor
    def setAutor(self, nuevo_autor) :
        self.autor = nuevo_autor
    def  getAnyoPublicacion(self) :
        return self.anyoPublicacion
    def setAnyoPublicacion(self, nuevo_anyoPublicacion) :
        self.anyoPublicacion = nuevo_anyoPublicacion
    def  getNumeroPaginas(self) :
        return self.numeroPaginas
    def anyadirPagina(self, nueva_pagina) :
        if (self.numeroPaginas < 999) :
            self.paginas[self.numeroPaginas] = nueva_pagina
            self.numeroPaginas += 1
    def  getPaginaNumero(self, numero_pagina) :
        i = 0
        while (i < self.numeroPaginas) :
            if (self.paginas[i].getNumero() == numero_pagina) :
                return self.paginas[i]
            i += 1
        return None
class Principal_EjemploLibroPagina :
    def main( args) :
        el_quijote = Libro("Don Quijote de la Mancha", 1234567890, "Miguel de Cervantes", 1605)
        pagina1 = Pagina("En un lugar de la Mancha, de cuyo nombre ...", 1)
        pagina2 = Pagina("...no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor...", 2)
        el_quijote.anyadirPagina(pagina1)
        el_quijote.anyadirPagina(pagina2)
        i = 1
        while (i <= el_quijote.getNumeroPaginas()) :
            print(el_quijote.getPaginaNumero(i).getContenido())
            i += 1
    

if __name__=="__main__":
    Principal_EjemploLibroPagina.main([])