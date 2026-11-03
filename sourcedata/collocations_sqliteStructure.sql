CREATE TABLE collocations (
  id int(11) NOT NULL UNIQUE,
  vocalized varchar(30) DEFAULT NULL,
  unvocalized varchar(30) DEFAULT NULL,
  rule varchar(30) DEFAULT NULL,
  category varchar(30) NOT NULL,
  note text
);