import numpy as np

sobel_Fst = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_Snd = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

previt_Fst = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
previt_Snd = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])


edgeDetection_Dict = { 'sobel': (sobel_Fst, sobel_Snd), 'previt': (previt_Fst, previt_Snd) }