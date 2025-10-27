def reverseString2(s: String): String = {
    var reversed = ""
    var i = s.length - 1
    while (i >= 0) do
        reversed = reversed + s(i)
        i -= 1
    end while
    reversed
}

def main(args: Array[String]): Unit = {
    println(reverseString2("Hello"))
}