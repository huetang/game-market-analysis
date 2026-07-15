-- database: ../database/game_market_analysis.db

SELECT 'Publisher' AS table_name, COUNT(*) FROM Publisher
UNION ALL
SELECT 'Developer', COUNT(*) FROM Developer
UNION ALL
SELECT 'Genre', COUNT(*) FROM Genre
UNION ALL
SELECT 'Platform', COUNT(*) FROM Platform
UNION ALL
SELECT 'Game', COUNT(*) FROM Game
UNION ALL
SELECT 'Game_Release', COUNT(*) FROM Game_Release
UNION ALL
SELECT 'Sales', COUNT(*) FROM Sales
UNION ALL
SELECT 'Steam_Metrics', COUNT(*) FROM Steam_Metrics;