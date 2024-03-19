CREATE DATABASE wsj;
use wsj;
CREATE TABLE stocks(
	exchange CHAR( 35 ) NOT NULL,
	symbol CHAR( 255 )  NOT NULL,
	volume INT NOT NULL,
	price FLOAT(12, 2 ) NOT NULL,
	chang FLOAT(12, 2 ) NOT NULL,
	);

