# Guiões das Sessões Laboratoriais
---
## Guião 9

### Finalização do protocolo StS usando certificados

No guião desta semana vamos concluir a implementação do protocolo _Station_to_Station_ fazendo uso de certificados X509. Para tal vamos incorporar a funcionalidade explorada no último guião (validação dos certificados), por forma a assegurar a cada um dos intervenientes que fazem uso da chave pública correcta na verificação da assinatura.

Concretamente, o protocolo a implementar irá ser então:  
1. Alice → Bob : g<sup>x</sup>  
2. Bob → Alice : g<sup>y</sup>, Sig<sub>B</sub>(g<sup>x</sup>, g<sup>y</sup>), Cert<sub>B</sub>  
3. Alice → Bob :  Sig<sub>A</sub>(g<sup>x</sup>, g<sup>y</sup>), Cert<sub>A</sub>  
4. Alice, Bob : K = g<sup>(x*y)</sup>

Note que os pares de chave a utilizar neste guião são os fornecidas nas _keystores_ PKCS12 fornecidos no guião 8.

Alguns apontadores:
 * Biblioteca [PyOpenSSL](https://www.pyopenssl.org/en/stable/), em particular os métodos:
    * [load_certificate](https://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.load_certificate) e [dump_certificate](https://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.dump_certificate)
    * [load_pkcs12](https://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.load_pkcs12) e os vários métodos da classe [PKCS12](https://www.pyopenssl.org/en/stable/api/crypto.html#pkcs12-objects)
    * os vários métodos da classe [X509Store](https://www.pyopenssl.org/en/stable/api/crypto.html#x509store-objects) (em particular, o [verify_certificate](https://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.X509StoreContext.verify_certificate]))
    
---
## Guião 8

### Manipulação de Certificados X509

O objectivo nesta semana é o de se investigar formas de validar _cadeias de certificados_ em _Python_. A ideia é que, mais tarde, esses certificados serão incorporados na aplicação clente-servidor que temos vindo a implementar - mas neste guião o objectivo é forcar no aspecto da _validação_ desses certificados.

Como ponto de partida, disponibiliza-se:

 1. Uma _keystore_ PKCS12 contendo o Certificado (e respectiva chave privada) para o rervidor: [Servidor.p12](Servidor.p12)
 1. Uma _keystore_ PKCS12 contendo o Certificado (e respectiva chave privada) para o cliente: [Cliente.p12](Cliente.p12) 
 1. O Certificado (em formato DER) da CA utilizada: [CA.cer](CA.cer)

Para aceder ao conteúdo das `Keystores` devem utilizar a password "1234", quer para carregar a `keystore`, quer para aceder à entrada respectiva (o `alias` é `Cliente1` e `Servidor` para as keystores `Cliente.p12` e `Servidor.p12` respectivamente).

Numa primeira fase, utilizaremos ferramentas de domínio público directamente na linha-de-comando. Concretamente, utilizaremos o [openSSL](https://www.openssl.org), e em particular os sub-comandos (ver respectiva documentação):
 - [`x509`](https://www.openssl.org/docs/manmaster/man1/openssl-x509.html);
 - [`pkcs12`](https://www.openssl.org/docs/manmaster/man1/openssl-pkcs12.html);
 - [`verify`](https://www.openssl.org/docs/manmaster/man1/verify.html).

Uma vez ultrapassado esse passo, vamos considerar como transpor esse método de validação para o _Python_, por forma a ser usável na aplicação cliente-servidor. A dificuldade é que as bibliotecas que temos vindo a utilizar não dispõe dessa funcionalidade, pelo que se sugere a instalação/utilização da biblioteca [PyOpenSSL](https://pyopenssl.org/en/stable/index.html).

Referências adicionais:
 - http://www.yothenberg.com/validate-x509-certificate-in-python/
 - http://aviadas.com/blog/2015/06/18/verifying-x509-certificate-chain-of-trust-in-python/
 - https://stackoverflow.com/questions/6345786/python-reading-a-pkcs12-certificate-with-pyopenssl-crypto


---
## Guião 7

### Protocolo *Station-to-Station* simplificado

Pretende-se complementar o programa com o acordo de chaves *Diffie-Hellman* para incluir a funcionalidade
análoga à do protocolo *Station-to-Station*. Recorde que nesse protocolo é adicionado uma troca de assinaturas:

1. Alice → Bob : g<sup>x</sup>
1. Bob → Alice : g<sup>y</sup>, Sig<sub>B</sub>(g<sup>x</sup>, g<sup>y</sup>)
1. Alice → Bob :  Sig<sub>A</sub>(g<sup>x</sup>, g<sup>y</sup>)
1. Alice, Bob : K = g<sup>(x*y)</sup>

De notar que um requisito adicional neste protocolo é a manipulação de pares de chaves assimétricas para realizar as assinaturas digitais (e.g. RSA). Para tal deve produzir um pequeno programa que gere os pares de chaves para cada um dos intervenientes e os guarde em ficheiros que serão lidos pela aplicação Cliente/Servidor.

Sugestão: comece por isolar as "novidades" requeridas pelo guião, nomeadamente:  

  1. criação do par de chaves para a assinatura e utilização dos métodos para ''assinar'' e ''verificar'' 

  1. gravar as chaves públicas/privadas em ficheiro
  
  1. integrar as assinaturas no protocolo _Diffie-Hellman_

---
## Guião 6

### Protocolo *Diffie-Hellman*

Relembre o protocolo de acordo de chaves _Diffie\_Hellman_:

 1. Alice → Bob : g<sup>x</sup>
 1. Bob → Alice : g<sup>y</sup>
 1. Alice, Bob : K = g<sup>(x*y)</sup>

Onde `g` é um gerador de um grupo cíclico de ordem prima `p`, `x` e `y` são elementos aleatórios do grupo, e `K` é o segredo estabelecido pelo protocolo. Todas as operaçes são realizadas módulo `p`.

Pretende-se implementar o protocolo de acordo de chaves *Diffie-Hellman* fazendo uso da funcionalidade oferecida pela biblioteca `cryptography`. Em concreto, utilizando a classe [`dh`](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/).

Algumas observações:  
 * Se pretender, pode fixar os parâmetros do grupo utilizando por exemplo:
 ```
P = 99494096650139337106186933977618513974146274831566768179581759037259788798151499814653951492724365471316253651463342255785311748602922458795201382445323499931625451272600173180136123245441204133515800495917242011863558721723303661523372572477211620144038809673692512025566673746993593384600667047373692203583
```
````S 
G = 44157404837960328768872680677686802650999163226766694797650810379076416463147265401084491113667624054557335394761604876882446924929840681990106974314935015501571333024773172440352475358750668213444607353872754650805031912866692119819377041901642732455911509867728218394542745330014071040326856846990119719675
```

 * A documentação da biblioteca não é muito clara na forma como se pode comunicar as chaves públicas DH, tal como requerido pelo protocolo. Na prática, existem duas alternativas:  
     - Aceder ao valor (inteiro) da chave pública através da classe `DHPublicNumbers`
     - Utilizar as facilidades de serialização da chave pública oferecidas pela biblioteca (acessível a partir do método `public_bytes` da classe `DHPublicKey`).

---
## Guião 5


### Comunicação entre cliente-servidor

As scripts [Client.py](scripts/Client.py) e
[Server.py](scripts/Server.py) constituem uma implementação muito
básica de uma aplicação que permite a um número arbitrário de
clientes comunicar com um servidor que escuta num dado port
(e.g. 8888). O servidor atribui um número de ordem a cada cliente, e
simplesmente faz o _dump_ do texto enviado por eese cliente
(prefixando cada linha com o respectivo número de ordem). Quando um
cliente fecha a ligação, o servidor assinala o facto (e.g. imprimindo
[n], onde _n_ é o número do cliente).

Exemplo da execução do servidor (que comunica com 3 clientes):


```bash
$ python3 Servidor.py
1 : daskj djdhs slfghfjs askj
1 : asdkdh fdhss
1 : sjd
2 : iidhs
2 : asdjhf sdga
2 : sadjjd d dhhsj
3 : djsh
1 : sh dh d   d
3 : jdhd kasjdh as
2 : dsaj dasjh
3 : asdj dhdhsjsh
[3]
2 : sjdh
1 : dhgd ss
[1]
2 : djdj
[2]
```

Pretende-se:

 * Modificar as respectivas classes por forma a garantir a
   _confidencialidade_ e _integridade_ nas comunicações
   estabelecidas.
 * Para garantir a confidencialidade, deverá considerar uma cifra por
   blocos no modo que considerar mais apropriado.
 * obs: nas implementações fornecidas das classes `Client` e
   `ServerWorker`, não deverá ser necessário "mexer" muito para além
   do método `process`.

---
## Guião 4

### Animação de modelos de segurança

Pretende-se animar em _Python_ os "jogos" que servem de base aos modelos de segurança
adoptados na formalização das provas de segurança. Especificamente,
sugere-se ilustrar ataque(s) à confidencialidade das cifras, recorrende à definição de
**IND-CPA** (_indistinguibilidade na presença
de ataques de texto-limpo escolhido_). Recorda-se que o jogo `IND-CPA` é definido
como (apresentado numa sintaxe que pretende facilitar a transposição para a respectiva
codificação em _Python_).

```
IND_CPA(C,A) =
  k = C.keygen()
  enc_oracle = lambda ptxt: C.enc(k,ptxt)
  m[0], m[1] = A.choose(enc_oracle)
  b = random_bit()
  c = C.enc(k,m[b])
  b' = A.guess(enc_oracle, c)
  return b==b'
```

Obs: `m[0]` e `m[1]` devem ser mensagens com um tamanho fixo pré-determinado; assume-se
ainda que o adversário `A` dispõe de "variáveis de instância" que armazena o estado
a preservar entre as duas chamadas.

A segurança é estabelecida quando, para qualquer adversário, a sua **vantagem** definida
como `2 * | Pr[IND_CPA(C,A)=1] - 1/2 |` é negligênciável. Naturalmente que verificar a
segurança de uma cifra concreta `C` estará fora do alcance de uma "animação" do jogo
`IND-CPA`, mas pode servir para ilustrar **ataques** instanciando um adversário que
permita um desvio significativo na probabilidade de sucesso do jogo.

Sugestões:
 * O mecanismo de classes do _Python_ é particularmente útil na parametrização dos jogos;
 * Uma cifra claramente insegura, como a cifra `Identidade` (onde as operações de cifrar
 e decifrar são a função identidade) pode ser útil para ilustrar os conceitos.
 * Alguns exemplos de ataques mencionados nas aulas que podem ser ilustrados: insegurança
 das cifras determinísticas; do mecanismo _encrypt\_and\_mac_; modo ECB numa cifra por
 blocos; etc.
 
 Valorização:
  * Considere jogos para outros modelos mencionados na aula (e.g. IND-CCA, INT-PTXT, INT-CTXT)

---
## Guião 3
### Implementação de Cifra Autenticada

Tem-se vindo a fazer uso da cifra autenticada `Fernet` que
garante simultaneamente ('i') a confidencialidade dos dados e ('ii') a
integridade da informação. Neste curso interessa-nos perceber como é que
essas propriedades podem ser estabelecidas a partir das várias técnicas
criptográficas disponíveis, pelo que nesta semana iremos realizar a mesma
funcionalidade recorrendo directamente de uma _cifra simétrica_ e de um
_MAC_. A questão que surge é como combinar essas primitivas, sendo que é concebível considerar as seguintes soluções:

 * **encrypt and MAC**: onde tanto cifra como o MAC são aplicados sobre o texto limpo;
 * **encrypt then MAC**: onde o texto limpo passa originalmente pela cifra, e o MAC é calculado já sobre o criptograma;
 * **MAC then encrypt**: onde é primeiro calculado o MAC sobre o texto limpo, e só depois é cifrado (texto limpo e _tag_ de autenticação).

Pretende-se então substituir a cirfra `Fernet` do programa de cifra por cada uma das três versões referidas. Sugere-se a utilização de `ChaCha20` como cifra, e de `HMAC-Sha256` como MAC.

---
## Guião 2
### Protecção de Segredos Criptográficos

No guião da semana passada fez-se uso da cifra autenticada `Fernet`
que garante simultaneamente ('i') a confidencialidade dos dados e
('ii') a integridade da informação. No entanto, e do ponto de vista de
segurança, o aspecto mais crítico na resolução do guião é o tratamento
dado aos segredos criptográficos utilizados. De facto, e para além de
se certificar que se recorre sempre a um **gerador de números
aletórios seguro**, é em geral desaconselhado armazenar segredos
criptográficos em ficheiros sem qualquer protecção.

Existem duas estratégias para evitar a utilização desses ficheiros
desprotegidos:

 1. *Evitar a necessidade de se armazenar a chave*. Para isso, considera-se
 um mecanismo seguro que permita gerar um segredo criptográfico a partir
 de uma _password_ ou _passphrase_ (que naturalmente não podem ser utilizadas
 directamente como chaves criptográficas). Para o efeito faz-se uso das
 designadas _Password Based Key Derivation Functions (PBKDF)_.
 1. Armazenar o ficheiro de forma protegida, no que se designa
 habitualmente por *KeyStore*. Na realidade, esta estratégia acaba por
 partilhar muitos dos requisitos da apresentada antes, porque para
 protegermos a 'KeyStore' irá ter de (internamente) usar uma cifra
 autenticada, e para isso de um novo segredo. Mas, tal como no ponto
 anterior, esse segredo é geralmente gerado a partir de uma
 _password_. [**OBS:** na verdade, é muito raro utilizar-se
 _KeyStores_ para armazenar chaves simétricas -- as _KeyStores_ são
 normalmente utilizadas para armazenar secregdos de "longo-prazo", que
 não é o caso de chaves simétricas que se recomenda que sejam
 utilizadas uma única vez (chaves de sessão)].
 
Pretende-se assim adicionar à funcionalidade pedida no guião anterior
a protecção dos segredos de acordo com ambas as estratégias
apresentadas. 

Sugestões:

 * Como mecanismo de PBKDF na primeiro abordagem, sugere-se a itilização da primitiva [`PBKDF2`](https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC);
 * Na inicialização do mecanismo PBKDF, irá recorrer a um _salt_ aleatório. Esse valor deve ser armazenado juntamente com o criptograma;
 * Para a leitura da _passphrase_, sugere-se a utilização do módulo [`getpass`](https://docs.python.org/3.7/library/getpass.html), da biblioteca standard Python;
  * A cifra [`Fernet`](https://cryptography.io/en/stable/fernet/) adopta um formato para a chave com a codificação `base64`. Para converter a _byte_string_ derivada pela KDF numa chave nesse formato, pode recorrer ao módulo da biblioteca `base64` do `Python`, especificamente o método [base64.urlsafe_b64encode](https://docs.python.org/2/library/base64.html#base64.urlsafe_b64encode);
 * Na segunda abordagem, recomenda-se o uso da PBKDF [`Scrypt`](https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#cryptography.hazmat.primitives.kdf.scrypt.Scrypt), já que adiciona protecção adicional a ataques de dicionário.


---

## Guião 1
### O Ambiente de Desenvolvimento

Esta primeira aula pretende essencialmente garantir uma utilização fluida do ambiente de trabalho adoptado
na UC. Isso pressupõe a utilização do `github` (em particular, do repositório atribuído ao grupo de trabalho), e
do ambiente `Python` (versão 3). 

#### Instalação de bibliotecas de suporte

##### Cryptography - https://cryptography.io/en/latest/

A biblioteca criptográfica que iremos usar maioritariamente no curso é `cryptography`. Trata-se de uma biblioteca
para a linguagem Python bem desenhada e bem documentada que oferece uma API de alto nível a diferentes
“Serviços Criptográficos” (_recipes_). No entanto, e no âmbito concreto deste curso, iremos fazer um uso
"menos standard" dessa biblioteca, na medida em que iremos recorrer directamente à funcionalidade de baixo nível.

Instalação:

Sugere-se o método de instalação baseado no `pip` (ver https://cryptography.io/en/latest/installation/).

```
pip3 install --upgrade pip
pip3 install cryptography
```

##### [opcional] Jupiter - https://jupyter.readthedocs.io/

`Jupyter` é um sistema de 'notebooks' para o Python que possibilita a
interação com a linguagem por intermédio de um simples
'browser'. Esses ´notebooks´ permitem que, para além células contendo
código Python e as respectivas respostas, existam elementos contendo
texto formatado, figuras, fórmulas matemáticas (escritas em LaTeX),
etc.  A ideia da utilização desses ´notebooks´ então a de permitir a
produção de documentos informativos contendo, para além do código
Python, todos os aspectos considerados relevantes (assumpções, opções
de desenho, limitações assumidas, etc.).

Instalação:

Sugere-se o método de instalação baseado no `pip` (ver https://jupyter.readthedocs.io/en/latest/install.html)

```
pip3 install jupyter
```


### Aplicação de exemplo: Cifra autenticada de Ficheiro

Pretende-se cifrar o conteúdo de um ficheiro, assegurando a
*confidencialidade* e *integridade* dos dados lá armazenados.

 * Para o efeito deve o mecanismo de cifra autenticada _Fernet_,
disponibilizada pela biblioteca _cryptography_.
 * Emule o efeito de um 'ataque' à integridade do criptograma. Verifique
o impacto na utilização do seu programa.

---

## ORGANIZAÇÃO DO REPOSITÓRIO

### Arrumação do repositório

Por forma a permitir um acesso ao repositório mais efectivo, devem proceder à seguinte organização de directorias:

```
+-- Readme.md: ficheiro contendo: (i) composição do grupo (número, nome e login github de cada
|              membro); (ii) aspectos que entenderem relevante salientar (e.g. dar nota de
|              algum guião que tenha ficado por realizar ou incompleto; um ou outro guião
|              que tenha sido realizado apenas por um dos membros do grupo; etc.)
+-- Guioes
|        |
|        +-- G1
|        |    +-- Readme.md: notas sobre a realização do guião 1 (justificação das opções
|        |    |              tomadas; instruções de uso; dificuldades encontradas; etc.)
|        |    +-- ...
|        |
|        +-- G2
|        |   ...
...      ...
|
+-- Projs
|       |
|       +-- A88888: projeecto individual do aluno ...
|       ...
|
...
```


---