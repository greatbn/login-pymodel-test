from WebModel import Initialize, Login
from WebModel import enablers

actions = (Initialize, Login)


testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Incorrect'),
    (Login, ( 'user1', 'password1' ), 'Correct'),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Incorrect'),
  ],
  [
    (Initialize, (), None),
    (Login, ( 'user1', 'password1' ), 'Correct'), 
  ]
]
