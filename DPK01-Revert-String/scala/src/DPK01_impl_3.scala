def reverseString3(s: String): String = {
    def reverseHelper(i: Int, reversed: String): String = {
        if (i < 0) then
            reversed  
        else
            reverseHelper(i - 1, reversed + s(i))  
    }
    
    reverseHelper(s.length - 1, "") 
}

@main def runImpl3(): Unit = {
    println(reverseString2("Hello"))
}