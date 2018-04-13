scala cookbook

// 3.5 break and continue

import util.control.Breaks._ 

breakable {
  for (i <- 1 to 10) {
    println(i)
    if (i > 4) break // break out of the for loop
  }
}


// 5.3

def makeConnection(timeout: Int = 5000, protocol: String = "http") {
        println("timeout = %d, protocol = %s".format(timeout, protocol))
        // more code here
}

trait SentientBeing
trait Animal extends SentientBeing

case class Dog(name: String) extends Animal
case class Person(name: String, age: Int) extends SentientBeing
    // later in the code ...

def printInfo(x: SentientBeing) = x match {
  case Person(name, age) => {println(s"$name at $age")} // handle the Person 
  case Dog(name) => (println(s"$name is a dog")) // handle the Dog
}

printInfo(Person("Tom", 52))

val juliet = Dog(name = "Juliet")
printInfo(juliet)





// cat Main.scala

class Main {
  for (i <- 1 to 10) println(i)
}

scalac -Xprint:parse Main.scala

// disassemble that file with this javap command:

javap Main.class
javap -c Main.class

// 10.9. Looping over a Collection with foreach
// 11.17. Traversing a Map

val fruits: List[(Int, String)] = List((1, "apple"), (2, "orange"))

for((id, name) <- fruits) {
  println(s"$id is $name")
}

// not working
fruits.foreach {
  (id, name) => {
    println(s"$id is $name")
  }
}

<console>:14: error: missing parameter type
Note: The expected type requires a one-argument function accepting a 2-Tuple.
      Consider a pattern matching anonymous function, `{ case (id, name) =>  ... }`

fruits.foreach {
  case (id, name) => {
    println(s"$id is $name")
  }
}

fruits.foreach {
  t1 => {
    t1 match {
      case (id, name) => {
        println(s"$id is $name")
      }
    }
  }
}

fruits.foreach {
  t1 => {
    println(s"${t1._1} is ${t1._2}")
  }
}

>>>> out put >>>>

1 is apple
2 is orange

// closure

import scala.collection.mutable.ArrayBuffer 
val fruits = ArrayBuffer("apple")
// the function addToBasket has a reference to fruits
val addToBasket = (s: String) => {
  fruits += s 
  println(fruits.mkString(", "))
}
// buyStuff method would typically be in another class,
def buyStuff(f: String => Unit, s: String) {
  f(s)
}

buyStuff(addToBasket, "cherries")
buyStuff(addToBasket, "grapes")

// 3.15. Working with a List in a Match Expression

def sum(list: List[Int]): Int = {
  list match {
    case Nil => 1
    case n :: rest => {
      println(n, rest)
      n + sum(rest)
    }
  }
}

val nums = List(1,2,3,4)

sum(nums)

//

val fruits = new Array[String](3)

// this uses a null. don't do this in the real world
var fruits: Array[String] = _

var fruits: Array[String] = Array()
fruits = Array("aa","bb","cc","dd")
var fruits: Array[String] = new Array[String](3)

val x = List(2)

1 :: x

val characters = collection.mutable.ArrayBuffer("Ben", "Jerry") // add one element

// append,
characters += "Dale"
characters += ("Gordon", "Harry")
characters.append("Laura", "Lucy")

characters ++= List("Charlie", "Daisy")

characters.sortWith(_ < _) // Ascending
characters.sortWith(_ > _) // Descending

scala.collection.mutable.ArrayBuffer[String] 
= ArrayBuffer(Ben, Jerry, Dale, Gordon, Harry, Laura, Lucy)

characters.sortBy(_.toLowerCase)
ArrayBuffer[String] = ArrayBuffer(Ben, Charlie, Daisy, Dale, Gordon, Harry, Jerry, Laura, Lucy)

```
val ourScore = List(3,2,7,9,8)

scala> ourScore.sortBy
   def sortBy[B](f: Int => B)(implicit ord: scala.math.Ordering[B]): List[Int]

scala> ourScore.sortBy(_.toString)
res42: List[Int] = List(2, 3, 7, 8, 9)

scala> ourScore.sortBy(_)
error: missing parameter type for expanded function ((x$1: <error>) => ourScore.sortBy(x$1))
       ourScore.sortBy(_)
                       ^
```
Why sortBy(_.toString) works, but .sortBy(_) did not work.
Can you elaborate `def sortBy[B](f: Int => B)` ?  
What is B ?
What is (f: Int => B) ?  ... etc.

