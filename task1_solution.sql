-- 1. Schema setup
-- Create the staging table for raw JSON data.
CREATE TABLE books (
    ordinal_number SERIAL, -- I add a SERIAL column to preserve the original order of records from the JSON file, without this, the import order is lost.
    id TEXT PRIMARY KEY, -- 'id' is set to TEXT to prevent precision loss on large integers, problem BigInt overflow
    title TEXT,
    author TEXT,
    genre TEXT,
    publisher TEXT,
    year INTEGER,
    price TEXT, -- 'price' is set to TEXT because raw data contains currency symbols ($/€)
    price_usd NUMERIC -- add column that stores changed values
);
-- Import 'task1_d.json' into 'books' table using DataGrip Import Tool here: database-task-1/tables/books (Import/Export --> Import Data From File(s)...)

-- 2. Data cleaning and transformation
-- Remove currency symbols using Regex and convert to Numeric.
-- Apply exchange rate: EUR to USD (rate: 1.2).
UPDATE books
SET price_usd =
        CASE
            WHEN price LIKE '€%' THEN
                CAST(regexp_replace(price, '[^\d.]', '', 'g') AS NUMERIC) * 1.2
            ELSE
                CAST(regexp_replace(price, '[^\d.]', '', 'g') AS NUMERIC)
            END
WHERE id IS NOT NULL;

--Round the calculated USD prices to 2 decimal places.
UPDATE books
SET price_usd = ROUND(price_usd, 2)
WHERE id IS NOT NULL;

--3. Analysis
CREATE VIEW books_summary AS
SELECT
    year AS "publication_year",
    COUNT(*) AS "book_count",
    ROUND(AVG(price_usd), 2) AS "average_price"
FROM books
GROUP BY year
ORDER BY year DESC;

--4. Validation
SELECT * FROM books_summary;
SELECT COUNT(*) AS total_books_imported FROM books;
SELECT COUNT(*) AS total_rows_count FROM books_summary;
