// Scala Essential Training for Data Science - Ben at Lynda,

// Parallel collections,
val v = (1 to 1000).toArray
val pv = v.par
pv.map(_ * 2)

pv.reduce(_ - _)

// Intro

var a : Double = 4;
var a : Int = 5;
var l : Long = 845789
var f = 1.23f
// f: Float = 1.23
var s = "Hello"

// Vector, addresses the inefficiency for random access on lists
var vec = Vector(1,2,3,4,5)

// arrays
val a0 = (1 to 4).toArray
val a1 = Array(1,2,3,4,5)
a1(2)
a1.length;
val a2: Array[Int] = new Array[Int](4)
val a3 = Array.ofDim[Int](5,5)

a1 ++ a2; // concat
// or, 
Array.concat(a1, a2)

// maps
scala> 
var capitcals = Map("BC" -> "Victoria", "AB" -> "Edmondon")
capitcals get "DE"
capitcals contains "DE"
// res16: Boolean = false
capitcals getOrElse ("DE", "None")
// res15: String = None

capitcals.keys;
// res1: Iterable[String] = Set(BC, AB)
capitcals.values;
//res2: Iterable[String] = MapLike(Victoria, Edmondon)

capitcals + ("ON"->"Toronto")
capitcals - "ON"

capitcals.keys.foreach((prov) => {
  printf("%s, %s \n", prov, capitcals(prov))
})

for ((k,v) <- capitcals) {
  printf("Key: %s, Value: %s \n", k, v)
}

// expressions
(3>4) && (5<10)

// Function
def myFunction(a:Int, b:Int) : Int = {
  val c = a + b
  return c
}
myFunction(1,2)

def myProcedure(inStr : String) : Unit = {
  printf("%s is good.", inStr)
}
myProcedure("Juliet")

// Object
val y = Array("Tom", "Phil", "Scott", "Ivy")
y.sorted

class loc(var x:Int, var y:Int, private var z:Int = 3)
val loc1 = new loc(2, 9)
loc1.y 

class loc(var x:Int, var y:Int, private var z:Int = 3) {
  var a: Int = x
  var b: Int = y 
  def move(delta_a: Int, delta_b: Int) {
    a = a + delta_a
    b = b + delta_b
  }
}

val point1 = new loc(2, 2)
(point1.x , point1.a)
point1.move(1,1)
(point1.x , point1.a)

// RDD
import scala.util.Random
val bigRng = scala.util.Random.shuffle(1 to 100)
val bigRng = 1 to 10
val bigRng = Array(2,2,3,1,5,7)

val bigPRng = sc.parallelize(bigRng);
bigPRng.collect()
bigPRng.take(20)

// RDD to DataFrame, toDF,
val rdd1 = bigPRng.map(num => (num, num + " x " + num + " is: ", num * 2))
val df1 = rdd1.toDF("id","strCol1","intCol2")
df1.show()

val bigPRng2s = bigPRng.map(_ * 2)
val bigPRng2 = bigPRng.map(num => num * 2)
bigPRng2.mean;
bigPRng2.count;
bigPRng2.stats;

def div(x:Int) : Boolean = {val y:Int=(x%3); return(y==0)}

def div(x:Int) : Boolean = {
    val y:Int=(x%3)
    return(y==0)
}

val bigBool = bigPRng2.map(div(_)).take(20);

import scala.collection.parallel.immutable.ParVector
val pvec200 = ParVector.range(0,200)

val republic = sc.textFile("LICENSE")
republic.take(20).foreach(println)
val lineWithApache = republic.filter(line => line.contains("Apache"));
lineWithApache.take(20).foreach(println(_))


// DataFrame

import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().appName("DFExample").getOrCreate();

val df_emp = spark.read.option("header", "true").csv("/Users/charliezhu/Downloads/Ex_Files_Scala_EssT_Data_Science/Exercise Files/Chapter 5/05_01/employee.txt")
val df_cr = spark.read.option("header", "true").csv("/Users/charliezhu/Downloads/Ex_Files_Scala_EssT_Data_Science/Exercise Files/Chapter 5/05_01/country_region.txt")
df_emp.createOrReplaceTempView("emp")
val sqldf_emp = spark.sql(""" select department, gender, count(*) from emp 
where id < 10
  --and gender = Male
group by department, gender
""")

