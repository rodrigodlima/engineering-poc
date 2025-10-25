def reverseString(s: String): String = {
    for (char <- s) {
        println(char)
    }
    s
}

def main(args: Array[String]): Unit = {
    val result = reverseString("Hello")
    println(result)
}