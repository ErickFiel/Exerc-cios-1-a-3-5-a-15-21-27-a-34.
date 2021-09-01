#!/usr/bin/env python
# coding: utf-8

# # Exercícios: 1 a 3, 5 a 15, 21, 27 a 34. 
# **1) Um computador possui uma memória principal com capacidade para
# armazenar palavras de 16 bits em cada uma de suas N células, e o seu
# barramento de endereços tem 12 bits de tamanho. Sabendo-se que em cada
# célula pode-se armazenar o valor exato de uma palavra, quantos bytes poderão
# ser armazenados nessa memória?**

# In[1]:


#Analizando a questão temos:
#Palavras de 16 bits
#BE tem 12 bits de tamanho
#Cada célula pode-se armazenar o valor exato de uma palavra
import math
Palavra= 16
BE= 12
E= BE
M= Palavra
Bytes= Palavra/8
N= 2**E
MP= N*Bytes
print("Poderão ser armazenados nessa memória",MP,"ou 8K bytes")


# **2) O que você entende por acesso à memória? Caracterize o tempo de acesso nos diversos tipos de memória.**
# 
# **Resposta:** O acesso aos dados armazenados em uma memória. O tempo de acesso é o tempo
# que a memória gasta para colocar uma informação na barra de dados após uma
# determinada posição ter sido endereçada.

# **3) Quais são as possíveis operações que podem ser realizadas em uma memória?**
# 
# **Resposta:** São duas, a operação de escrita, que é a ação de guardar um elemento (ou um grupo
# de elementos), e a operação de leitura que é realizada para a consecução desta ação
# de armazenamento.

# **5) Qual é a diferença, em termos de endereço, conteúdo e total de bits, entre as
# seguintes organizações de MP:**
# 
# **a) memória A: 32K célula de 8 bits cada;**

# In[2]:


#Analizando a questão temos:
#Célula 32K= 2^5.2^10= 2^15
#Cada célula de 8 bits
import math
N= 2**15
M= 8
E= math.log2(N)
Conteúdo= 8
T= N*M
print("O endereço é de",E,"bits, o conteúdo é de",Conteúdo,"e o total de bits é de",T,"ou 256K bits")


# **b) memória B: 16K célula de 16 bit cada; e:**

# In[3]:


#Analizando a questão temos:
#Célula 16K= 2^4.2^10= 2^14
#Cada célula de 16 bits
import math
N= 2**14
M= 16
E= math.log2(N)
Conteúdo= 16
T= N*M
print("O endereço é de",E,"bits, o conteúdo é de",Conteúdo,"e o total de bits é de",T,"ou 256K bits")


# **c) memória C: 16k célula de 8 bits cada.**

# In[4]:


#Analizando a questão temos:
#Célula 16K= 2^4.2^10= 2^14
#Cada célula de 8 bits
import math
N= 2**14
M= 8
E= math.log2(N)
Conteúdo= 8
T= N*M
print("O endereço é de",E,"bits, o conteúdo é de",Conteúdo,"e o total de bits é de",T,"ou 128K bits")


# **6) Qual a função do registrador de endereços de memória (REM)? E do
# registrador de dados de memória (RDM)?**
# 
# **Resposta:** O registrador de endereços de memória (REM) armazena temporariamente o
# endereço de acesso a uma posição de memória, ao se iniciar uma operação de leitura
# ou de escrita. O registrador de dados de memória (RDM) armazena temporariamente
# a informação que está sendo transferida da MP para o processador ou do processador
# para a MP.

