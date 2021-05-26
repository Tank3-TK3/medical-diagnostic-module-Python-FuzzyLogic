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
        self.diagnosisresult = np.zeros( ( 1 , 10 ) , dtype=np.float64 )
        self.usersymptoms = []
        self.listdiseases = []

    def processARGV( self , matrix ):
        matrix = sys.argv[1]
        matrix = matrix.replace( ' ' , '' )
        matrix = matrix.replace( ' ' , '' )
        matrix = matrix.replace( '[[' , '' )
        matrix = matrix.replace( ']]' , '' )
        matrix = matrix.split( '],[' )
        try:
            self.usersymptoms = np.array( [matrix[0].split( ',' )] , dtype=np.float64 )
        except ValueError:
            print( '>VALUES CANNOT BE CONVERTED< (Symptom values are incorrect)' )
            exit()
        self.listdiseases = np.array( matrix[1].split( ',' ) )

    def generalDiagnosis( self ):
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

    def specificDiagnosis( self ):
        self.generalDiagnosis()
        for i in range( 0 , 10 ):
            if str( i ) not in self.listdiseases:
                self.diagnosisresult[0][i] = -1
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
    if mdm.listdiseases[0] == '':
        try:
            mdm.generalDiagnosis()
        except IndexError:
            print( '>INVALID ARGUMENTS RECEIVED<' )
            exit()
    else:
        mdm.specificDiagnosis()
    print( json.dumps( mdm.diagnosisresult[0].tolist() ) )
