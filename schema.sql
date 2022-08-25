DROP TABLE IF EXISTS utente;
CREATE TABLE utente (
    nome TEXT PRIMARY KEY
);

DROP TABLE IF EXISTS ruolo;
CREATE TABLE ruolo (
    nome TEXT PRIMARY KEY
);

DROP TABLE IF EXISTS relazione;
CREATE TABLE relazione (
  utente TEXT,
  ruolo TEXT,
  CONSTRAINT PK_relazione PRIMARY KEY (utente, ruolo),
  CONSTRAINT FK_utente FOREIGN KEY (utente) REFERENCES utente (nome),
  CONSTRAINT FK_ruolo FOREIGN KEY (ruolo) REFERENCES ruolo (nome)
);