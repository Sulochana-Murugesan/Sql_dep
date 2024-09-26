CREATE PROCEDURE ins
AS
BEGIN
    DECLARE @i INT = 1;
    DECLARE @random_name NVARCHAR(100);
    DECLARE @random_position NVARCHAR(100);
    DECLARE @random_notes NVARCHAR(MAX);

    WHILE @i <= 1000
    BEGIN
        -- Generate random name and position
        SET @random_name = 'Employee ' + CAST(@i AS NVARCHAR(10));
        SET @random_position = 'Position ' + CAST((FLOOR(1 + RAND() * 10)) AS NVARCHAR(10));

        -- Generate random notes with special characters and newlines
        SET @random_notes = 'Note 1: ' + CHAR(FLOOR(32 + RAND() * 95)) + 
                            ' Special Char: ' + CHAR(FLOOR(32 + RAND() * 95)) + 
                            CHAR(10) + 
                            'Note 2: ' + CHAR(FLOOR(32 + RAND() * 95)) + 
                            ' Another Special Char: ' + CHAR(FLOOR(32 + RAND() * 95));

        -- Insert into table
        INSERT INTO employee (name, position, notes) 
        VALUES (@random_name, @random_position, @random_notes);

        SET @i = @i + 1;
    END
END;
EXEC ins;