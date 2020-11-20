import configparser




# DROP TABLES

staging_videos_table_drop = "DROP TABLE IF EXISTS youtube.staging_videos;"
videos_trending_table_drop = "DROP TABLE IF EXISTS youtube.videos_trending;"
videos_table_drop = "DROP TABLE IF EXISTS youtube.videos;"
videos_notitle_table_drop = "DROP TABLE IF EXISTS youtube.videos_notitle;"
time_table_drop = "DROP TABLE IF EXISTS youtube.time;"
category_table_drop = "DROP TABLE IF EXISTS youtube.category;"

# CREATE TABLES

staging_videos_table_create= ("""
CREATE TABLE IF NOT EXISTS youtube.staging_videos (
  id INT IDENTITY(0,1) PRIMARY KEY,
  video_id VARCHAR NOT NULL,
  trending_date VARCHAR SORTKEY,
  title VARCHAR,
  channel_title VARCHAR,
  category_id SMALLINT,
  publish_time VARCHAR,
  tags VARCHAR(max),
  views INT,
  likes INT,
  dislikes INT,
  comment_count INT,
  thumbnail_link VARCHAR,
  comments_disabled BOOLEAN,
  ratings_disabled BOOLEAN,
  video_error_or_removed BOOLEAN,
  description VARCHAR(max),
  country VARCHAR(2)
)
""")



videos_trending_table_create = ("""
CREATE TABLE IF NOT EXISTS youtube.videos_trending(
  "videos_trending_id" INT IDENTITY(0,1) PRIMARY KEY,
  "video_id" VARCHAR NOT NULL DISTKEY,
  "trending_date" VARCHAR NOT NULL SORTKEY,
  "views" INT,
  "likes" INT,
  "dislikes" INT,
  "comment_count" INT,
  "comments_disabled" BOOLEAN,
  "ratings_disabled" BOOLEAN,
  "video_error_or_removed" BOOLEAN,
  "country" VARCHAR(2)
)
""")

videos_table_create = ("""
CREATE TABLE IF NOT EXISTS youtube.videos(
  "video_id" VARCHAR NOT NULL DISTKEY,
  "title" VARCHAR,
  "channel_title" VARCHAR,
  "category_title" VARCHAR,
  "country" VARCHAR(2),
  "publish_time" TIMESTAMP,
  "tags" VARCHAR(max),
  "thumbnail_link" VARCHAR,
  "description" VARCHAR(max),
  PRIMARY KEY ("video_id","country")
)
""")

videos_notitle_table_create = ("""
CREATE TABLE IF NOT EXISTS youtube.videos_notitle(
  "video_id" VARCHAR NOT NULL DISTKEY,
  "channel_title" VARCHAR,
  "category_title" VARCHAR,
  "country" VARCHAR(2),
  "publish_time" TIMESTAMP,
  PRIMARY KEY ("video_id","country")
)
""")


time_table_create = ("""
CREATE TABLE IF NOT EXISTS youtube.time(
  "trending_date" VARCHAR PRIMARY KEY,
  "year" SMALLINT,
  "month" SMALLINT,
  "day" SMALLINT
) DISTSTYLE ALL
""")

category_table_create = ("""
CREATE TABLE IF NOT EXISTS youtube.category (
  "category_id" SMALLINT,
  "category_title" VARCHAR,
  "country_code" VARCHAR(2),
  PRIMARY KEY ("category_id","country_code")
) DISTSTYLE ALL
""")



# QUERY LISTS


create_table_queries = [staging_videos_table_create,videos_table_create, videos_notitle_table_create, videos_trending_table_create,time_table_create,category_table_create]

drop_table_queries =[staging_videos_table_drop,videos_table_drop, videos_notitle_table_drop, videos_trending_table_drop ,time_table_drop,category_table_drop]

check_table_queries = ["youtube.staging_videos","youtube.videos_trending","youtube.videos","YouTube.videos_notitle","youtube.category","youtube.time"]
