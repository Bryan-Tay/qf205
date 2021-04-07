import numpy as np

def Implicit(S, K, r, q, T, sigma, M, N=1, call=1):
    delta_t=T/N
    S_max=2*K
    delta_S=S_max/M
    k=np.floor(int(S/delta_S))
    
    #creating A
    A = np.zeros((M+1,M+1))
    A[0,0] = 1
    A[M,M] = 1        

    for i in range(1,M):
        for j in range(0,M+1):
            a = 0.5*delta_t*((r-q)*j-((sigma**2)*(j**2)))
            b = 1+delta_t*((sigma**2)*(j**2)+r)
            c = -0.5*delta_t*((sigma**2)*(j**2)+(r-q)*j)
            
            if i-j==1:
                A[i,j]=a
                A[i,j+1]=b
                A[i,j+2]=c

    #creating A inv               
    Ainv = np.linalg.pinv(A) 
    
    #creating Fc call
    Fc = np.zeros((M+1,1))
    Fp = np.zeros((M+1,1))

    #for call
    if call == 1:
        for j in range(M+1):
            Fc[j,0] = max(((j*delta_S)-K),0)
        for i in range(N-1,-1,-1):
            Fc[0,0] = 0
            Fc[M,0] = S_max-K*np.exp((-r)*(N-i)*(delta_t))
            Fc = Ainv.dot(Fc)
        OptionPrice = Fc[int(k),0] + ((Fc[int(k+1),0] - Fc[int(k),0])/(delta_S))*(S - (int(k)*delta_S))
    #for put   
    else:    
        for j in range(M+1):    
            Fp[j,0] = max(K-(j*delta_S),0)
    
        for i in range(N-1,-1,-1):
            Fp[0,0] = K*np.exp((-r)*(N-i)*(delta_t))
            Fp[M,0] = 0
            Fp = Ainv.dot(Fp)
        OptionPrice = Fp[int(k),0] + ((Fp[int(k+1),0] - Fp[int(k),0])/(delta_S))*(S - (int(k)*delta_S))

    return OptionPrice