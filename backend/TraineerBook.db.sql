BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Activity" (
	"id"	INTEGER NOT NULL,
	"image"	TEXT,
	"description"	TEXT,
	"teacher"	TEXT,
	"class_space"	TEXT,
	FOREIGN KEY("class_space") REFERENCES "ClassRoom"("name"),
	FOREIGN KEY("teacher") REFERENCES "Teacher"("name"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "ClassRoom" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Comment" (
	"id"	INTEGER NOT NULL,
	"user"	TEXT,
	"content"	TEXT,
	FOREIGN KEY("user") REFERENCES "User"("email"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Incident" (
	"id"	INTEGER NOT NULL,
	"user"	TEXT,
	"reservation"	TEXT,
	"content"	TEXT,
	FOREIGN KEY("user") REFERENCES "User"("email"),
	FOREIGN KEY("reservation") REFERENCES "Reservation"("product"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Product" (
	"id"	INTEGER NOT NULL,
	"product_hour_init"	TEXT,
	"product_hour_fin"	TEXT,
	"quantity"	INTEGER,
	"price"	INTEGER,
	"activity"	TEXT,
	FOREIGN KEY("activity") REFERENCES "Activity"("description"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Reservation" (
	"id"	INTEGER NOT NULL,
	"user"	TEXT,
	"product"	TEXT,
	"buy_date"	TEXT,
	"buy_method"	TEXT,
	FOREIGN KEY("product") REFERENCES "Product"("activity"),
	FOREIGN KEY("user") REFERENCES "User"("email"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Teacher" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER NOT NULL,
	"email"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
COMMIT;