spark.sql(""" select department, gender, count(*) from emp 
where id < 100
  and department = "'Automotive'"
group by department, gender
""").show()

spark.sql(""" select department, gender from emp where gender = "'Male'" """).show()
spark.sql(""" select id, department, gender from emp where department = "'Automotive'" """).show()
spark.sql(""" select department, gender from emp where id < 5 """).show()

val df_emp_region = df_emp.join(df_cr, "region_id")
df_emp_region.columns

// JSON input,
val df_json_dd = spark.read.json("/Users/charliezhu/Downloads/Ex_Files_Scala_EssT_Data_Science/Exercise Files/Chapter 5/05_04/dept_div.json")

val textFile = spark.read.textFile("README.md")
// textFile: org.apache.spark.sql.Dataset[String] = [value: string]

val df_emp = spark.read.option("header", "true").csv("/Users/charliezhu/Downloads/Ex_Files_Scala_EssT_Data_Science/Exercise Files/Chapter 5/05_01/employee.txt")
// df_emp: org.apache.spark.sql.DataFrame = [id: string, last_name: string ... 7 more fields]

Quick Start
--
https://spark.apache.org/docs/latest/quick-start.html

val tf = spark.read.textFile("LICENSE");
tf.count();
tf.take(5).foreach(println);

val linsWithApache = tf.filter(line => line.contains("Apache"));

tf.filter(line => line.contains("Apache")).count();
tf.filter(line => line.contains("Apache")).take(5).foreach(println)
tf.filter(line => line.contains("Apache")).collect().foreach(println)

tf.filter(line => line.contains("Apache")).show()

tf.map(line => line.split(" ").size)
res22: Array[Int] = Array(35, 31, 25, 1, 11)

tf.map(line => line.split(" ").size).reduce((a,b) => Math.max(a,b));

* MapReduce
tf.flatMap(line => line.split(" "))
tf.flatMap(line => line.split(" ")).groupByKey(identity).count().show()