A:  passing a lambda (or Attribute) to sortBy, 貌似 sortBy 只接收 函数 或者 属性作为参数。

// Map

val localDB = Map("url" -> "jdbc:postgresql://localhost/scala_db", "user" -> "scala_user", "password" -> "")
val devDB = Map("url" -> "jdbc:postgresql://localhost/scala_db", "user" -> "scala_user", "password" -> "")
val prodDB = Map("url" -> "jdbc:postgresql://bworks-bicloud-postgres-prod.cfnjvvaebgzj.us-east-1.rds.amazonaws.com/report"
  , "user" -> "bwdbadmin", "password" -> "fYi6NJpas4oeatss")

var dbMap = Map("localDB" -> localDB, "prodDB" -> prodDB)
dbMap += ("devDB" -> devDB)

dbMap("devDB")("user")

for ((k,v) <- dbMap) {
  println(s"$k, $v")
}

// 9.8 partial functions in Scala

trait PartialFunction[-A, +B] extends (A) => B

val divide = new PartialFunction[Int, Int] {
  def apply(x: Int) = 44 / x 
  def isDefinedAt(x: Int) = (x != 0)
}

divide.isDefinedAt(1)
divide.isDefinedAt(0)

List(0,1,2,4).map(divide)  // java.lang.ArithmeticException: / by zero

// collect method is written to test the isDefinedAt method for each element,
List(0,1,2,4).collect(divide)  // List[Int] = List(44, 22, 11)

// 11.11
import sys.process._
"find /Users/charliezhu/work -type f -exec grep -il scala {} ;".!
"find /Users/charliezhu/work -name *.scala".!

$> find /Users/charliezhu/work -type f -exec grep -il scala {} \;
$> find /Users/charliezhu/work -name *.scala -exec wc -l {} \;
"find /Users/charliezhu/work -name *.scala -exec wc -l {} ;".!

