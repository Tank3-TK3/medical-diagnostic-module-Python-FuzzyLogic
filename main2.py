import numpy as np
import sys
import json

class MDM():
    matrizprecargada = None
    matrizinterseccion = None
    resultadosdiagnosticos = None
    sintomasusuario = []
    listaenfermedades = []

    def __init__(self):
        self.matrizinterseccion = np.zeros((10,16))
        self.resultadosdiagnosticos = np.zeros((1,10))
        self.matrizprecargada=np.array(
            [
                [0.5,0.0,0.9,0.8,0.8,0.0,0.0,0.6,0.0,0.0,0.0,0.4,0.0,0.0,0.0],
                [0.6,0.0,0.0,0.0,0.5,0.7,0.0,0.0,0.0,0.0,0.0,0.0,0.7,0.0,0.0],
                [0.9,0.3,0.8,0.8,0.0,0.0,0.5,0.6,0.0,0.0,0.0,0.7,0.0,0.5,0.0],
                [0.9,0.7,0.7,0.0,0.0,0.0,0.6,0.9,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                [0.0,0.0,0.9,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.9,0.0,0.0,0.0],
                [0.0,0.0,0.3,0.0,0.5,0.0,0.0,0.0,0.0,0.0,0.8,0.7,0.0,0.0,0.0],
                [0.4,0.7,0.9,0.6,0.0,0.0,0.6,0.0,0.0,0.0,0.0,0.3,0.5,0.0,0.0],
                [0.3,0.0,0.7,0.8,0.0,0.0,0.5,0.0,0.0,0.0,0.6,0.9,0.0,0.0,0.4],
                [0.0,0.0,0.8,0.7,0.0,0.0,0.0,0.0,0.0,0.7,0.5,0.6,0.0,0.0,0.6],
                [0.0,0.0,0.5,0.5,0.3,0.0,0.7,0.0,0.9,0.4,0.7,0.7,0.0,0.9,0.0]
            ])

    def diagnosticoG(self):
        for a in range(0,self.matrizprecargada.shape[0]):
            for b in range(0,self.matrizprecargada.shape[1]):
                if self.matrizprecargada[a][b] >= self.sintomasusuario[0][b]:
                    self.matrizinterseccion[a][b] = self.sintomasusuario[0][b]
                else:
                    self.matrizinterseccion[a][b] = self.matrizprecargada[a][b]
        for a in range(0,self.matrizinterseccion.shape[0]):
            for b in range(0,self.matrizinterseccion.shape[1]-1):
                self.matrizinterseccion[a][15] += self.matrizinterseccion[a][b]
            self.resultadosdiagnosticos[0][a] = self.matrizinterseccion[a][15]

    def procesamientoARGV(self,m):
        m = sys.argv[1]
        m = m.replace(' ','')
        m = m.replace(' ','')
        m = m.replace('[[','')
        m = m.replace(']]','')
        m = m.split('],[')
        try:
            self.sintomasusuario = np.array([m[0].split(',')],dtype=np.float64)
        except:
            print('>LOS VALORES NO SE PUEDEN CONVERTIR <(Los valores de los síntomas son incorrectos)')
            exit()
        self.listaenfermedades = np.array(m[1].split( ',' ))

    def diagnosticoE(self):
        self.diagnosticoG()
        for indice in range(0,10):
            if str(indice) not in self.listaenfermedades:
                self.resultadosdiagnosticos[0][indice] = -1

modulo = MDM()
try:
    if len(sys.argv[1]) > 1:
        modulo.procesamientoARGV(sys.argv[1])
except:
    print('>ARGUMENTOS NO RECIBIDOS<')
    exit()
if modulo.listaenfermedades[0] == '':
    try:
        modulo.diagnosticoG()
    except:
        print('>ARGUMENTOS NO VÁLIDOS RECIBIDOS<')
        exit()
else:
    modulo.diagnosticoE()
print(json.dumps(modulo.resultadosdiagnosticos[0].tolist()))
