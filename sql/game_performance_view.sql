-- database: ../database/game_market_analysis.db

CREATE VIEW game_performance_view AS

SELECT
    g.game_id,
    g.title,
    g.release_date,

    pub.publisher_name,
    dev.developer_name,
    gen.genre_name,

    p.platform_type,

    SUM(s.total_sales) AS total_sales,
    SUM(s.north_america_sales) AS north_america_sales,
    SUM(s.europe_sales) AS europe_sales,
    SUM(s.japan_sales) AS japan_sales,
    SUM(s.other_sales) AS other_sales,


    AVG(s.critic_score) AS average_critic_score,

    MAX(sm.peak_ccu) AS peak_ccu,
    MAX(sm.positive_reviews) AS positive_reviews,
    MAX(sm.negative_reviews) AS negative_reviews,
    MAX(sm.price) AS price,
    MAX(sm.average_playtime) AS average_playtime

FROM Game g

LEFT JOIN Publisher pub
    ON g.publisher_id = pub.publisher_id

LEFT JOIN Developer dev
    ON g.developer_id = dev.developer_id

LEFT JOIN Genre gen
    ON g.genre_id = gen.genre_id

LEFT JOIN Game_Release gr
    ON g.game_id = gr.game_id

LEFT JOIN Platform p
    ON gr.platform_id = p.platform_id

LEFT JOIN Sales s
    ON gr.release_id = s.release_id

LEFT JOIN Steam_Metrics sm
    ON g.game_id = sm.game_id

GROUP BY
    g.game_id,
    g.title,
    g.release_date,
    pub.publisher_name,
    dev.developer_name,
    gen.genre_name,
    p.platform_type;