find /Users/charliezhu/work -name *.scala | xargs wc -l
val numRows = ("find /Users/charliezhu/work -name *.scala" #| "xargs wc -l").!!.trim 

("ls" #| "xargs wc -l").!
("ls" #| "wc -l").!

import sys.process._ 
val out = "which xargs".lineStream_!.headOption

// 11.12

import sys.process._
val stdout = new StringBuilder
val stderr = new StringBuilder

val outLogger = ProcessLogger(line => stdout.append(line), line => stderr.append(line))
val status = Seq("find", "/usr", "-name", "make") ! outLogger

stdout.clear
stderr.clear

// works in Scala 2.11.8, but not in 2.12.4
val status = "ls -al FRED" ! ProcessLogger(line => stdout.append(line), line => stderr.append(line))

println(status)
println("stdout: " + stdout)
println("stderr: " + stderr)

val status = Seq("find", "/usr", "-name", "make") ! ProcessLogger(stdout.append(_), stderr.append(_))
val status = Seq("find", "/usr", "-name", "make") ! ProcessLogger(line => stdout.append(line), line => stderr.append(line))

"ls -e" ! ProcessLogger((e: String) => println(" error: " + e))

// 11.13 

import sys.process._

// run command inside a Bourne shell instance
Seq("/bin/sh", "-c", "ls | wc -l").!

try {
  Seq("/bin/sh", "-c", "ls | grep scala").!!
} catch {
  case e: RuntimeException => e.printStackTrace
}

// 12.1 open and read text files in Scala

https://alvinalexander.com/scala/how-to-open-read-text-files-in-scala-cookbook-examples

// Automatically closing the resource,
Object Control {
  def using[A <: { def close(): Unit }, B](resource: A)(f: A => B): B = {
    try {
      f(resource)
    } finally {
      resource.close()
    }
  }
}

// how the using control structure works, e.g.  A <:
// https://alvinalexander.com/scala/using-control-structure-beginning-scala-david-pollak#how-the-using-control-structure-works

A and B both define types.
A can be an instance of any class that has a close() method. 
  (This is known as a structural type in Scala.)
B can be any type.

// 13.1


// 13.3 Communicate between Actors,

// https://doc.akka.io/docs/akka/current/actors.html#creating-actors
val system = ActorSystem("pingpong")
val pinger = system.actorOf(Props[Pinger], "pinger")
val ponger = system.actorOf(Props(classOf[Ponger], pinger), "ponger")  <<== diff

// cookbook,
val system = ActorSystem("PingPongSystem")
val pong = system.actorOf(Props[Pong], name = "pong")
val ping = system.actorOf(Props(new Ping(pong)), name = "ping")  <<== diff

// 14.3

import java.util.Calendar
import java.text.SimpleDateFormat
object DateUtils {

    def sysDate: String = getCurrentDateTime("YYYY-MM-dd")  // 2018-03-26
    def sysTime: String = getCurrentDateTime("h:m:s")  // 11:44:15

    // as "Thursday, November 29"
    def getCurrentDate: String = getCurrentDateTime("EEEE, MMMM d")

    // as "6:20 p.m."
    def getCurrentTime: String = getCurrentDateTime("K:m aa")

    // a common function used by other date/time functions
    private def getCurrentDateTime(dateTimeFormat: String): String = {
        val dateFormat = new SimpleDateFormat(dateTimeFormat)
        val cal = Calendar.getInstance()
        dateFormat.format(cal.getTime())
    }

}

DateUtils.getCurrentTime

DateUtils.getCurrentDate

DateUtils.sysDate

import java.text.SimpleDateFormat
import java.util.Date

object Utils {

    val DATE_FORMAT = "EEE, MMM dd, yyyy h:mm a"

    def getDateAsString(d: Date): String = {
        val dateFormat = new SimpleDateFormat(DATE_FORMAT)
        dateFormat.format(d)
    }

    def convertStringToDate(s: String): Date = {
        val dateFormat = new SimpleDateFormat(DATE_FORMAT)
        dateFormat.parse(s)
    }

}

def convertDateStringToLong(dateAsString: String): Long = {
    Utils.convertStringToDate(dateAsString).getTime
}

def convertLongToDate(l: Long): Date = new Date(l)

new Date(1504754034000L)

convertLongToDate(1504754034000L)

res37: java.util.Date = Wed Sep 06 20:13:54 PDT 2017

// 18.14

cat project/assembly.sbt

addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.6")

cat build.sbt

lazy val root = (project in file(".")).
  settings(
    name := "email_metrics",
    version := "0.1",
    scalaVersion := "2.11.12",
    mainClass in Compile := Some("campaign.Main")
  )

libraryDependencies ++= Seq(
  "org.apache.spark" % "spark-sql_2.11" % "2.2.1" % "provided",
  "org.postgresql" % "postgresql" % "42.2.1",
)

fork in run := true

run in Compile := Defaults.runTask(fullClasspath in Compile, mainClass in (Compile, run), runner in (Compile, run)).evaluated

assemblyMergeStrategy in assembly := {
  case "META-INF/MANIFEST.MF" => MergeStrategy.discard
  // case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}

sbt assembly

$ java -cp "/Users/charliezhu/app/scala/adMetrics/target/scala-2.12/adMetrics-assembly-1.0.jar" foo.bar.Main
Hello sbt build
$ java -jar /Users/charliezhu/app/scala/adMetrics/target/scala-2.12/adMetrics-assembly-1.0.jar
Hello sbt build

// 19.8

#Scala call-by-name syntax, accept a block of code as a parameter.

def timer[A](blockOfCode: => A) = {
  val result = blockOfCode
  result
}

// 20.2 Prefer immutable objects

class Pizza {
  private val _toppings = new collection.mutable.ArrayBuffer[String]()  // <<<< 
  def toppings = _toppings.toList
  def addTopping(t: Topping) { _toppings += t } 
  def removeTopping(t: Topping) { _toppings -= t }
}

class Pizza {
  var names = Vector[String]()
  def addName(n: String) = names :+ n 
}

var pizza = new Pizza;
pizza.addName("Joy")
pizza.names 
pizza.names = pizza.addName("Joy")

val names = collection.mutable.ArrayBuffer[String]()
names += ("Tom","Sarah","Amy","Tiger")
names += "Tiger"

scala> names += "Tiger"
res3: names.type = ArrayBuffer(Tom, Sarah, Amy, Tom, Sarah, Amy, Tiger, Tiger)

scala> names -= "Tiger"
res4: names.type = ArrayBuffer(Tom, Sarah, Amy, Tom, Sarah, Amy, Tiger)

//
