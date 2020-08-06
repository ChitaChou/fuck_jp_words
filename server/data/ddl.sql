/* 词汇分组表：分组ID、分组名称、创建时间、更新时间 */
CREATE TABLE "main"."group" (
  "group_id" integer PRIMARY KEY AUTOINCREMENT,
  "group_name" text(50) NOT NULL,
  "add_datetime" integer NOT NULL,
  "upd_datetime" integer NOT NULL
);

/* 词汇表：词汇ID、分组ID、日语词汇、中文翻译、创建时间、更新时间 */
CREATE TABLE "main"."words" (
  "words_id" integer PRIMARY KEY AUTOINCREMENT,
  "group_id" integer NOT NULL,
  "words_jp" text(150) NOT NULL,
  "trans_cn" text(150) NOT NULL,
  "add_datetime" integer NOT NULL,
  "upd_datetime" integer NOT NULL
);

/* 考试记录表：考试ID（创建时时间戳）、小题ID、类型（汉译日-1；日译汉-2）、词汇ID、答案、创建时间、更新时间 */
CREATE TABLE "main"."test_record" (
  "test_id" integer,
  "record_id" integer,
  "type" integer NOT NULL,
  "words_id" integer NOT NULL,
  "answer" text(150),
  "add_datetime" integer NOT NULL,
  "ans_datetime" integer
);

/* 为考试记录表添加复合主键 */
create unique index uk_tr on test_record (record_id);

/* 考试结果表：考试ID、分数、完成时间 */
CREATE TABLE "main"."test_result" (
  "test_id" integer PRIMARY KEY,
  "score" integer NOT NULL,
  "finish_datetime" integer NOT NULL
);