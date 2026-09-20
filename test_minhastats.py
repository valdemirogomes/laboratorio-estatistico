import numpy as np
import minhastats as ms
D=np.random.default_rng(0).gamma(2,9,500).tolist()
def test_media(): assert np.isclose(ms.media(D),np.mean(D),rtol=1e-9)
def test_mediana(): assert np.isclose(ms.mediana(D),np.median(D))
def test_variancias():
    assert np.isclose(ms.variancia(D,True),np.var(D,ddof=1),rtol=1e-9)
    assert np.isclose(ms.variancia(D,False),np.var(D,ddof=0),rtol=1e-9)
def test_percentil(): assert np.isclose(ms.percentil(D,25),np.percentile(D,25),rtol=1e-6)
def test_cov_corr():
    x=D[:100]; y=[2*a+3 for a in x]
    assert np.isclose(ms.covariancia(x,y),np.cov(x,y,ddof=1)[0,1])
    assert np.isclose(ms.correlacao(x,y),np.corrcoef(x,y)[0,1])
def test_regressao():
    x=[1,2,3,4]; y=[5,7,9,11]; b0,b1,r2=ms.regressao_linear(x,y)
    assert np.isclose(b0,3) and np.isclose(b1,2) and np.isclose(r2,1)
