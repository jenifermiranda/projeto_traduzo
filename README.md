<h1 align='center'><b>Projeto Traduzo</b></b></h1>

![Tela](src/views/static/images/traduzo.png)

Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side.

<br><br>
<strong>Preparando o Ambiente</strong>
  <br />

Para executar o app e ver ele funcionando você precisa seguir os passos abaixo:

**[1]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[2]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**[3]** Banco e Flask pelo Docker

```bash
docker compose up translate
```

**[4]** Popular o banco

```bash
docker compose exec -it translate python3 src/run_seeds.py
```

<br><br>
<strong>Habilidades</strong>
  <br />
  
A partir desse projeto eu desenvolvi as seguintes habilidades:

- Implementar uma API utilizando arquitetura em camadas MVC;

- Utilizar o Docker para projetos Python;

- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB;

- Escrever testes para APIs para garantir a implementação dos endpoints;

- Interagir com um banco de dados não relacional MongoDB;

- Desenvolver páginas web Server Side.
  
<br><br>
*Esse app faz parte dos projetos avaliadores da Trybe e alguns arquivos foram fornecidos para que fosse possível a avaliação do meu código.
