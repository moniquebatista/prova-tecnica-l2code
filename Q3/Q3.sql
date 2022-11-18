//Questão 3 prova L2 CODE 
//PostgreSQL
CREATE TABLE contratos(
	cod_contratos int,
	valor_parcela int,
	parcela int,
	PRIMARY KEY(cod_contratos)
);
CREATE TABLE pessoas(
	cod_pessoas int,
	nome varchar(60),
	contrato_id int,
	inadimplente varchar(1),
	dt_completo date,
	PRIMARY KEY(cod_pessoas),
	FOREIGN KEY(contrato_id) REFERENCES contratos(cod_contratos) 
);
CREATE TABLE pagamentos(
	cod_pagamentos int,
	pessoa_cod int,
	dt_pagamento date,
	PRIMARY KEY(cod_pagamentos),
	FOREIGN KEY(pessoa_cod) REFERENCES pessoas(cod_pessoas)
);

insert into contratos values (1, 150, 100);
insert into contratos values (2, 300, 48);
insert into contratos values (3, 550, 24);
insert into contratos values (4, 1000, 12);

insert into pessoas values (1,'Cristian Ghyprievy', 2,'S', NULL);
insert into pessoas values (2,'Joana Cabel', 1,'S', NULL );
insert into pessoas values (3,'John Serial', 3,'S', NULL );
insert into pessoas values (4,'Michael Seven',2,'N', '2022-09-25' );

insert into pagamentos values (1, 4, '2022-09-01');
insert into pagamentos values (2, 3, '2022-09-05');
insert into pagamentos values (3, 1, '2022-09-19');
insert into pagamentos values (4, 2, '2022-09-25');

SELECT pessoas.nome, Extract('Day' From pagamentos.dt_pagamento) 
AS dia_mes, contratos.valor_parcela from pessoas INNER JOIN pagamentos 
ON pagamentos.pessoa_cod = pessoas.cod_pessoas
INNER JOIN contratos on pessoas.contrato_id = contratos.cod_contratos
WHERE pessoas.inadimplente = 'S' ORDER BY nome;

SELECT pessoas.nome, (contratos.valor_parcela * contratos.parcela) as valor_total
from pessoas INNER JOIN contratos on pessoas.contrato_id = contratos.cod_contratos
WHERE pessoas.inadimplente = 'N';
