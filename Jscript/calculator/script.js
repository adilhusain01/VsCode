/// Circumference of a circle
/*const pi = 3.14;
let radius, circumference;
radius = window.prompt("Enter the radius : ");
radius = Number(radius);
circumference = 2 * pi * radius;
console.log(circumference);
*/




/// Math function

/*
let x=5.956,p=10,z=30;

y= Math.pow(x,2);
y= Math.round(x);
y= Math.ceil(x);
y= Math.floor(x);
y= Math.sqrt(x);
y= Math.abs(x);
y=Math.max(x,p,z);
y=Math.min(x,p,z);
y=Math.PI;

*/
//console.log(y);


/// Hpotenuse of a right angled triangle

/*
let p,b,h;
document.getElementById("b").onclick=function(){
    p=document.getElementById("P").value;
    p=Number(p);
    b=document.getElementById("B").value;
    b=Number(b);
    z=Math.pow(p,2) + Math.pow(b,2);
    h = Math.sqrt(z);
    console.log(h);
}
*/

/*
let p,b,h;
p=window.prompt("Enter p : ");
b=window.prompt("Enter b");

h=Math.sqrt(Math.pow(p,2) + Math.pow(b,2));
console.log(h);
*/



/*
let count=0;
document.getElementById("low").onclick = function(){
    count-=1;
    document.getElementById("para").innerHTML=count;
}
document.getElementById("reset").onclick = function(){
    count=0;
    document.getElementById("para").innerHTML=count;
}
document.getElementById("high").onclick = function(){
    count+=1;
    document.getElementById("para").innerHTML=count;
}
*/



/// String functions
/*
let stra=" Hi Andoromada Galaxy ";
let number="123-456-789";

console.log(stra.length);
console.log(stra.charAt(1));
console.log(stra.indexOf("a"));
console.log(stra.lastIndexOf("a"));
console.log(stra.trim());
console.log(stra.toUpperCase());
console.log(stra.toLowerCase());
console.log(number.replaceAll("-",""));
*/


/// Slicing the string
/*
let stra="Snoop Dogg";
let firstname,lastname;
console.log(stra.slice(0,stra.indexOf(" ")));
console.log(stra.slice(stra.indexOf(" ")+1));
*/

/// Method chaining
/*
let stra=" Hi Andromada Galaxy ";
console.log(stra.trim().slice(0,2).toUpperCase());
*/


/// if-else
/*
let age=16;

if(age>18){
    console.log("major");
} else if(age==18){
    console.log("neutral");
} else{
    console.log("minor");
}
*/


/// Checked boxes and radio buttons
/*
document.getElementById("b1").onclick=function(){
    if (document.getElementById("i1").checked){
        console.log("True");
    } else {
        console.log("False");
    }
}
*/

/*
document.getElementById("b1").onclick=function(){
    if (document.getElementById("male").checked){
        console.log("Male");
    } else  if  (document.getElementById("female").checked){
        console.log("Female");
    } else {
        console.log("No input");
    }
}
*/


/// for loop
/*
for (let i=1; i<=100; i++){
    console.log(i);
}
*/

// Area of  rectabgle using functions

/*
let length,breadth;
length = window.prompt("Enter the l : ");
breadth = window.prompt("Enter the b : ");
area(length,breadth);

function area(l,b){
    let area = l*b;
    console.log("The area is  :: ",area);
}
*/


/// Template literals
/*
let name = "Adil husain";
console.log(`Hello ${name}`);
*/


/// toLocaleString

/*
let num=50;

num = num.toLocaleString("en-US");
num = num.toLocaleString("hi-IN");
num = num.toLocaleString("de-DE");

num = num.toLocaleString("hi-IN",{style:"currency",currency:"INR"});
num = num.toLocaleString("en-US",{style:"currency",currency:"USD"});
num = num.toLocaleString("de-DE",{style:"currency",currency:"EUR"});

num = num.toLocaleString(undefined,{style:"percent"});
num = num.toLocaleString(undefined,{style:"unit",unit:"celsius"});

console.log(num);
*/



/// Number Guessing game

/*
let num=(Math.floor(Math.random()*10+1));
console.log(num);

let guesses=0;
document.getElementById("b1").onclick=function(){

    let guess=document.getElementById("i1").value;
    guesses+=1;
    if (guess==num){
        document.getElementById("p1").innerHTML=`It took ${guesses} guesses to guess #`;
    } else if (guess<num){
        document.getElementById("p1").innerHTML="Too small!";
    }  else if (guess>num){
        document.getElementById("p1").innerHTML="Too large!";
    } else {
        document.getElementById("p1").innerHTML="Invalid Input!";
    }
}
*/


/// Temperature Converter
/*
document.getElementById("b1").onclick = function() {
    let val=document.getElementById("i3").value;
    let output;
    if (document.getElementById("i1").checked){
        output=(val-32)/(9/5);
        document.getElementById("p1").innerHTML=output +" °C";
    } else if (document.getElementById("i2").checked){
        output=(val*(9/5)+32);
        document.getElementById("p1").innerHTML=output +" °F";
    }
}
*/



/// Spread operator
/*
let arr = [1,2,3,4,5,6,7,8,9];
let drr = [9,8,7,6,5,4,3,2,1];
console.log(...arr);
arr.push(...drr);
console.log(...arr);
*/



/// Rest parameters

/*
let a=1;
let b=2;
let c=3;
let d=4;

console.log(sum(a,b,c,d));
function sum(...numbers){
    let total = 0;
    for (let number of numbers){
        total += number;
    }
    return total;
}
*/


