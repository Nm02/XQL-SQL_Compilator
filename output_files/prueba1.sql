DROP TABLE catalogo;
UPDATE catalogo SET precio = 45 WHERE producto = 'Smartphone';
SELECT producto, codigo FROM catalogo WHERE precio > 50;
CREATE TABLE catalogo (producto VARCHAR, precio INT);