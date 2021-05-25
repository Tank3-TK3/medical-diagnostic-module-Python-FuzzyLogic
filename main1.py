###################################################################################################
#                                            <MODULES>
import sys
import json
import numpy as np
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
        self.usersymptoms = []
        self.listdiseases = []
        self.diagnosisresult = np.zeros( ( 1 , 10 ) , dtype=np.float64 )
        self.indexdoc = 0

    def processARGV( self , matrix ):
        matrix = sys.argv[1]
        matrix = matrix.replace( '[[' , '' )
        matrix = matrix.replace( ']]' , '' )
        matrix = matrix.split( '],[' )
        try:
            self.usersymptoms = np.array( [matrix[0].split( ',' )] , dtype=np.float64 )
        except ValueError:
            print( '>VALUES CANNOT BE CONVERTED TO FLOATS<' )
            exit()
        self.listdiseases = np.array( matrix[1].split( ',' ) )

    def generatesDiagnosis( self ):
        for i in range( 0 , self.preloadedmatrix.shape[0] ):
            for j in range( 0 , self.preloadedmatrix.shape[1] ):
                if self.preloadedmatrix[i][j] >= self.usersymptoms[0][j]:
                    self.intersectionmatrix[i][j] = self.usersymptoms[0][j]
                else:
                    self.intersectionmatrix[i][j] = self.preloadedmatrix[i][j]
        for i in range( 0 , self.intersectionmatrix.shape[0] ):
            for j in range( 0 , self.intersectionmatrix.shape[1]-1 ):
                self.intersectionmatrix[i][15] += self.intersectionmatrix[i][j]
            self.diagnosisresult[0][i] = self.intersectionmatrix[i][15]
        return json.dumps(self.diagnosisresult[0].tolist())
###################################################################################################
#                                             <MAIN>
if __name__ == '__main__':
    mdm = MedicalDiagnosticModule()
    try:
        if len( sys.argv[1] ) > 1 :
            mdm.processARGV( sys.argv[1] )
    except IndexError:
        print( '>ARGUMENTS NOT RECEIVED<' )
        exit()
    try:
        print( mdm.generatesDiagnosis() )
    except IndexError:
        print( '>INVALID ARGUMENTS RECEIVED<' )
        exit()
