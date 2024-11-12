DROP TABLE IF EXISTS air_quality CASCADE;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS metadata;


CREATE OR REPLACE FUNCTION verify_aqhi_value_in_range(aqhi SMALLINT) RETURNS BOOLEAN
    LANGUAGE SQL
    IMMUTABLE
    RETURN aqhi >= 1 AND aqhi <= 10;

CREATE TABLE air_quality (
    identity TEXT PRIMARY KEY,
    baseURL TEXT NOT NULL,
    subURL TEXT NOT NULL,
    rel_or_ret BOOLEAN NOT NULL,
    data_collection_time INT NOT NULL, 
    aqhi SMALLINT NOT NULL,
    CHECK (verify_aqhi_value_in_range(aqhi))
);

CREATE INDEX message_id ON air_quality (aqhi)
    INCLUDE (baseURL, subURL, rel_or_ret);

CREATE TABLE location (
    identity TEXT PRIMARY KEY,
    city TEXT NOT NULL,
    FOREIGN KEY (identity) REFERENCES air_quality(identity)
); 

CREATE TABLE metadata (
    identity TEXT PRIMARY KEY,
    topic TEXT NOT NULL,
    publish_time INT NOT NULL,
    from_cluster TEXT,
    to_cluster TEXT,
    size SMALLINT,
    FOREIGN KEY (identity) REFERENCES air_quality(identity)
);
