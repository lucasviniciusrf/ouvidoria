# ouvidoria
Projeto de Ouvidoria -> Python e MySQL

Este sistema realiza o cadastro, listagem, atualização, exclusão e busca de manifestações em um banco de dados MySQL.

🔌 Conexão com o Banco
- criarConexao(...): Conecta ao MySQL.
- encerrarConexao(...): Encerra a conexão.

🧾 Operações com o Banco
- insertNoBancoDados(...): Insere dados.
- listarBancoDados(...): Lista dados.
- atualizarBancoDados(...): Atualiza registros.
- excluirBancoDados(...): Remove registros.

 Funcionalidades da Ouvidoria
- listagemManifestacoes(conn): Lista todas as manifestações.
- listagemTipo(conn): Lista por tipo (1: Reclamação, 2: Sugestão, 3: Elogio).
- adicionarManifestacao(conn): Adiciona nova manifestação com CPF, nome, tipo e texto.
- atualizarInformacoes(conn): Atualiza o texto da manifestação pelo CPF (parcial ou completo).
- pesquisarManifestacoes(conn): Busca manifestação por CPF.
- excluirManifestacoes(conn): Exclui manifestação por CPF.
- quantidadeManifestacoes(conn): Mostra o total de manifestações registradas.

📋 Menu Principal (laço while)
Apresenta as opções para o usuário:
1. Listar manifestações
2. Listar por tipo
3. Adicionar nova
4. Ver quantidade
5. Buscar por CPF
6. Atualizar
7. Excluir
8. Sair

Tudo organizado com tratamento de erros, uso de prepared statements para segurança, e conexão robusta com o banco de dados. Prontinho para rodar e usar como base em sistemas reais!
