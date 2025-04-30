CREATE DATABASE IF NOT EXISTS trade_db;
USE trade_db;

CREATE TABLE IF NOT EXISTS trade_summary (
    typecode VARCHAR(10),
    refyear INT,
    reporteriso VARCHAR(5),
    reporterdesc VARCHAR(255),
    partneriso VARCHAR(5),
    partnerdesc VARCHAR(255),
    flowcode VARCHAR(10),
    cmdcode VARCHAR(20),
    cmddesc VARCHAR(255),
    qty FLOAT,
    netwgt FLOAT,
    cifvalue BIGINT,
    fobvalue BIGINT,
    primaryvalue BIGINT,
    isreported BOOLEAN
);
