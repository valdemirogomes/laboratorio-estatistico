"""Núcleo estatístico implementado sem funções estatísticas prontas."""

def _validar(dados):
    if len(dados) == 0: raise ValueError('sequencia vazia')

def media(dados):
    _validar(dados); return sum(dados)/len(dados)

def mediana(dados):
    _validar(dados); v=sorted(dados); n=len(v); m=n//2
    return v[m] if n%2 else (v[m-1]+v[m])/2

def moda(dados):
    _validar(dados); c={}
    for x in dados: c[x]=c.get(x,0)+1
    mx=max(c.values()); return [x for x,n in c.items() if n==mx]

def amplitude(dados):
    _validar(dados); return max(dados)-min(dados)

def variancia(dados, amostral=True):
    _validar(dados); n=len(dados)
    if amostral and n<2: raise ValueError('variancia amostral exige n >= 2')
    m=media(dados); return sum((x-m)**2 for x in dados)/(n-1 if amostral else n)

def desvio_padrao(dados, amostral=True): return variancia(dados, amostral)**0.5

def percentil(dados,p):
    _validar(dados)
    if not 0<=p<=100: raise ValueError('percentil deve estar entre 0 e 100')
    v=sorted(dados); pos=p*(len(v)-1)/100; lo=int(pos); hi=min(lo+1,len(v)-1); f=pos-lo
    return v[lo]+f*(v[hi]-v[lo])

def quartis(dados): return percentil(dados,25),percentil(dados,50),percentil(dados,75)

def coef_variacao(dados, percentual=True):
    m=media(dados)
    if abs(m)<1e-15: raise ValueError('media zero: CV indefinido')
    cv=desvio_padrao(dados)/m; return cv*100 if percentual else cv

def covariancia(x,y,amostral=True):
    if len(x)!=len(y): raise ValueError('vetores com tamanhos diferentes')
    _validar(x); n=len(x)
    if amostral and n<2: raise ValueError('covariancia amostral exige n >= 2')
    mx,my=media(x),media(y); return sum((a-mx)*(b-my) for a,b in zip(x,y))/(n-1 if amostral else n)

def correlacao(x,y):
    sx,sy=desvio_padrao(x),desvio_padrao(y)
    if sx==0 or sy==0: raise ValueError('correlacao indefinida para variavel constante')
    return covariancia(x,y)/(sx*sy)

def regressao_linear(x,y):
    if len(x)!=len(y) or len(x)<2: raise ValueError('regressao exige vetores de mesmo tamanho e n >= 2')
    mx,my=media(x),media(y); den=sum((xi-mx)**2 for xi in x)
    if den==0: raise ValueError('x constante: regressao indefinida')
    b1=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))/den; b0=my-b1*mx
    yhat=[b0+b1*xi for xi in x]; sq_res=sum((yi-yh)**2 for yi,yh in zip(y,yhat)); sq_tot=sum((yi-my)**2 for yi in y)
    r2=1-sq_res/sq_tot if sq_tot else 1.0
    return b0,b1,r2
