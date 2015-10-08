import numpy as np

sobel_Fst = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_Snd = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

previt_Fst = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
previt_Snd = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])


edge_detection_dict = { 'sobel': (sobel_Fst, sobel_Snd), 'previt': (previt_Fst, previt_Snd) }

blur = np.array([[1.,2,1],[2,4,2],[1,2,1]])
blur5 = np.array([[1.,4,7,4,1], [4,16,26,16,4], [7,26,41,26,7], [1,4,7,4,1], [4,16,26,16,4]])
clarify = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
noize = np.array([[1,1,1],[1,1,1],[1,1,1]])
edges = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

kernel_dict = { 'blur': blur, 'blur5': blur5, 'clarify': clarify, 'noize': noize, 'edges': edges }