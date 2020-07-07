# Algo Positivo
Projeto integrador do 2º período de Análise e Desenvolvimento de Sistemas, Faculdade de Tecnologia de São José dos Campos.
Este é um projeto da parceria entre a FATEC de São José dos Campos e a SPC Brasil.

## Motivação
Com a mudança do modelo de operação do Cadastro Positivo, surgiu a necessidade de
realizar uma gestão de informação mais eficaz para garantir a qualidade, o uso adequado e
gerar valor através dos dados. E para gerar valor através destes dados, será mapeado de
forma geral o perfil dos clientes, de modo que a área de marketing possa compreender
melhor quem são seus clientes e criar campanhas mais assertivas para determinado nicho,
ajudando na tomada de decisões.

## Solução 
Um software capaz de analisar dados e gerar um relatório com informações dos clientes,
contendo alguns indicadores que serão úteis para a equipe da área de marketing da SPC
Brasil.

## Funcionamento 
Será desenvolvido um programa em Python onde ele será responsável por gerar as
informações úteis e enviar para todos os e-mails cadastrados em um banco de dados
SQLite3.
Os dados que serão gerados são: total e média de idade dos clientes por região, estado,
sexo, faixa etária, quantidade de transações por modalidade de cada região e faixa etária. Os
dados serão enviados no formato de arquivo JSON para que possa ser aberto em outras
ferramentas de análise como Excel.
Primeiramente o programa vai ler os dados dos clientes e de operações para extrair as
informações necessárias para realizar a análise, evitando dados incompletos, como
operações com IDs de pessoas não cadastradas na base, ou estado não encontrado.
Após a filtragem para obter dados confiáveis, o programa passa para a etapa de analisar e
gerar os dados que serão usados pela área de marketing.
E por fim, após estar pronto o arquivo com os dados úteis, eles serão enviados de forma
automática para os endereços de e-mail cadastrados.

## Desenvolvedores:  
[*Wesley Dias (PO)*](https://github.com/WeDias)  
[*Israel Augusto (MASTER)*](https://github.com/IsraelAugusto0110)   
[*Denis Lima*](https://github.com/Denis-Lima)  
[*Natalia Biscaro*](https://github.com/NataliaBiscaro)   
[*Euclides Rezende*](https://github.com/euclas)
