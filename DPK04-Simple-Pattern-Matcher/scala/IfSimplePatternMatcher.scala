import scala.io.StdIn.readLine

def consoleInput(country: String): Unit =
  if country == "Usa" then
    println("Language is English")
  else if country == "Spain" then
    println("Language is Spanish")
  else if country == "Italy" then
    println("Language is Italian")
  else if country == "France" then
    println("Language is French")
  else if country == "Germany" then
    println("Language is German")
  else
    println("No valid value")
    
@main def run(): Unit =
  println("Please enter the country")
  val country = readLine()
  consoleInput(country)