# Temas de Projectos Individuais

São apresentados diferentes tipos de pequenos projectos individuais. Note que o principal objectivo desta selecção é o de servir de referencial para o tipo de trabalho pretendido, sendo que podem ser propostos projectos similiares e/ou variantes dos apresentados.  
Os trabalhos devem ser realizados individualmente e colocados no repositório do grupo até ao final do dia do 2º teste da disciplina, numa directoria de topo como o nome **Proj-\<NUM-ALUNO\>** (e.g. `Proj-a99999`). A escolha do projecto deve ser comunicada ao docente durante a aula ou por email.

---
## Prototipagem de Técnicas Criptográficas em _Sage_

O [SageMath](http://www.sagemath.org) é um sistema _open source_ para matemática que agrega um vasto conjunto de recursos para computação científica. Torna-se assim de uma ferramente priveligiada para a prototipagem de técnicas criptográficas avançadas.
O modo de interacção típica como o _Sage_ é por intermédio de _notebook_s (similares aos _notebook_s do _Jupyter_), e em que a linguagem de programação que adoptada continua a ser o _Python_.

Nestes projecto, o objectivo é construir um _notebook_ do _Sage_ que implemente (e documente) uma técnica criptográfica avançada. Como exemplos de técnicas que poderão ser adoptadas, sugere-se:
 * Criptografia baseada em curvas elípticas (ver https://en.wikipedia.org/wiki/Elliptic-curve_cryptography#Cryptographic_schemes para alguns exemplos)
 * _Identity-based Encryption_ (baseado em http://home.deib.polimi.it/gmauri/critto/ibe_sage.pdf)
 * _Paillier cryptosystem_ (ver https://en.wikipedia.org/wiki/Paillier_cryptosystem)
 * um esquema baseado no _El Gamal_ para _Threshold Encryption_ (descrito em http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=C381EE37B66843AC5EF6C91CDCDD05F3?doi=10.1.1.50.1412&rep=rep1&type=pdf)

Algumas referências Web:
 * http://www.math2803.gatech.edu/lessons/lesson-7/sage/
 * https://www.maths.ox.ac.uk/system/files/attachments/sage-introduction.pdf
 * https://www.johannes-bauer.com/compsci/ecc/#anchor37

---
## Implementação de Tecnicas Criptográficas em _Python_

O objectivo destes projectos é implementar (ou adaptar uma implementação) para uma nova técnica criptográfica, por forma a exibir uma API de utilização semelhante à oferecida pelas bibliotecas que temos vindo a utilizar (`cryptography` ou `pycrypto`). O resultado final deverá ser então o(s) ficheiro(s) _Python_ correspondentes (devidamente comentados) e um `Readme.md` que cumpra as funções de um "mini-relatório".

 * um esquema baseado no _El Gamal_ para _Threshold Encryption_ (descrito em http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=C381EE37B66843AC5EF6C91CDCDD05F3?doi=10.1.1.50.1412&rep=rep1&type=pdf)
 * _Crammer-Shoup_ (ver https://en.wikipedia.org/wiki/Cramer–Shoup_cryptosystem) -- perceber/adaptar/documentar implementação disponibilizada em https://github.com/benkreuter/cca2python
 * _Scnorr NIZK Proof_ (c.f https://datatracker.ietf.org/doc/draft-hao-schnorr/02/?include_text=1) -- ver também https://en.wikipedia.org/wiki/Schnorr_signature

---
## Explorar novas Bibliotecas ou Ferramentas

Nestes projectos pretende-se tomar contacto com ferramentas e/ou bibliotecas relacionadas com os assuntos abordados na UC. 
 * Utilizar a biblioteca `ssl` (standard do _Python_) para estabelecer um canal seguro entre duas entidades (e.g. na aplicação Cliente/Servidor que vem sendo utilizada nas aulas).
 * Fazer o _deploy_ da Certificate Authority _open-source_ **EJBCA** (http://ejbca.org) para produzir certificados para diferentes fins (correio electrónico; tls; etc.)
 * _Proof-assistant_ para provas criptográficas - o sistema **EasyCrypt**. (ver https://www.easycrypt.info/) e https://github.com/EasyCrypt/easycrypt).

---
## Estudo de Artigos Científicos

Nestes projectos pretende-se aprofundar um assunto apresentado num artigo científico sobre uma área da cryptografia. Como resultado pretende-se um pequeno relatório (que pode ser materializado num ficheiro `Readme.md`) e que contenha uma resenha crítica do artigo. Pode, se entender, fazer acompanhar o relatório com código _Python_ que ilustre algum dos aspectos apresentado.

 * "Sequences of Games: A Tool for Taming Complexity in Security Proofs", Victor Shoup.  http://shoup.net/papers/games.pdf
 * "Authenticated Encryption: Relations among notionsand analysis of the generic composition paradigm", Mihir Bellare and Chanathip Namprempre. http://cseweb.ucsd.edu/~mihir/papers/oem.pdf
 * Sobre o desenho, implementação e uso da bliblioteca _NaCl_ (ver http://nacl.cr.yp.to/index.html). _Bindings_ para _Python_: https://github.com/pyca/pynacl/
 * "Computer-Aided Security Proofs for the Working Cryptographer". G. Barthe et al. http://software.imdea.org/~szanella/Zanella.2011.CRYPTO.pdf ([slides](https://www.iacr.org/conferences/crypto2011/slides/02-1-Barthe.pdf) da apresentação)
