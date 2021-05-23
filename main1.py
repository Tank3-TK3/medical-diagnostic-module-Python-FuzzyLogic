###################################################################################################
#                                            <MODULES>
import numpy as np
import random
###################################################################################################
#                                             <CLASS>
class MedicalDiagnosticModule():
    def __init__( self ):
        self.preloadedmatrix = np.array(
            [
                [0.8, 0  , 0.6, 0  , 0.4, 0  , 0  , 0.6, 0.8, 0.7, 0.8, 0.6, 0  , 0  , 0  ],
                [0  , 0.6, 0.8, 0.8, 0.7, 0  , 0  , 0.4, 0.6, 0.5, 0.4, 0.7, 0  , 0  , 0.5],
                [0  , 0.8, 0.4, 0.7, 0.5, 0  , 0  , 0.7, 0  , 0.7, 0.5, 0  , 0  , 0.4, 0  ],
                [0  , 0.2, 0.9, 0.5, 0.7, 0.8, 0  , 0.4, 0  , 0  , 0.9, 0  , 0  , 0  , 0  ],
                [0  , 0  , 0.8, 0.3, 0.7, 0  , 0  , 0.7, 0.5, 0.7, 0.7, 0  , 0  , 0  , 0  ],
                [0.9, 0.6, 0.5, 0.4, 0.6, 0.9, 0  , 0.8, 0.7, 0.2, 0.8, 0.5, 0  , 0  , 0  ],
                [0  , 0  , 0.4, 0  , 0.7, 0  , 0  , 0.6, 0.9, 0.6, 0  , 0  , 0.8, 0  , 0.9],
                [0.7, 0.7, 0.8, 0.9, 0.5, 0.5, 0  , 0.6, 0.7, 0.4, 0.6, 0.6, 0  , 0.6, 0  ],
                [0  , 0  , 0.5, 0.6, 0.8, 0  , 0.8, 0.6, 0.9, 0.6, 0  , 0.8, 0  , 0  , 0  ],
                [0  , 0.6, 0.9, 0  , 0.6, 0  , 0  , 0.7, 0.9, 0.9, 0  , 0.8, 0  , 0  , 0  ]
            ] , dtype=np.float64 )
        self.intersectionmatrix = np.zeros( ( 10 , 16 ) , dtype=np.float64 )
        self.usersymptoms = np.zeros( ( 1 , 15 ) , dtype=np.float64 )
        self.indexdoc = 0

    def generateSymptoms( self ):
        for i in range( 0 , len( self.usersymptoms[0] ) ):
            self.usersymptoms[0][i] = random.random()
    
    def intersectMatrix( self ):
        for i in range( 0 , self.preloadedmatrix.shape[0] ):
            for j in range( 0 , self.preloadedmatrix.shape[1] ):
                if self.preloadedmatrix[i][j] >= self.usersymptoms[0][j]:
                    self.intersectionmatrix[i][j] = self.usersymptoms[0][j]
                else:
                    self.intersectionmatrix[i][j] = self.preloadedmatrix[i][j]
        for i in range( 0 , self.intersectionmatrix.shape[0] ):
            for j in range( 0 , self.intersectionmatrix.shape[1]-1 ):
                self.intersectionmatrix[i][15] += self.intersectionmatrix[i][j]
###################################################################################################
#                                             <MAIN>
if __name__ == '__main__':
    mdm = MedicalDiagnosticModule()
    mdm.generateSymptoms()
    mdm.intersectMatrix()
