# Teste Técnico – Desenvolvedor Full Stack Django

Este projeto foi desenvolvido como parte de um processo seletivo para uma vaga de estágio em desenvolvimento. O desafio é dividido em três partes principais.

- Parte 1 - Python
- Parte 2 – Exercícios Rápidos de Django
- Parte 3 – Desafio Django

## Tecnologias Utilizadas 

- Python 3
- Django
- HTML, Bootstrap e JavaScript

## Parte 1 - Python

Nesta etapa, foram resolvidos exercícios que abordam conceitos fundamentais de Python, com foco em:  

- Manipulação de listas com list comprehension;  
- Tratamento de strings e remoção de pontuação;  
- Agrupamento e contagem de dados usando dicionários;  
- Cálculo de médias;  
- Leitura e processamento de arquivos CSV.  

Os exercícios estão organizados em arquivos `.py` individuais, disponíveis na pasta `parte-1-python` do repositório. As soluções possuem comentários explicativos para facilitar o entendimento.

## Parte 2 – Exercícios Rápidos de Django

Nesta etapa, foram realizados pequenos testes em Django para reforçar conceitos básicos, incluindo criação de models, migrations, administração e templates. 

### Exercícios respondidos

8. **Relacionamentos:**

*ForeignKey*: É uma relação 1 para muitos. Por exemplo: Um produto pode ter apenas uma categoria, mas uma categoria pode ter vários produtos. E esses modelos são referenciados com uma chave estrangeira.

*ManyToManyField:* É uma relação muitos para muitos. Por exemplo: Um streaming pode ter vários filmes e um filme pode estar em vários streamings. Uma tabela intermediária é criada para relacionar registros dos dois modelos.

9. **Registro no admin**

Para registrar o model `Produto` no admin, no arquivo `admin.py` do app:

```python
from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
```

## Parte 3 – Desafio Django

Sistema básico para cadastro e gerenciamento de Clientes, Produtos e Pedidos, com funcionalidades práticas e interface responsiva.

### Funcionalidades principais

- CRUD completo para clientes, produtos e pedidos.  
- Seleção múltipla de produtos ao criar pedidos via checkboxes.  
- Cálculo automático do valor total do pedido no frontend com JavaScript.  
- Filtro de pedidos por cliente.  
- Layout simples com Bootstrap.

## Instalação e execução para as partes 2 e 3

1. Clone o repositório:

```bash
git clone https://github.com/NicolasCasser/Teste-Tecnico-Desenvolvedor-FullStackDjango
```

2. Crie e ative ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale o Django
```bash
pip install Django
```

4. Aplique as migrations:
```bash
python manage.py migrate
```

5. Execute o servidor:
```bash
python manage.py runserver
```

6. Acesse a aplicação no navegador:
```bash
http://127.0.0.1:8000/
```