/// forEach function array
/* 
let arr=[[1,2,3],[4,5,6],[7,8,9]];
arr.forEach(sum);

function sum(array){
    let total=0;
    for(let i=0;i< array.length;i++){
        total+=array[i];
    }
    print(total);
}

function print(element){
    console.log(element);
}
*/



///  map array
// Passes array elemets  and then makes the output as a new array in a new variable
/*
let numbers = [1,2,3,4,5,6,7,8,9];

let squares = numbers.map(square);
squares.forEach(print);

function square(number){
    let sq=Math.pow(number,2);
    return sq;
}

function print(element){
    console.log(element);
}
*/


/// filter array

//Makes a new array with only valid values through a defined function
/*
let ages=[12,13,14,15,16,18,21,17,19];

let adults = ages.filter(chkage);
adults.forEach(print);

function chkage(element){
    return element>=18;
}

function print(element){
    console.log(element);
}
*/


/// reduce array
// reduces array to a single value
/*
let arr = [5, 10, 15, 20, 25];

let sum = arr.reduce(reduced);
console.log(sum);

function reduced(total, element) {
    return total + element;
}
*/



/// sort array
/*
let arr = [75,30,45,60,90,100];

let brr = arr.sort(z2asort);

brr.forEach(print);

function a2zsort(x,y){
    return x-y;
}
function z2asort(x,y){
    return y-x;
}

function print(element){
    console.log(element);
}
*/


/// function expression

/*
let a = function(){
    console.log("Hello");
}
a();
*/

/*
let count=0;
function decreaseCount(){
    count-=1;
    document.getElementById("h1").innerHTML=count;
}
function increaseCount(){
    count+=1;
    document.getElementById("h1").innerHTML=count;
}
*/


/// Arrow function
/*
let name = (username) => (console.log(username));
name("Bro");
*/
/*
let calc = (x,y) => (console.log((x/y)*100));
calc(9,5);
*/

/*
let arr=[8,7,6,5,4,3,2,1];
arr.sort(sorting);

function sorting(x,y){
    return x-y;
}

function print(element){
    console.log(element);
}

arr.forEach(print);

console.log("\n");
*/

/*
let arr=[8,7,6,5,4,3,2,1];
arr.sort((x,y)=>(x-y));
arr.forEach((element) => console.log(element));
*/



//Cards shuffling using an array
/*
let cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q"];
function shuffle(arr){
    let currentIndex = cards.length;
    while (currentIndex!=0){
        let num = Math.floor(Math.random()*(cards.length));
        currentIndex-=1;
        temp=arr[currentIndex];
        arr[currentIndex]=arr[num];
        arr[num]=temp;
    }

    return arr;
}
shuffle(cards);
cards.forEach(card => console.log(card));
*/




/// Map
/*
let a = new Map([
    ["A",65],
    ["B",66],
    ["C",67]
]);

let shoppingcart=0;
shoppingcart += a.get("A");
console.log(shoppingcart);

a.set("D",68);
console.log(a);

a.delete("D");
console.log(a);

console.log(a.has("A"));

console.log(a.size);

a.forEach((value,key)=>console.log(key, value));
*/



// OBJECT 
/*
let car = {
    model:"e-Tron",
    company:"Audi",
    manf:"1998",

    drive:function(){
        console.log("You drive this car");
    }
};

console.log(car.drive);
*/

/// this keyword
/*
let company1 = {
    employees:"55",
    niche:"Soda",

    work:function(){
        console.log(`Do wash ${this.niche} bottles`);
    }
}

let company2 = {
    employees:"69",
    niche:"Pepsi",

    work:function(){
        console.log(`Do wash ${this.niche} bottles`);
    }
}

company1.work();
company2.work();
*/

// Class 
/*
class player{
    score = 0;

    pause(){
        console.log(`Player has paused tha Game and the score is ${this.score}.`);
    }
    
    resume(){
        console.log(`Player has resumed tha Game and the score is ${this.score}.`);
    }
}

let player1 = new player();
player1.score=20;
player1.resume();
*/



/// Constructor [It lies inside class and its work is to accept arguements and assign properties]
/*
class students{
    constructor(name,age,gender){
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    info(){
        console.log(`This student ${this.name} is of age ${this.age} and is of gender ${this.gender}.`);
    }
}

let student1 = new students("Alex",9,"Male");
student1.info();
*/



/// static in classes
// useful for the caches, fixed-config, useful for utility functionss
/*
class car{
    static cars=0;
    constructor(model){
        this.model=model;
        car.cars+=1;
    }

    static run(){
        console.log("3.....2....1.....! GOO");
    }
}


let car1 = new car("Audi");
let car2 = new car("Audi");
let car3 = new car("Audi");

car.run();
*/


// class inheritance 
// to reduce the lines of code, we refrence the individual classes to a single extended class

/*
class normal{
    honks = true;
    fuel = true;

    ok(){
        console.log(`You can honk and shit in this car`);
    }
}

class audi extends normal{
    name = "A8";
}
class merc extends normal{
    name = "A8";
}
class bugatti extends normal{
    name = "A8";
}

let merc1 = new merc(); 
merc1.ok();
*/




/// get property in class


class student{
    constructor(name,age,gender){
        this._name=name;
        this._age=age;
        this._gender=gender;
    }

    get name(){
        return this._name;
    }
}

let s1 = new student("Adil",19,"Male");
************************************************************************************************************************************x
console.log(s1.name);