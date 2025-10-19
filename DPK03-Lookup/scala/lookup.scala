object LookupApp extends App {
  case class Person(id: Int, name: String, email: String)

  val people = List(
    Person(1, "John", "john@john.jhon.com"),
    Person(2, "Alice", "alice@alice.com")
  )

  val idMap: Map[Int, Person] = people.map(p => p.id -> p).toMap
  val nameMap: Map[String, Person] = people.map(p => p.name -> p).toMap
  val emailMap: Map[String, Person] = people.map(p => p.email -> p).toMap

  def lookup(key: Any): Option[String] = key match {
    case id: Int       => idMap.get(id).map(_.name)
    case name: String if nameMap.contains(name) =>
      nameMap.get(name).map(_.email)
    case email: String if emailMap.contains(email) =>
      emailMap.get(email).map(_.name)
    case _ => None
  }

  println(lookup(1).getOrElse("Not found")) 
  println(lookup("John").getOrElse("Not found")) 
  println(lookup("john@john.jhon.com").getOrElse("Not found")) 
  println(lookup("desconhecido").getOrElse("Not found"))
}