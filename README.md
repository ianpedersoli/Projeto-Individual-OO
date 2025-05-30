## Sistema de Controle de Estudantes

📄 Definição do Problema

O cenário educacional moderno exige uma gestão eficiente e organizada das informações dos alunos. Manter registros precisos de estudantes, suas matrículas e desempenho acadêmico, como notas e médias, é crucial para instituições de ensino e educadores.
O problema que este projeto busca resolver é a necessidade de um sistema robusto e fácil de usar para gerenciar o cadastro e o desempenho acadêmico de estudantes. Ele visa centralizar as operações de registro, permitindo que professores e administradores possam adicionar, remover, listar e atualizar informações de alunos, além de gerenciar suas notas de forma eficiente e confiável.

🚀 Funcionalidades (Casos de Uso)
Este sistema oferece as seguintes funcionalidades principais para o gerenciamento de estudantes:

UC001: Adicionar Novo Estudante
Descrição: Permite cadastrar um novo estudante no sistema, fornecendo seu nome, idade e matrícula.
Validações: Garante que a matrícula seja única (9 dígitos numéricos) e o nome também seja único (ignorando maiúsculas/minúsculas).

UC002: Remover Estudante
Descrição: Permite excluir um estudante existente do sistema com base em sua matrícula.

UC003: Listar Estudantes
Descrição: Exibe uma lista completa de todos os estudantes cadastrados, incluindo seus dados pessoais e desempenho acadêmico (média).

UC004: Adicionar Nota ao Estudante
Descrição: Permite registrar uma nova nota para um estudante específico, utilizando sua matrícula como identificador.

UC005: Calcular Média de Notas do Estudante
Descrição: Calcula e exibe a média das notas de um estudante individualmente.

UC006: Limpar Banco de Dados
Descrição: Oferece uma opção para apagar todos os dados de estudantes do sistema, incluindo o arquivo de persistência (.db).

🏗️ Estrutura do Projeto

O projeto segue uma estrutura modular para organização e clareza do código:

````
├── main.py

└── package/

    ├── controllers/
    
    │   └── sistema_controller.py
    
    └── models/
    
        ├── estudante.py
        
        └── pessoa.py
````
        
main.py: Ponto de entrada da aplicação, responsável por inicializar a interface gráfica.

package/models/: Contém as classes que representam os dados do sistema.

pessoa.py: Define a classe base Pessoa.

estudante.py: Define a classe Estudante, que herda de Pessoa.

package/controllers/: Contém as classes de controle da lógica de negócio e persistência.

sistema_controller.py: Gerencia as operações de CRUD (Criar, Ler, Atualizar, Deletar) dos estudantes e a persistência de dados.


UML: Diagrama de Classes
A arquitetura do sistema pode ser visualizada no diagrama de classes abaixo:

Fragmento do código
````
classDiagram
    class Pessoa {
        - _nome: str
        - _idade: int
        + __init__(nome: str, idade: int)
        + nome: str (property)
        + idade: int (property)
        + exibir_dados(): str
    }

    class Estudante {
        - _matricula: str
        - _notas: list
        + __init__(nome: str, idade: int, matricula: str)
        + adicionar_nota(nota: float)
        + media_notas(): float
        + matricula: str (property)
        + notas: list (property)
        + exibir_dados(): str
    }

    class SistemaController {
        - caminho_banco: str
        - estudantes: list<Estudante>
        + __init__()
        - _salvar_dados()
        - _carregar_dados(): list<Estudante>
        + adicionar_estudante(nome: str, idade: int, matricula: str)
        + remover_estudante(matricula: str)
        + listar_estudantes(): list<str>
        + adicionar_nota_estudante(matricula: str, nota: float)
        + calcular_media_estudante(matricula: str): float
        + limpar_dados()
        - _buscar_estudante_por_matricula(matricula: str): Estudante
    }

    class Interface {
        - master: tk.Tk
        - controller: SistemaController
        - nome_entry: tk.Entry
        - idade_entry: tk.Entry
        - matricula_entry: tk.Entry
        - nota_entry: tk.Entry
        - resultado: tk.Text
        + __init__(master: tk.Tk)
        + limpar_campos()
        + adicionar_estudante()
        + remover_estudante()
        + listar_estudantes()
        + adicionar_nota()
        + media_estudante()
        + limpar_dados()
    }

    Pessoa <|-- Estudante : Herança
    SistemaController "1" *-- "0..*" Estudante : Composição (Gerencia)
    Interface "1" -- "1" SistemaController : Associação (Usa)
````
    
⚙️ Como Rodar o Projeto
Siga os passos abaixo para configurar e executar o Sistema de Controle de Estudantes em sua máquina.

Pré-requisitos
Python 3.x (versões mais recentes são recomendadas)
1. Clonar o Repositório
```
git clone <URL_DO_SEU_REPOSITORIO>
cd sistema-controle-estudantes # Ou o nome da sua pasta
```

3. Executar a Aplicação
A interface gráfica do sistema será iniciada.

```
python main.py
```
3. Utilizando a Interface
   
Adicionar Estudante: Preencha os campos "Nome", "Idade" e "Matrícula" e clique em "Adicionar Estudante".

Remover Estudante: Insira a matrícula do estudante no campo "Matrícula" e clique em "Remover Estudante".

Listar Estudantes: Clique em "Listar Estudantes" para ver todos os alunos cadastrados na área de texto.

Adicionar Nota: Insira a matrícula e a nota nos campos correspondentes e clique em "Adicionar Nota".

Média de Notas: Insira a matrícula e clique em "Média de Notas" para ver a média de um estudante.

Limpar Banco de Dados: Clique em "Limpar Banco de Dados" para remover todos os registros (solicitará confirmação).

🤝 Contribuição
Este é um projeto individual.
