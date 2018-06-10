var Dany = ['Daenerys', 'Targaryen', 22, 'House Targaryen', 'Valyrian', 'Queen of the Andals the Rhoynar and the First Men', 'Lady Regnant of the Seven Kingdoms', 'Protector of the Realm', 'Khaleesi of the Great Grass Sea', 'Breaker of Chains', 'Mother of Dragons', 'Queen of Meereen']
console.log(Dany[3]);
console.log(Dany.last_name);

var Dany = {
    first_name: 'Daenerys',
    last_name: 'Targaryen',
    age: 22,
    allegiance: 'House Targaryen',
    ancestry: 'Valyrian',
    titles: ['Queen of the Andals, the Rhoynar and the First Men', 'Lady Regent of the Seven Kingdoms', 'Protector of the Realm', 'Khaleesi of the Great Grass Sea', 'Breaker of Chains', 'Mother of Dragons', 'Queen of Meereen']
  }
  console.log(Dany.age);

var dojo = {};                                 // creates an empty object
dojo = {
    name: 'Coding Dojo',                         // property can store a string
    number_of_students: 25,                      // property can store a number
    instructors: ['Andrew', 'Michael', 'Jay'],   // property can store arrays
    location: {                                  // property can even store another object!
    city: 'San Jose',
    state: 'CA',
    zipcode: 95112
    },
    
}

console.log(dojo.name, dojo.number_of_students, dojo.instructors, dojo.location);// access object properties with dot (.) notation
console.log(dojo["name"]);                     // or bracket [] notation (note: specify key in quotes) After creating a new object we might 
console.log(dojo.name);




var glazedDonuts = [
    {
      frosting: 'glazed',
      style: 'cake',
      type: 'old fashioned',
      age: '45',
      time: 'minutes'
    },
    {
      frosting: 'glazed',
      style: 'yeast raised',
      type: 'regular',
      age: '5',
      time: 'minutes'
    },
    {
      frosting: 'glazed',
      style: 'yeast raised',
      type: 'jelly filled',
      age: '1',
      time: 'seconds'
    }
  ];

var purchase;
if((glazedDonuts[0].age < 25 && glazedDonuts[0].time == 'minutes') || glazedDonuts[0].time == 'seconds'){
  //shop owner
  purchase = glazedDonuts[0];
}
else {
  console.log('sorry it has been out a bit longer');
}

var numPurchase = 0;
for (var donut in glazedDonuts){
  console.log(glazedDonuts[donut].type);
  if((glazedDonuts[donut].age < 25 && glazedDonuts[donut].time == 'minutes') || glazedDonuts[donut].time == 'seconds'){
    numPurchase++;
  }
  else {
    console.log('not this donut...');
   }
}
console.log(numPurchase);
