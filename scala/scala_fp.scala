

19

Case class copy method

case class Person(name: String, age: Int)
val p = Person(name = "John 3", age = 18)
val p2 = p.copy(name = "Lee 4")

28 Partially-Applied Functions (and Currying)

def plus(a: Int)(b: Int) = a + b 
def plus2 = plus(2)(_)

plus2(3) 

val plusFn = (a:Int)(b:Int) => a + b  // error: not a legal formal parameter.

def add(a: Int, b: Int) = (a + b)
val addNewFn = add _

val addFn = (add _).curried
val addFn2 = addFn(2)
addFn2(3) // Int = 5

36 Recursion: Thinking Recursively

def reverseStr(str: String): String = str match {
  case "" => ""
  case x => reverseStr(x.tail) + x.head
}

def rev(str: String): String = str match {
  case "" => {
    val stackTraceAsArray = Thread.currentThread.getStackTrace
    stackTraceAsArray.foreach(println)
    ""
  }
  case x => { 
    rev(x.tail) + x.head
  }
}


def sum(list: List[Int]): Int = list match {
  case Nil => {
    // this manually creates a stack trace
    val stackTraceAsArray = Thread.currentThread.getStackTrace 
    stackTraceAsArray.foreach(println)
    0
  }
  case x :: xs => x + sum(xs)
}

val list = List.range(1, 5)
sum(list)

java.lang.Thread.getStackTrace(Thread.java:1559)
$line29.$read$$iw$$iw$.sum(<console>:14)
$line29.$read$$iw$$iw$.sum(<console>:18)
$line29.$read$$iw$$iw$.sum(<console>:18)
$line29.$read$$iw$$iw$.sum(<console>:18)
$line29.$read$$iw$$iw$.sum(<console>:18)

39 Tail-Recursive Algorithms 

import scala.annotation.tailrec

def sumAPI(l_out: List[Int]):Int = {
  @tailrec
  def sum(l_in: List[Int], accumulator: Int): Int = l_in match {
    case Nil => accumulator
    case x :: xs => sum(xs, x + accumulator)
  }

  sum(l_out, 0)
}

val list = List.range(1, 5)
sumAPI(list)

55 Opening Curly Brace

val x = FOO {
    // more code here
}

val x = FOO { (s: State) =>
    // more code here
}

trait Person {
  def name: String
  val hobby: String   // def is same as val, abstract val field, no assignment.
  val age: Int = 18   // = 18, mean concrete field, need override when instantiate.
  override def toString = s"name: $name, age: $age, hobby: $hobby"
}

val mary = new Person {
  val name = "mary"
  val hobby = "swim"
  override val age = 22 // concrete field in Trait/Abstract base class, need override when instantiate.
}

println(mary)
