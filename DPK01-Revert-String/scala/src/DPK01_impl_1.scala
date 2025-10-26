def reverseString(s: String): String = {
    var reversed = ""
    for (i <- s.length - 1 to 0 by -1) {
        reversed = reversed + s(i)
    }
    reversed
}

def main(args: Array[String]): Unit = {
    println(reverseString("Hello"))
}