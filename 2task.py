```mermaid
classDiagram
class User {
    +UUID4 id
    +String name
    +String email
    +String password
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

class Place {
    +UUID4 id
    +String name
    +String description
    +String location
    +Float price
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
    +get_reviews()
}

class Review {
    +UUID4 id
    +String text
    +Float rating
    +UUID4 user_id
    +UUID4 place_id
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

class Amenity {
    +UUID4 id
    +String name
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

User "1" --> "*" Review : writes
Place "1" --> "*" Review : receives
Place "1" --> "*" Amenity : has
```
