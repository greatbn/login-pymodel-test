from WebModel import Login, Initialize

actions = (Initialize, Login,)
testSuite = [
  [
    (Initialize, (), None),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Incorrect'),
    (Login, ( 'user1', 'password1' ), 'Correct'),
    (Login, ( 'VinniPuhh', 'Incorrect' ), 'Incorrect'),  # cannot login because user1 already login
  ]
]
