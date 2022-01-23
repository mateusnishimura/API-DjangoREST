# API-DjangoREST

Para clonar o repositório localmente:
`git clone git@github.com:mateusnishimura/API-DjangoREST.git`

Para ativar o ambiente virtual:
`source venv/bin/activate`

Para analisar se foram feitas mudanças nos modelos e, em caso positivo, criar novas migrações:
`python manage.py makemigrations`

Para criar as migrations:
`python manage.py migrate`

Para criar um superusuário:
`python manage.py createsuperuser`

Para executar o servidor:
`python manage.py runserver`


| Rotas | URL |
| ------ | ------ |
| Frutas: POST, GET| [http://localhost:8000/fruit/] |
| Frutas: UPDATE, DELETE| [http://localhost:8000/fruit/:id_fruta] |
| Regiões: POST, GET | [http://localhost:8000/region/] |
| Regiões: UPDATE, DELETE| [http://localhost:8000/region/:id_regiao] |
| Painel admin | [http://localhost:8000/admin] |