# **7) Descreva os barramentos que interligam processador e MP, indicando função
# e direção do fluxo de sinais de cada um.**
# 
# **Resposta:** Barramento de dados- Interliga o RDM a MP, para transferência de informações entre
# MP e processador. Sua direção do fluxo é bidimensional, ou seja, ora os sinais
# percorrem o barramento do processador para a MP, ora percorrem o caminho inverso.
# Barramento de endereços- Interliga o REM (MAR) a MP para transferência dos bits
# que representam um determinado endereço. Sua direção de fluxo é unidirecional, já
# que somente o processador aciona a MP para a realização de operações de escrita ou
# leitura.
# Barramento de controle- Interliga o processador a MP para passagem de sinais de
# controle durante uma operação de leitura ou escrita. Sua direção de fluxo é
# bidirecional, já que o processador pode enviar sinais de controle para a MP, como
# sinal indicador de que a operação é de leitura ou de escrita, e a MP pode enviar sinais
# do tipo WAIT, além de uma infinidade de outros sinais.

# **8) Descreva passo a passo uma operação de leitura. Utilize um diagrama
# esquemático.**
# 
# 1) REM &lt;- de outro registrador do processador
# 
# 1.a) O endereço é colocado no barramento de endereços
# 
# 2) Sinal de leitura no barramento de controle
# 
# 2.a) Decodificação do endereço e localização da célula (controlador de memória)
# 
# 3) RDM &lt;- MP(REM) pelo barramento de dados
# 
# 4) Para outro registrador do processador &lt;- RDM

# **9) Faça o mesmo para uma operação de escrita.**
# 
# 1) (REM) &lt;- (outro registrador)
# 
# 1.a) O endereço é colocado no barramento de endereços
# 
# 2) (RDM) &lt;- (outro registrador)
# 
# 3) Sinal de escrita
# 
# 4) (MP(REM) &lt;- (RDM)

# **10) Um computador possui um RDM com 16 bits de tamanho e um REM com
# capacidade para armazenar números com 20 bits. sabe-se que a célula desse
# computador armazena dados com 8 bits de tamanho e que ele possui uma
# quantidade N de células, igual à capacidade máxima de armazenamento.
# Pergunta-se:**
# 
# **a) Qual é o tamanho do barramento de endereço?**

# In[8]:


#Analizando a questão temos:
#RDM com 16 bits
#REM com capacidade para armazenar números com 20 bits
#A célula desse computador armazena dados com 8 bits de tamanho
#A quantidade N de células é igual à capacidade máxima de armazenamento
REM= 20
E= REM
BE= E
print("O tamanho do barramento de endereço é de",BE,"bits")


# **b) Quantas células de memória são lidas em uma única operação de leitura?**

# In[6]:


#Analizando a questão temos:
#RDM com 16 bits
#REM com capacidade para armazenar números com 20 bits
#A célula desse computador armazena dados com 8 bits de tamanho
#A quantidade N de células é igual à capacidade máxima de armazenamento
RDM= 16
M= 8
Células_lidas= RDM/M
print("São lidas",Células_lidas,"células")


# **c) Quanto bits tem a memória principal?**

# In[7]:


#Analizando a questão temos:
#RDM com 16 bits
#REM com capacidade para armazenar números com 20 bits
#A célula desse computador armazena dados com 8 bits de tamanho
#A quantidade N de células é igual à capacidade máxima de armazenamento
E= 20
M= 8
N=2**E
MP= N*M
print("A memória principal tem",MP,"ou 8M bits")


# **11) Um microcomputador possui uma capacidade máxima de memória principal
# (RAM) com 32K células, cada uma capaz de armazenar uma palavra de 8 bits.
# Pergunta-se:**
# 
# **a) Qual é o maior endereço, em decimal, dessa memória?**

# In[3]:


#Analizando a questão temos:
#MP com 32K células = 2^5.2^10= 2^15
#Palavra de 8 bits
import math
N= 2**15
E= math.log2(N)
print("Como temos",E,"bits de endereço o maior endereço é 111111111111111 que em decimal é 32767")


# **b) Qual é o tamanho do barramento de endereços desse sistema?**

# In[2]:


#Analizando a questão temos:
#MP com 32K células = 2^5.2^10= 2^15
#Palavra de 8 bits
import math
N= 2**15
E= math.log2(N)
BE= E
print("O tamanho do barramento de endereços é de",BE,"bits")


