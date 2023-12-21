# Formação Django

- Base da Programação Web
	## Arquitetura Cliente-Servidor
		Estrutura de computação distribuida que distribui tarefas e cargas de trabalho entre fornecedores de serviço e requerentes dos serviços.
		
		- servidor: fornecedor;	
		- cliente: requerente ex.: navegador;
		- internet: meio;
		
	## Protocolo HTTP e seus verbos
		Protocolo de Transferência de Hipertexto
		- se comunicam nas portas 80 para HTTP;
		- portas 443 para HTTPS (criptografada);
		
		** HTTP RFC 7540 (documentação)
		
		- Verbos/Métodos
			Get: busca recursos ou cache;
			Post: cria novo recurso;
			Put/Patch: atualiza um recurso;
			Delete: remove um recurso;
			
	## Progamação Estátia x Dinâmica
		- Estática: linguagens de programação que não são processados no servidor;
		- Dinâmica: que são processados no servidor;

- Django Framework Básico
	## Inicialização de Projeto e Ambiente Virtual
		Boa prática: para cada projeto, é recomendado utilizar um novo ambiente virtual (de preferêncai de mesmo nome do projeto);
		
		- Comandos:
			python -m venv NomeDoProjeto (cria o ambiente virtual)
			.\CaminhoDoAmbienteVirtual\Scripts\Activate.ps1 (ativa o ambiente virtual)
			python.exe -m pip install --upgrade pip
			pip install Django (instala o Django no ambiente virtual)
			pip freeze > requirements.txt (usa pip (gerenciador de Pacotes) para indicar bibliotecas necessárias no projeto)
			
			- Criação de Projeto Django
			django-admin startproject nomeDoProjeto . (comando para criação de projeto Django ('.' diz para que não seja diretório raiz, apenas arquivos do projeto)
			
			- Criação de Aplicação Django
			django-admin startapp nomeAplicacao
			
			## Execução
			- comandos de gerenciamento dos projetos Django devem ser executados no mesmo diretório do arquivo 'manage.py';
			- python manage.py runserver (comando para execuação do projeto)
			- python manage.py migrate (comando sugerido após o run para corrigir os erros de migrations)
			
	## Projetos x Aplicações Django
		- o que torna um projeto django?
		- pra que serve as aplicações Django?
		
		O django possui projetos que englobam todo o escopo e dentro desse projeto cria-se aplicações plugáveis (onde cada aplicação terá sua função especifica, trabalham entre si e podem ser usadas em outros projetos);
			
	## Configurações - SETTINGS.py
		** Quando criada nova aplicação em um projeto Django, é necessário referênciar essa aplicação no arquivos 'settings.py' no campo 'INSTALLED_APPS' para que o projeto tenha conhecimento dessa aplicação;
			
		** Em 'settings.py' no campo 'TEMPLATES', em 'DIRS' é necessário inserir 'templates' dentre os couchetes [], diz que o diretório de templates se chamará templates;
			
	## Migrations: forma profissional de se manter um histórico de banco de dados;
		python manage.py makemigrations (cria migrations para todos os modelos do projeto)
		python manage.py migrate (aplica as migrations)
	
	## MTV do Django
		Models:
			- modelos de dados;
			
		Views:
			- atual como o Controller na arquitetura MVC;
			- views são criadas nas aplicações e são funções python que recebem uma variável chamada request e retorna a renderização desse request passando um template;
			
		Templates:
			- atual como as views na MVC (paginas HTML por exemplo);
			
		Rotas / URLS.py:
			- de forma profissional, não é recomendado adicionar todas as rotas no arquivo de urls do projeto, o recomendado é adicionar um include no urls.py e especificar uma a uma as rotas para direcionar ao arquivo de rotas das aplicações;
			- importa das views as funções ex.: from core.views import index, contato;
			- em seguida cria-se os caminhos ex.: path('contato', contato);