val wordCount = tf.flatMap(line => line.split(" ")).groupByKey(identity).count();
wordCount.collect()
scala> wordCount.show()
+--------------------+--------+
|               value|count(1)|
+--------------------+--------+
|               those|       3|
|            brackets|       1|
|                (New|       4|
+--------------------+--------+
only showing top 20 rows

* Self-Contained Applications,




// blog install spark 2.2.1 on Mac

Spark is incompatible with Java 9.
Install Java 8 instead.

# to uninstall Java 9
brew cask uninstall java

Here is the complete and simple installation steps for spark on Mac :

brew tap caskroom/versions
brew cask search java
brew cask install java8

# brew install scala  # You might need these step, 
brew install apache-spark


./bin/spark-shell --master local[2]

./bin/spark-shell --master local[1]


// Connect o PostgresQL

$>
brew info postgres

// Start manually:

pg_ctl -D /usr/local/var/postgres start

// or, write stats to log,
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

// Stop manually:

pg_ctl -D /usr/local/var/postgres stop

// Status

pg_ctl -D /usr/local/var/postgres status


createdb scala_db
createuser scala_user
psql -U scala_user -d scala_db -a -f "/Users/charliezhu/Downloads/Ex_Files_Scala_EssT_Data_Science/Exercise Files/Chapter 3/03_02/emps.sql"
psql -U scala_user -d scala_db

// scala -classpath ~/app/lib/postgresql-42.1.1.jre6.jar
bin/spark-shell -classpath ~/app/lib/postgresql-42.1.1.jre6.jar

// Scala code,
import java.sql.Driver
import java.sql.DriverManager
import java.sql.Connection

val driver = "org.postgresql.Driver"
val url = "jdbc:postgresql://localhost/scala_db?user=scala_user"
Class.forName(driver)
var connection: Connection = null

connection = DriverManager.getConnection(url)
val statement = connection.createStatement()
val resultSet = statement.executeQuery("select * from emps limit 5")
resultSet.next
resultSet.getString("last_name")
resultSet.getString("department")

while ( resultSet.next() ) {
  val last_name = resultSet.getString("last_name")
  val dept = resultSet.getString("department")
  printf("%s: %s \n", dept, last_name)
}

// Prepare SQL statement
val queryStr = "select * from emps where department = ? "
val ps = connection.prepareStatement(queryStr)
ps.setString(1, "Home")
val rs = ps.executeQuery()

while ( rs.next() ) {
  val last_name = rs.getString("last_name")
  val dept = rs.getString("department")
  val startDate = rs.getString("start_date")
  printf("%s: %s \t %s \n", dept, last_name, startDate)
}


// Start Kafka

cd /Users/charliezhu/app/kafka_2.12-1.0.0/

# start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties &
sleep 2
# start Kafka Server
bin/kafka-server-start.sh config/server.properties &
sleep 2
# create new topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic1

# see the topic
bin/kafka-topics.sh --list --zookeeper localhost:2181

# run producer, sending message
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic1

// create methods that take variable-arguments (varargs) fields.
// Use _* to adapt a sequence
// adapt a sequence (Array, List, Seq, Vector, etc.) so it can be used as an argument 
// for a varargs field:

def printAll(strings: String*) {
  strings.foreach(x => { printf(" it is a %s \n", x)})
}
def printAll(strings: String*) {
  for (x <- strings) {
    printf(" it is a %s \n", x)
  }
}

printAll("AA", "BB", "DD")

val fruits = List("apple", "banana", "cherry")
printAll(fruits: _*)

val fruits = Array("apple", "banana", "cherry")
printAll(fruits: _*)


object Main extends App {
  val nums = Seq(1,2,3)
  for (n <- nums) println(n)
}


val pcFile = sc.textFile("/Users/charliezhu/work/log/pc2.txt")
val rdd1 = pcFile.map(x => x.split(",")).map(x => Array(x(2), x(3), x(4)))
rdd1.foreach(x => println(x(0), x(1)))
rdd1.map(x => (x(0), x(1).trim.toLong)).reduceByKey((a,b) => {a + b}).foreach(println)

// RDD need Seq / Array / List, as element data type, 
// DataFrame need tuple, and element data type,

val pc = pcFile.map(x => x.split(",").map(_.trim)).map(x => (x(2).toLowerCase, x(3).toLong, x(4).toLong))
val df = pc.toDF("event","users","count")
df.show()

df.groupBy("event").agg(sum("users"), sum("count")).show()

df.filter("event like 'purchase%'")
.groupBy($"event").agg(sum($"users"), min($"users"), max("users")).show

df.orderBy(asc("event")).show;
df.orderBy($"event".desc).show;

df.filter("event = 'purchase_success'").show()
df.filter("event like 'purchase%'").show()
df.filter($"event" === "purchase_success").show()

df.filter($"users" === 34).show()
df.filter("users = 34").show()
df.where("users = 34 or users = 178").show()
df.where($"users" === 34 || $"users" === 178).show()

df.registerTempTable("purchase_sample")
sql("select event, sum(users), sum(count) from purchase_sample group by event").show

// select selectExpr



// spark is a SparkSession
val csv_df = spark.read
.format("csv")
.option("header","true")
.option("inferSchema","true")
.load("/Users/charliezhu/work/log/pc.txt")

val csv_df = spark.read.format("csv").option("header","true").load("/Users/charliezhu/work/log/pc.txt")
.show

val df = spark.sql("SELECT * FROM csv.`/Users/charliezhu/work/log/pc.txt`")

// purchase_initialized_fail
// custom schema,

import org.apache.spark.sql.types._

val customSchema = StructType(Array(
StructField("ds", StringType, true),
StructField("game_id", StringType, true),
StructField("app_id", StringType, true),
StructField("se1", StringType, true),
StructField("player_id", StringType, true),
StructField("apiversion", StringType, true),
StructField("version_name", StringType, true),
StructField("event", StringType, true),
StructField("system_device", StringType, true),
StructField("system_platform", StringType, true),
StructField("platform", StringType, true)
));


val csv_df = spark.read.format("csv").schema(customSchema).load("/Users/charliezhu/work/log/pf.csv")
// csv_df.orderBy(asc("ds"), asc("player_id")).show
csv_df.createOrReplaceTempView("purchase_fail")
val sort_df = sql("select ds, player_id, app_id, se1, system_device, event from purchase_fail order by ds, player_id")
sort_df.show 

sort_df.write.format("csv").save("/Users/charliezhu/work/log/pf_sort")

// $example on:programmatic_schema$

import org.apache.spark.sql.Row
import org.apache.spark.sql.SparkSession

import org.apache.spark.sql.types._

import spark.implicits._

// $example on:programmatic_schema$
// Create an RDD
val peopleRDD = spark.sparkContext.textFile("examples/src/main/resources/people.txt")

// The schema is encoded in a string
val schemaString = "name age"

val fields = schemaString.split(" ").map(fieldName => StructField(fieldName, StringType, nullable = true))

val schema = StructType(fields)

// Convert records of the RDD (people) to Rows
val rowRDD = peopleRDD.map(_.split(",")).map(attributes => Row(attributes(0), attributes(1).trim))

// Apply the schema to the RDD
val peopleDF = spark.createDataFrame(rowRDD, schema)

// Creates a temporary view using the DataFrame
peopleDF.createOrReplaceTempView("people")

// SQL can be run over a temporary view created using DataFrames
val results = spark.sql("SELECT name FROM people")

// The results of SQL queries are DataFrames and support all the normal RDD operations
// The columns of a row in the result can be accessed by field index,
results.map(attributes => "Name: " + attributes(0)).show()

// accesse columns of a row, by field name
results.map(attributes => "Name: " + attributes.getAs[String]("name")).show()


// 
    // Alternatively, a DataFrame can be created for a JSON dataset represented by
    // a Dataset[String] storing one JSON object per string

val otherPeopleDataset = spark.createDataset("""{"name":"Charlie","address":{"city":"Victoria","state":"BC"}}""" ::"""{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}""" :: Nil)
otherPeopleDataset.show()
val otherPeople = spark.read.json(otherPeopleDataset)
otherPeople.show()


// write to Kafka,

Create the built.sbt
Let’s create an sbt project and add following dependencies in build.sbt.

libraryDependencies ++= Seq("org.apache.spark" % "spark-sql_2.11" % "2.2.0",
                        "org.apache.spark" % "spark-sql-kafka-0-10_2.11" % "2.2.0",
                        "org.apache.kafka" % "kafka-clients" % "0.11.0.1")
Create the SparkSession
Now, we have to import the necessary classes and create a local SparkSession, 
the starting point of all functionalities in Spark:

val spark = SparkSession
 .builder
 .appName("Spark-Kafka-Integration")
 .master("local")
 .getOrCreate()


val mySchema = StructType(Array(
 StructField("id", IntegerType),
 StructField("name", StringType),
 StructField("year", IntegerType),
 StructField("rating", DoubleType),
 StructField("duration", IntegerType)
))

val streamingDataFrame = spark.readStream.schema(mySchema).csv("/Users/charliezhu/work/log/moviedata.csv")

streamingDataFrame.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value")
.writeStream 
.format("kafka") 
.option("topic", "test") 
.option("kafka.bootstrap.servers", "localhost:9092") 
.option("checkpointLocation", "/Users/charliezhu/work/log/checkpoint/") 
.start()

import spark.implicits._
val df = spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092")
  .option("subscribe", "test")
  .load()

val df1 = df.selectExpr("CAST(value AS STRING)", "CAST(timestamp AS TIMESTAMP)").as[(String, Timestamp)]
  .select(from_json($"value", mySchema).as("data"), $"timestamp")
  .select("data.*", "timestamp")

df1.writeStream
    .format("console")
    .option("truncate","false")
    .start()
    .awaitTermination()

// for loop, and yield,

val y = for (e <- (1 to 3)) yield e