# **c) Quantos bits podem ser armazenados no RDM e no REM?**

# In[4]:


#Analizando a questão temos:
#MP com 32K células = 2^5.2^10= 2^15
#Palavra de 8 bits
import math
N= 2**15
M= 8
E= math.log2(N)
BE= E
BD= M
REM= BE
RDM= BD
print("No RDM podem ser armazenados",RDM,"bits e no REM",REM,"bits")


# **d) Qual é o total máximo de bits que pode existir nesta memória?**

# In[5]:


#Analizando a questão temos:
#MP com 32K células = 2^5.2^10= 2^15
#Palavra de 8 bits
import math
N= 2**15
M= 8
T= N*M
print("O total máximo de bits nesta memória é de",T,"ou 256K bits")


# **12) Considere uma célula de uma MP cujo endereço é, em hexadecimal, 2C81 e
# que tem armazenado em seu conteúdo um valor igual a, em hexadecimal, F5A.
# Sabe-se que, neste sistema as células têm o mesmo tamanho da palavra e que
# em cada acesso é lido o valor de uma célula. Pergunta-se:**
# 
# **a) Qual deve ser o tamanho do REM e do RDM nesse sistema?**

# In[15]:


#Analizando a questão temos:
#Uma MP cujo endereço em hexadecimal é 2C81
#Seu conteúdo tem um valor em hexadecimal de F5A
#Células têm o mesmo tamanho da palavra
#Em cada acesso é lido o valor de uma célula
Endereço_em_hexadecimal= 4*4
Valor_do_conteúdo= 3*4
E= Endereço_em_hexadecimal
REM= E
M= Valor_do_conteúdo
RDM= M
print("O tamanho do REM é de",REM,"bits e o do RDM é de",RDM,"bits")


# **b) Qual deve ser a máxima quantidade de bits que podem ser implementados
# nessa memória?**

# In[17]:


#Analizando a questão temos:
#Uma MP cujo endereço em hexadecimal é 2C81
#Seu conteúdo tem um valor em hexadecimal de F5A
#Células têm o mesmo tamanho da palavra
#Em cada acesso é lido o valor de uma célula
Endereço_em_hexadecimal= 4*4
Valor_do_conteúdo= 3*4
E= Endereço_em_hexadecimal
N=2**E
M= Valor_do_conteúdo
T= N*M
print("A máxima quantidade de bits que podem ser implementados nessa memória é de",T," ou 768K bits")


# **13) Considere uma memória com capacidade de armazenamento de 64K bytes;
# cada célula pode armazenar 1 byte de informação e cada caractere é codificado
# com 8 bits. Resolveu-se armazenar na memória deste sistema um conjunto de
# caracteres do seguinte modo. A partir do endereço (hexadecimal) 27FA, foram
# escritos sucessivamente grupos de 128 caracteres iguais, iniciando pelo grupo
# de As, seguido do grupo de Bs e assim por diante, qual deverá ser o endereço
# correspondente ao local onde está armazenado o 1º J?**

# In[5]:


#Analizando a questão temos:
#Memória com capacidade de armazenamento de 64K bytes= 2^6.2^10= 2^16
#Cada célula pode armazenar 1 byte
#Cada caractere é codificado com 8 bits
#Endereço hexadecimal: 27FA
#Grupos de 128 caracteres iguais
#De A até J temos 10 letras
#27FA em decimal é 10234
N= 2**16
M= 8 
Endereço_hexadecimal= 4*4
E= Endereço_hexadecimal
Hexadecimal_em_decimal= 10234
Primeiro_A= Hexadecimal_em_decimal
A_até_I= 9*128 
Primeiro_J= Primeiro_A+A_até_I
print("O endereço que corresponde ao 1º J é",Primeiro_J,"em decimal ou 2C7A em hexadecimal")


