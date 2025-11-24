--1. Schema setup
CREATE TABLE "second-solution".books_staging (
    id TEXT,
    title TEXT,
    author TEXT,
    genre TEXT,
    publisher TEXT,
    year INTEGER,
    price TEXT
);

--2. Data cleaning
CREATE TABLE "second-solution".books AS
SELECT
    id,
    title,
    author,
    genre,
    publisher,
    year,
    ROUND(
            CASE
                WHEN price LIKE '€%' THEN

                    CAST(TRANSLATE(price, '€', '') AS NUMERIC) * 1.2
                WHEN price LIKE '$%' THEN
                    CAST(TRANSLATE(price, '$', '') AS NUMERIC)
                END, 2
    ) AS price_usd
FROM "second-solution".books_staging;

ALTER TABLE "second-solution".books ADD PRIMARY KEY (id);

-- 3. Analysis
CREATE VIEW "second-solution".books_summary AS
SELECT
    year AS "publication_year",
    COUNT(*) AS "book_count",
    ROUND(AVG(price_usd), 2) AS "average_price"
FROM "task-1".books
GROUP BY year
ORDER BY year DESC;

-- 4. Validation
SELECT * FROM "second-solution".books_summary;

