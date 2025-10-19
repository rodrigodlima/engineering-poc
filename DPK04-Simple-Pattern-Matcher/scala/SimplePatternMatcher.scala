object SimpleMatcher {
    def matchLang(x: String): String = x match {
        case "Usa" => "English"
        case "Spain" => "Spanish"
        case "Italy" => "Italian"
        case "France" => "French"
        case "Germany" => "German"
    }

    def main(args: Array[String]): Unit = {
        println(matchLang("Usa"))
        println(matchLang("Spain"))
        println(matchLang("Italy"))
        println(matchLang("France"))
        println(matchLang("Germany"))
    }
}
