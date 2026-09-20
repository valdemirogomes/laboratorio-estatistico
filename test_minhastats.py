import numpy as np
import minhastats as ms

RNG=np.random.default_rng(0)
D=RNG.gamma(2,9,500).tolist()

def test_media(): assert np.isclose(ms.media(D),np.mean(D),rtol=1e-9)
def test_mediana(): assert np.isclose(ms.mediana(D),np.median(D),rtol=1e-9)
def test_moda(): assert set(ms.moda([1,1,2,2,3])) == {1,2}
def test_amplitude(): assert np.isclose(ms.amplitude(D),np.ptp(D))
def test_variancia_amostral(): assert np.isclose(ms.variancia(D,True),np.var(D,ddof=1),rtol=1e-9)
def test_variancia_populacional(): assert np.isclose(ms.variancia(D,False),np.var(D,ddof=0),rtol=1e-9)
def test_desvio_amostral(): assert np.isclose(ms.desvio_padrao(D,True),np.std(D,ddof=1),rtol=1e-9)
def test_desvio_populacional(): assert np.isclose(ms.desvio_padrao(D,False),np.std(D,ddof=0),rtol=1e-9)
def test_percentis_quartis():
    for p in [0,25,50,75,100]: assert np.isclose(ms.percentil(D,p),np.percentile(D,p),rtol=1e-6)
def test_coef_variacao(): assert np.isclose(ms.coef_variacao(D),np.std(D,ddof=1)/np.mean(D)*100,rtol=1e-9)
def test_covariancia():
    x=D[:100]; y=[2*a+3 for a in x]
    assert np.isclose(ms.covariancia(x,y),np.cov(x,y,ddof=1)[0,1],rtol=1e-9)
def test_correlacao():
    x=D[:100]; y=[2*a+3 for a in x]
    assert np.isclose(ms.correlacao(x,y),np.corrcoef(x,y)[0,1],rtol=1e-9)
def test_regressao():
    x=[1,2,3,4]; y=[5,7,9,11]; b0,b1,r2=ms.regressao_linear(x,y)
    assert np.isclose(b0,3) and np.isclose(b1,2) and np.isclose(r2,1)
