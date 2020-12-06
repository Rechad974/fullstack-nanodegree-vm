-- Vagrant

Launch Vagrant

`vagrant up`

Stop Vagrant 

`vagrant halt`

SSH into VM
`vagrant ssh`

-- CRUD operation SQLAlchemy

Import libs, create engine, create session

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
```

Create (add function)

```python
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
```

Read 

```python
### One result

firstResult = session.query(Restaurant).first()
firstResult.name

### Multiple results
items = session.query(MenuItem).all()
for item in items:
    print item.name
```

Update

1) Find entry 
2) Reset value
3) Add to session (like for create value)
4) Execute the session commit

```python
### Find result

veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
```
  
```python
### Update entry

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 
```

Delete

1. Find the entry
2. Delete the entry
3. Execute the session commit