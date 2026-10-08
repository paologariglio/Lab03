import csv
from cmath import nan
from errno import ENOMEM
from operator import attrgetter
from sys import exception


class Strumenti:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.__id_strumento = id_strumento
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore
    @property
    def marca(self):
        return self.__marca
    @property
    def id_strumento(self):
        return self.__id_strumento

    def __str__(self):
        return f"{self.__id_strumento},{self.__tipo},{self.__marca},{self.__anno_acquisto},{self.__valore}"

class Prestiti:
    def __init__(self, data, id_strumento, cognome_allievo, id_prestito):
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo
        self.__id_prestito = id_prestito
    @property
    def id_strumento(self):
        return self.__id_strumento
    @property
    def id_prestito(self):
        return self.__id_prestito
    def __str__(self):
        return f"Prestito {self.__id_prestito}:{self.__cognome_allievo},{self.__id_strumento},{self.__data}"

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = { }
        self.prestiti = { }

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r", encoding= "utf-8") as infile:
                reader = csv.reader(infile)
                for line in reader:
                    id_strumento = line[0]
                    tipo = line[1]
                    marca = line[2]
                    anno_acquisto = line[3]
                    valore = line[4]
                    nuovo_strumento = Strumenti(id_strumento, tipo, marca, anno_acquisto, valore)
                    self.strumenti[id_strumento] = nuovo_strumento
        except FileNotFoundError:
            print(f"File {file_path} non trovato")


        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        id_strumento = "S" + str(len(self.strumenti)+1)
        strumento_tastiera = Strumenti(id_strumento, tipo, marca, anno_acquisto, valore)
        self.strumenti[id_strumento] = strumento_tastiera
        return self.strumenti[id_strumento]

        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        ordinati = sorted(self.strumenti.values(), key=attrgetter('marca'))
        return ordinati
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception("strumento non trovato")
        for strumento in self.prestiti.values():
            if strumento.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito")
        id_prestito = "P" + str(len(self.prestiti)+1)
        nuovo_prestito = Prestiti(data, id_strumento, cognome_allievo, id_prestito)
        self.prestiti[id_prestito] = nuovo_prestito
        return nuovo_prestito

        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception("prestito non trovato")
        else:
            self.prestiti.pop(id_prestito)
        # TODO
