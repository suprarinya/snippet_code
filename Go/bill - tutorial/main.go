package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	// "sort"
	// "strings"
)

var score = 99.5

func main() {

	// string
	// var nameOne string = "iris"
	// var nameTwo  = "renato"
	// var nameThree string
	// fmt.Println(nameOne, nameTwo, nameThree)

	// nameOne = "inari"
	// nameThree = "ren"
	// fmt.Println(nameOne, nameThree)

	// nameFour := "yoshi"
	// fmt.Println(nameFour)

	// ints
	// var ageOne int = 20
	// var ageTwo = 30
	// ageThree := 40
	// fmt.Println(ageOne, ageTwo, ageThree)

	// bits & memory
	// var numOne int8 = 100
	// var numTwo int8 = -128
	// var numThree uint = 25

	// float
	// var scoreOne float32 = 100.02
	// var scoreTwo float64 = 888888888888888888.22
	// scoreThree := 23.9998

	// age := 35
	// name := "Iris"

	// print
	// fmt.Print("hello,")
	// fmt.Print("world")

	// println
	// fmt.Println("add new line:")
	// fmt.Println("below")
	// fmt.Println("my age is", age, "and my name is", name)

	// printf (formatted string) - %_ format specifier
	// fmt.Printf("my age is %v and my name is %v\n", age, name)
	// fmt.Printf("my age is %q and my name is %q\n", age, name)
	// fmt.Printf("my age is %T and my name is %T\n", age, name)
	// fmt.Printf("you scored %.2f points!\n",  225.678)

	// Sprintf (save formatted strings)
	// str := fmt.Sprintf("my age is %v and my name is %v\n", age, name)
	// fmt.Println("the saved string is:", str)

	// array
	// var ages [3]int = [3]int {1,2,3}  
	// var ages = [3]int {1,2,3} 
	// names := [4]string{"Iris", "Ren", "Banan", "Sarah"}
	// names[1] = "Renato"
	// fmt.Println(ages, len(ages))
	// fmt.Println(names, len(names))

	// slices (use arrays under the hood)
	// var scores = []int{100,50, 60}
	// scores[2] = 25
	// scores = append(scores, 67)
	// fmt.Println(scores, len(scores))

	// slice ranges
	// rangeOne := names[1:3]
	// rangeTwo := names[2:]
	// rangeThree := names[:3]
	// rangeOne = append(rangeOne, "Bell")
	// fmt.Println(rangeOne, rangeTwo, rangeThree)

	// the standard library
	// greeting := "hello there friend!"

	// fmt.Println(strings.Split(greeting, " "))
	// fmt.Println(strings.Index(greeting, "there"))
	// fmt.Println(strings.Contains(greeting, "there"))
	// fmt.Println(strings.ReplaceAll(greeting, "hello", "hi"))
	// fmt.Println(strings.ToUpper(greeting))
	// // the original value is unchanged
	// fmt.Println("original string value = ", greeting)

	// ages := []int{45, 20, 35, 30, 75, 60, 65,25}

	// sort.Ints(ages)
	// fmt.Println(ages)

	// index := sort.SearchInts(ages, 30)
	// fmt.Println(index)

	// names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}
	// sort.Strings(names)
	// fmt.Println(names)
	// fmt.Println(sort.SearchStrings(names, "peach"))

	// loops
	// x := 0
	// for x < 5 {
	// 	fmt.Println("the value of x is: " , x)
	// 	x++
	// }

	// for i := 0; i < 5; i++ {
	// 	fmt.Println("the value of x is: " , i)
	// }

	// names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}

	// for i := 0; i < len(names); i++ {
	// 	fmt.Println("the value of x is: " , names[i])
	// }

	// for index, value := range names {
	// 	fmt.Println(index, " ", value)
	// }

	// for _, value := range names {
	// 	fmt.Println(value)
	// }

	// boolean & condition
	// age := 25
	// fmt.Println(age <= 50)
	// fmt.Println(age >= 50)
	// fmt.Println(age == 45)
	// fmt.Println(age != 50)

	// if age < 30 {
	// 	fmt.Println("age is less than 30")
	// } else if age < 40 {
	// 	fmt.Println("age is less than 40")
	// } else {
	// 	fmt.Println("age not is less than 45")
	// }

	// names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}

	// for index, value := range names {
	// 	if index == 1 {
	// 		fmt.Println("continuing at pos", index)
	// 		continue
	// 	}

	// 	if index > 2 {
	// 		fmt.Println("breaking at pos", index)
	// 		break
	// 	}


	// 	fmt.Printf("the value at %v, value is %v\n", index, value)
	// }

	// use function
	// sayGreeting("Iris")
	// sayGreeting("Ren")
	// sayBye("Iris")

	// names := []string{"Kara", "Seraphina"}
	// cycleNames(names, sayGreeting)
	// cycleNames(names, sayBye)

	// a1 := circleArea(10.5)
	// a2 := circleArea(12)
	// fmt.Println(a1, a2)
	// fmt.Printf("circle 1 is %0.3f and circle 2 is %.3f", a1, a2)

	// function - return multiple values
	// fn, sn := getInitials("iris belfa")
	// println(fn, sn)
	// fn2, sn2 := getInitials("Ren")
	// println(fn2, sn2)

	// package scope
	// sayHello("Mai")

	// for _, v := range points {
	// 	println(v)
	// }

	// showScore()

	// maps 
	// menu := map[string]float64{
	// 	"soup": 4.99,
	// 	"pie" : 7.99,
	// 	"salad" : 6.99,
	// 	"toffee pudding" : 3.55,
	// }

	// fmt.Println(menu)
	// // fmt.Println(menu["pie"])

	// // looping maps
	// for k,v := range menu {
	// 	fmt.Printf("The name of menu is %v, and the price is %v \n", k, v)
	// }

	// // ints as key type
	// phonebook := map[int]string{
	// 	1111: "ren",
	// 	2222: "kara",
	// 	3333: "iris",
	// }

	// fmt.Println(phonebook)
	// for k,v := range phonebook {
	// 	fmt.Printf("%v - %v \n", k, v)
	// }

	// phonebook[1111] = "ren2"
	// fmt.Println(phonebook)


	// pass-by value => GO make copies of variable passed 
	// into func -> that's why var name doesn't change value 
	// to "wedge"
	//  Non-pointer Values -> strings, ints, bools, flao
	// name := "tifa"

	// newName := updateName(name)
	// fmt.Println(name, newName)

	// fmt.Println("memeory address of name is: ", &name)

	// m := &name
	// fmt.Println("memory adddress: ", m)
	// fmt.Println("value of memory address: ", *m)

	// updateName(m)
	// fmt.Println(name)

	// //  Pointer Wrapper Values -> slices, maps, functions
	// menu := map[string]float64{
	// 	"pie"       : 5.95,
	// 	"ice creme" : 3.99,
	// }
	// updateMenu(menu)
	// fmt.Println(menu)

	// structs & custom types



	// myBill := newBill("iris's bill")

	// myBill.addItem("onion soup", 4.95)
	// myBill.addItem("meat pie", 4.25)
	// myBill.addItem("salad", 4.5)
	// myBill.addItem("coffee", 3.5)

	// myBill.updateTip(10)

	// fmt.Println(myBill.format())

	myBill := createBill()
	promptOptions(myBill)


}

