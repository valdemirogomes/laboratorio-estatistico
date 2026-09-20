import math, random
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import minhastats as ms

st.set_page_config(page_title='Laboratório Estatístico Interativo',layout='wide')
st.title('📊 Laboratório Estatístico Interativo')
st.caption('Matemática e Estatística para Computação — medidas exibidas calculadas pelo núcleo próprio minhastats.py')

@st.cache_data
def carregar(): return pd.read_csv('dados/dataset.csv')
df=carregar(); nums=list(df.select_dtypes(include='number').columns); cats=list(df.select_dtypes(exclude='number').columns)
mod=st.sidebar.radio('Módulo',['0 — Dataset','1/2 — Descritiva','3 — LGN e TCL','4 — Distribuições','5 — Correlação e regressão','6 — Descobertas'])

if mod=='0 — Dataset':
    st.header('Módulo 0 — Dataset'); st.write(f'{len(df)} registros, {len(nums)} variáveis numéricas e {len(cats)} categóricas.'); st.dataframe(df.head(30),use_container_width=True)
    st.write('Nulos por coluna:'); st.dataframe(df.isna().sum().to_frame('nulos'))
elif mod=='1/2 — Descritiva':
    st.header('Módulos 1 e 2 — Estatística descritiva interativa'); col=st.selectbox('Variável numérica',nums); d=df[col].dropna().tolist()
    q1,q2,q3=ms.quartis(d); iqr=q3-q1; outs=[x for x in d if x<q1-1.5*iqr or x>q3+1.5*iqr]
    c1,c2,c3,c4=st.columns(4); c1.metric('Média',f'{ms.media(d):.2f}'); c2.metric('Mediana',f'{ms.mediana(d):.2f}'); c3.metric('Desvio amostral',f'{ms.desvio_padrao(d):.2f}'); c4.metric('CV',f'{ms.coef_variacao(d):.1f}%')
    st.write(f'Q1={q1:.2f} | Q3={q3:.2f} | amplitude={ms.amplitude(d):.2f} | outliers (IQR): {len(outs)}')
    dif=ms.media(d)-ms.mediana(d); lim=.5*ms.desvio_padrao(d)
    st.info('Assimetria à direita: valores altos puxam a média.' if dif>lim else 'Assimetria à esquerda: valores baixos puxam a média.' if dif<-lim else 'Distribuição aproximadamente simétrica pela regra automática do projeto.')
    k=max(1,round(1+3.322*math.log10(len(d)))); fig,ax=plt.subplots(); ax.hist(d,bins=k); ax.set_title(f'Histograma — Sturges (k={k})'); st.pyplot(fig)
    fig,ax=plt.subplots(); ax.boxplot(d,vert=False); ax.set_title('Boxplot'); st.pyplot(fig)
    if cats:
        cat=st.selectbox('Variável categórica',cats); st.bar_chart(df[cat].value_counts().head(15))
elif mod=='3 — LGN e TCL':
    st.header('Módulo 3 — Lei dos Grandes Números e Teorema Central do Limite'); n=st.slider('Lançamentos da moeda',100,10000,3000,100); lanc=np.random.default_rng().integers(0,2,n); freq=np.cumsum(lanc)/np.arange(1,n+1)
    fig,ax=plt.subplots(); ax.plot(range(1,n+1),freq); ax.axhline(.5,linestyle='--'); ax.set_xscale('log'); ax.set_ylim(0,1); ax.set_title('LGN — frequência relativa converge para 0,5'); st.pyplot(fig)
    col=st.selectbox('Variável do dataset para TCL',nums); d=df[col].dropna().tolist(); tam=st.slider('Tamanho da amostra',2,min(100,len(d)),30); reps=st.slider('Repetições',100,3000,1000,100)
    rng=random.Random(); medias=[ms.media(rng.choices(d,k=tam)) for _ in range(reps)]; fig,ax=plt.subplots(); ax.hist(medias,bins=30,density=True); mu=ms.media(medias); sd=ms.desvio_padrao(medias); xs=np.linspace(min(medias),max(medias),200); ax.plot(xs,stats.norm.pdf(xs,mu,sd)); ax.set_title('TCL — distribuição das médias amostrais'); st.pyplot(fig)
elif mod=='4 — Distribuições':
    st.header('Módulo 4 — Distribuições teóricas'); col=st.selectbox('Variável',nums); d=df[col].dropna().tolist(); dist=st.selectbox('Distribuição',['Normal','Exponencial','Uniforme','Poisson'])
    fig,ax=plt.subplots(); ax.hist(d,bins=30,density=True,alpha=.5); xs=np.linspace(min(d),max(d),300); m=ms.media(d); s=ms.desvio_padrao(d)
    if dist=='Normal': ax.plot(xs,stats.norm.pdf(xs,m,s)); txt=f'Normal(μ={m:.2f}, σ={s:.2f})'
    elif dist=='Exponencial':
        lam=1/m; ax.plot(xs,stats.expon.pdf(xs,scale=1/lam)); txt=f'Exponencial(λ={lam:.4f})'
    elif dist=='Uniforme': ax.plot(xs,stats.uniform.pdf(xs,loc=min(d),scale=max(d)-min(d))); txt=f'Uniforme(a={min(d):.2f}, b={max(d):.2f})'
    else:
        vals=range(max(0,int(min(d))),int(max(d))+1); ax.plot(list(vals),stats.poisson.pmf(list(vals),m),'o'); txt=f'Poisson(λ={m:.2f}) — apropriada sobretudo para contagens.'
    ax.set_title(txt); st.pyplot(fig); st.warning('O ajuste visual deve ser discutido criticamente; um ajuste ruim também é resultado relevante.')
else:
    if mod=='5 — Correlação e regressão':
        st.header('Módulo 5 — Correlação e regressão'); xcol=st.selectbox('X',nums); ycol=st.selectbox('Y',[c for c in nums if c!=xcol]); tmp=df[[xcol,ycol]].dropna(); x=tmp[xcol].tolist(); y=tmp[ycol].tolist(); r=ms.correlacao(x,y); b0,b1,r2=ms.regressao_linear(x,y); st.write(f'Pearson r = **{r:.4f}** | ŷ = **{b0:.4f} + {b1:.4f}·x** | R² = **{r2:.4f}**'); st.info(f'Cada unidade a mais de {xcol} está associada, em média, a {b1:.4f} unidades de variação em {ycol}. Correlação não implica causalidade.')
        fig,ax=plt.subplots(); ax.scatter(x,y,s=10); xx=np.linspace(min(x),max(x),100); ax.plot(xx,[b0+b1*v for v in xx]); st.pyplot(fig); xp=st.number_input('X para predição',min_value=float(min(x)),max_value=float(max(x)),value=float(ms.media(x))); st.success(f'Predição dentro da faixa observada: ŷ = {b0+b1*xp:.3f}')
    else:
        st.header('Módulo 6 — Três descobertas do dataset'); st.markdown('**1. Relação entre estudo e desempenho:** compare `study_hours` e `exam_score` no módulo de regressão e quantifique r e R².\n\n**2. Contraste entre grupos:** use `course` ou `study_method` para observar diferenças de desempenho entre categorias.\n\n**3. Pontos fora da curva:** no módulo descritivo, escolha `study_hours`, `sleep_hours` ou `exam_score` e investigue os outliers detectados pela regra do IQR.'); st.caption('As conclusões finais devem registrar número/gráfico e limite: associação não é causalidade e este dataset é demonstrativo.')