# **14) O custo das memórias SRAM é maior que o das memórias DRAM. No
# entanto, o processo de conexão das memórias DRAM é mais complexo que o
# das SRAM e, em consequência, o preço da interface das DRAM é bem maior que
# o da SRAM. Supondo que uma interface de DRAM custe RS 5,00, uma interface
# de SRAM custe RS 1,00, o preço por bit de uma SRAM é de RS0,00002 e o de uma
# DRAM é de RS 0,00001, calcule quantos bits deve ter uma memória dinâmica
# (DRM) para que o conjunto seja mais barato.**

# In[12]:


#Analizando a questão temos:
#O custo das memórias SRAM é maior que o das memórias DRAM
#o preço da interface das DRAM é bem maior que o da SRAM
#DRAM custe R$ 5,00, uma interface de SRAM custe R$ 1,00
#O preço por bit de uma SRAM é de R$0,00002 e o de uma DRAM é de R$0,00001
DRAM= 5
SRAM= 1
Preço_por_bit_de_uma_SRAM= 2/100000
Preço_por_bit_de_uma_DRAM= 1/100000
Y= DRAM-SRAM
Z= Preço_por_bit_de_uma_SRAM-Preço_por_bit_de_uma_DRAM
X= Y/Z
print("A DRAM tem",X,"bits ou aproximadamente 400.000 bits.")


# **15) Compare uma memória principal e uma memória cache em termos de tempo
# de acesso, capacidade e temporariedade de armazenamento de dados.**
# 
# **Resposta:** Em relação ao tempo de acesso, a memória principal possui baixa velocidade e por
# isso se situa abaixo das memórias cache, já que atualmente a memória principal
# possui tempo de acesso entre 50 e 80 ns, enquanto a memória cache possui um
# tempo de acesso entre 5 e 20 ns. Na questão de capacidade, a memória principal é
# sempre bem superior à das memórias cache, e com o surgimento das arquiteturas de
# 64 bits os processadores poderão gerar endereços de 64 bits de largura, possibilitando
# assim gerar um espaço de endereçamento de memória de 16 EB (16 exabytes),
# enquanto os valores típicos de memória cache oscilam entre 32 e 256KB e ate 4MB.
# Já no requisito de temporariedade de armazenamento de dados, a transitoriedade com
# que as informações permanecem armazenadas na memória principal é, em geral,
# mais duradoura que na memória cache.

# **21) Considere um sistema constituído de um processador - memória cache -
# memória principal, no qual o tempo de acesso processador/memória cache é de
# 8 ns e o tempo de acesso memória cache/memória principal é de 70 ns.
# Observando-se um intervalo correspondente a 100 acessos consecutivos do
# processador e que a eficiência da memória cache de 96%. Calcule o tempo
# médio de acesso do sistema.**

# In[20]:


#Analizando a questão temos:
#tempo de acesso processador/memória cache é de 8 ns
#tempo de acesso memória cache/memória principal é de 70 ns
#100 acessos e eficiência de 96%
Eficiência= 96
Tempo_de_acesso_P_MC= 8
Tempo_de_acesso_MC_MP= 70
Acessos= 100
X= Eficiência*Tempo_de_acesso_P_MC
Y= Acessos-Eficiência
Z= Tempo_de_acesso_MC_MP+Tempo_de_acesso_P_MC
Tempo_total_de_acesso= X+Y*Z
Média= Tempo_total_de_acesso/Acessos
print("O tempo médio de acesso do sistema é de",Média,"ns")


# **27) Quantos bits são requeridos para se endereçar células em uma memória de
# 128G?**
# 

# In[21]:


#Analizando a questão temos:
#Memória de 128G= 2^7.2^30= 2^37
import math
N= 2**37
E= math.log2(N)
print("São requeridos",E,"bits")


# **28) E quantos bits seriam requeridos se a memória tivesse 32K?**

# In[22]:


#Analizando a questão temos:
#Memória de 32K= 2^5.2^10= 2^15
import math
N= 2**15
E= math.log2(N)
print("São requeridos",E,"bits")


# **29) Quantas posições de memória existem desde o endereço 0400(hexadecimal),
# inclusive, e o endereço 11FF (hexadecimal)**

