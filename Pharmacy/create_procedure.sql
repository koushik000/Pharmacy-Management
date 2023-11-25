-- Stored procedure to get drug information by name
CREATE PROCEDURE IF NOT EXISTS get_drug_info(IN drug_name VARCHAR(255))
BEGIN
    SELECT * FROM drugs WHERE drug_name = drug_name;
END;