func getInput(propmt string,r *bufio.Reader) (string, error) {
	fmt.Print(propmt)
	input, err := r.ReadString('\n')
	return strings.TrimSpace(input), err
}

func createBill() bill {
	reader  := bufio.NewReader(os.Stdin)

	promptOne := "Create a new bill name: "
	name, _ := getInput(promptOne, reader)

	b := newBill(name)
	fmt.Println("Created the bill - ", b.name)
	return b
}

func promptOptions(b bill)  {
	reader := bufio.NewReader(os.Stdin)

	opt, _ := getInput("Choose option (a - add item, s - save bill, t - add tip): ", reader)

	switch opt {
		case "a":
			name, _ := getInput("Item name: ", reader)
			price, _ := getInput("Item price: ", reader)

			p, err := strconv.ParseFloat(price, 64)
			if err != nil  {
				fmt.Println("The price must be a number")
				promptOptions(b)
			}
			b.addItem(name, p)

			fmt.Println("item added -", name, price)
			promptOptions(b)
		case "t":
			tip, _ := getInput("Enter tip amount ($): ", reader)

			t, err := strconv.ParseFloat(tip, 64)
			if err != nil  {
				fmt.Println("The tip must be a number")
				promptOptions(b)
			}
			b.updateTip(t)

			fmt.Println("Tip updated: ", tip)
			promptOptions(b)
		case "s":
			b.saveBill()
			fmt.Println("You save the file - ", b.name)
		default:
			fmt.Println("that was not a valid option")
			promptOptions(b)
		
	}
}

func updateName(x *string) string {
	*x = "wedge"
	return *x
}

func updateMenu(y map[string]float64) {
	y["coffee"] = 2.99
}

func sayGreeting(n string)  {
	fmt.Printf("Good morning %v \n", n)
}

func sayBye(n string)  {
	fmt.Printf("Goodbye %v \n", n)
}

func cycleNames(n []string, f func(string))  {
	for _, v := range n {
		f(v)
	}
}

func circleArea(r float64) float64 {
	area := math.Pi * r * r
	return area
}

func getInitials(n string) (string, string) {
	s := strings.ToUpper(n)
	names := strings.Split(s, " ")
	var initials [] string
	for _, v := range names {
		firstLetter := v[0:1]
		initials = append(initials, firstLetter)
	} 

	if len(initials) > 1 {
		return initials[0], initials[1]
	}

	return initials[0], "_"
}