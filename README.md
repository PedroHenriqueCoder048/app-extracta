<table>
 <tr>
   <td>
     <h1>
      EXTRACTAR
     </h1>
   </td>
  <td>
   <img
    src="https://img.icons8.com/?size=100&id=47052&format=png&color=000000"
    />
   <img
    src="https://img.icons8.com/?size=100&id=43147&format=png&color=000000"
    />
  </td>
 </tr>
 </table>

<p>Essa aplicação foi feita utilizando as tecnologias DJANGO,OCR, OLLAMA,PYTESSERACT e DOCKER.Essa aplicação foi feita para estudar e treinar de como usar uma IA de escalo local em algum projeto, foi bastante desafiador e sproveitei os conhecimentos que obtuve nos ultimos meses de DJANGO para criar aplicações simples mas úteis.</p>

<p>Essa aplicação o usuário insere um pdf no qual ultilizando IA e OCR extrai os dados e converte de acordo com a necessidade do usuário</p>

<h2>Requisitos para rodar na máquina local</h2>

<h3>Ollama</h3>

<p>Ollma com o IA de escala local deepseek com 7 bilhões de parâmetros.</p>

<p>OBS: por se tratar de uma IA local , é necessário ter uma maquina com uma GPU.</p>

<p>Mais informações podem ser encontradas na </p>[Documetação](https://docs.ollama.com/)

<p>Rodar Ollama depois de instalado</p>

`ollama run deepseek-r1`

<p>No caso da versão já configurada no container</p>

`ollama run deepseek-r1:7b`

Caso queira usar um modelo com mais ou menos parâmetros, acesse pdf/views.py e ajuste o bloco da função home para ajusar os parâmetros do modelo desejado

`llm = OllamaLLM(
     #Aqui ajustamos o modelo do Ollama#
     model='deepseek-r1:7b',
     temperature=0,
     base_url="http://host.docker.internal:11434",)`

<h3>Docker</h3>

Para instalar o Docker para poder rodar o container

<p>Para a instalação você pode ir direto na [Documetação](https://docs.docker.com/?_gl=1*1v27m4w*_gcl_au*MTk1OTAyODQwNC4xNzYzNjY1NDU2*_ga*NTI3NDg3MTI5LjE3NjM2NjU0NTc.*_ga_XJWPQMJYHQ*czE3NjM2NjU0NTYkbzEkZzEkdDE3NjM2NjU0NTgkajU4JGwwJGgw)</p>

<p>OBS: Caso o seu SO seja windows não esqueça de instalar o wsl</p>

<p>Após o download e instalação, você vai na raiz de onde esta todos os arquivos do projeto e vai criar a build para rodar o container</p>

`docker build -t app-extracta`

<p>Agora vamos rodar o container</p>

`docker run -p 8000:8000 aoo-extracta`