# In[23]:


#Analizando a questão temos:
#Posições entre o endereço hexadecimal 0400 e o endereço 11FF
#O hexadecimal 0400 em decimal é 1024
#O hexadecimal 11FF em decimal é 4607
Primeiro_hexadecimal= 1024
Segundo_hexadecimal= 4607
Posições= Segundo_hexadecimal-Primeiro_hexadecimal
print("Entre os dois hexadecimais existem",Posições,"posições")


# **30) De que depende fundamentalmente a determinação da quantidade máxima de posições de memória que um processador consegue endereçar?**
# 
# **Resposta:** Depende da quantidade de bits que um processador pode endereçar.

# **31) Uma imagem pode ser representada por uma matriz de pontos armazenada
# na memória de um computador. Cada ponto possui uma indicação de cor
# associada a ela; essa cor precisa de 4 byte para ser representada. Baseado
# nessas informações, pede-se:**
# 
# **a) A quantidade de memória, em bytes, necessária para armazenar uma imagem
# de 640 X 420 pontos;**

# In[26]:


#Analizando a questão temos:
#Cada ponto possui uma indicação de cor associada a ela
#Essa cor precisa de 4 byte para ser representada
#Imagem de 640X420 pontos
Imagem= 640*420
Byte= 4
Quantidade_de_memória= Imagem*Byte
print("A quantidade de memória, em bytes, necessária é de",Quantidade_de_memória,"ou aproximadamente 1,03MB")


# **b) A quantidade de memória em megabytes. necessária para armazenar 10
# imagens semelhantes a esta;**

# In[28]:


#Analizando a questão temos:
#Cada ponto possui uma indicação de cor associada a ela
#Essa cor precisa de 4 byte para ser representada
#Imagem de 640X420 pontos
#10 imagens
#1 imagem é 1,03MB
Memória= 103/100
Imagens= 10
Quantidade_de_memória= Memória*Imagens
print("A quantidade de memória em megabytes. necessária para armazenar 10 imagens é de aproximadamente",Quantidade_de_memória,"MB")


# **c) Quantas imagens como esta poderiam ser armazenadas na memória de um
# computador com 128MB de memória RAM?**

# In[36]:


#Analizando a questão temos:
#Cada ponto possui uma indicação de cor associada a ela
#Essa cor precisa de 4 byte para ser representada
#Imagem de 640X420 pontos
#Quantas imagens podeme ser armazenadas em um computador com 128MB de memória RAM
Imagem= 103/100
Memória_RAM= 128
X=Memória_RAM/Imagem
print("A memória RAM pode armazenar",X,"bytes de imagens, então podem ser colocadas 124 imagens em 128MB de memória RAM")


# **32) Quantos bytes podem ser armazenados em uma memória ROM que possua
# 16 linhas de endereçamento e que possua 4 linhas de saída de dados?**

# In[37]:


#Analizando a questão temos:
#Memória ROM com 16 linhas de endereçamento
#4 linhas de saída de dados
E= 16 
N= 2**E
M= 4
T=N*M
Bytes=T/8
print("Podem ser armazenados",Bytes,"ou 32K bytes")


# **33) Você considera válida a afirmação "um computador com mais poder de
# processamento pode armazenar mais programas"?**
# 
# **Resposta:** Essa afirmativa não é válida pois um computador com um poder de processamento
# maior processa os dados armazenados ou inseridos, para poder armazenar mais
# programas é necessário o computador ter mais espaço no disco rígido.

# **34) Você considera válida a afirmação "vale aumentar a capacidade da memória
# principal para que o acesso aos meios magnéticos (discos rígidos e disquetes)
# seja mais rápido"?**
# 
# **Resposta** Só é válida caso os meios magnéticos possuírem uma alta taxa de transferência, pois
# assim a capacidade da memória principal faria com que mais dados dos discos fossem
# lidos em ciclo, aumentando o volume de transferências.
